from helpers import flatten, iDecode

from viewdefs import TP_LABELS, ITEM_STYLE


def csv(data):
    """converts an data structure of rows and fields into a csv string.
    With proper quotations and escapes
    """
    result = []
    if data is not None:
        for row in data:
            prow = [str(x) for x in row]
            trow = [
                f'''"{x.replace('"', '""')}"''' if '"' in x or "," in x else x
                for x in prow
            ]
            result.append((",".join(trow)).replace("\n", " ").replace("\r", " "))
    return "\n".join(result)


class CSVDATA:
    def __init__(self, Check, Record, Word, Query, auth, PASSAGE_DBS):
        self.Check = Check
        self.Record = Record
        self.Word = Word
        self.Query = Query
        self.auth = auth
        self.PASSAGE_DBS = PASSAGE_DBS

    def page(self):
        Check = self.Check
        Record = self.Record

        vr = Check.field("material", "", "version")
        iidRep = Check.field("material", "", "iid")
        mr = Check.field("material", "", "mr")
        qw = Check.field("material", "", "qw")
        tp = Check.field("material", "", "tp")
        extra = Check.field("rest", "", "extra")

        (iid, keywords) = iDecode(qw, iidRep)
        iidRep2 = iDecode(qw, iidRep, rsep=" ")
        fileName = f"{vr}_{ITEM_STYLE[qw]['t']}{iidRep2}_{TP_LABELS[tp]}{extra}.csv"
        (authorized, msg) = Record.authRead(mr, qw, iidRep)

        if not authorized:
            return dict(fileName=fileName, data=msg)

        hebrewFields = Check.fields(tp, qw=qw)
        data = self.get(vr, mr, qw, iid, keywords, tp, extra, hebrewFields, fileName)
        return dict(fileName=fileName, data=data)

    def get(self, vr, mr, qw, iid, keywords, tp, extra, hebrewFields, fileName):
        Word = self.Word
        Query = self.Query
        auth = self.auth
        PASSAGE_DBS = self.PASSAGE_DBS

        if extra:
            extra = "_" + extra
        if len(extra) > 64:
            extra = extra[0:64]

        headRow = ["book", "chapter", "verse"] + [hf[1] for hf in hebrewFields]

        if qw == "n":
            keywordsSql = keywords.replace("'", "''")
            myId = auth.user.id if auth.user is not None else None
            extra = "" if myId is None else f" or created_by = {myId} "

            hflist = ", ".join(hf[0] for hf in hebrewFields)
            sql = f"""
select
    shebanq_note.note.book, shebanq_note.note.chapter, shebanq_note.note.verse,
    {hflist}
from shebanq_note.note
inner join book on shebanq_note.note.book = book.name
inner join clause_atom on clause_atom.ca_num = shebanq_note.note.clause_atom
    and clause_atom.book_id = book.id
where shebanq_note.note.keywords like '% {keywordsSql} %'
    and shebanq_note.note.version = '{vr}'
    and (shebanq_note.note.is_shared = 'T' {extra})
;
"""
            dataRows = PASSAGE_DBS[vr].executesql(sql) if vr in PASSAGE_DBS else []
        else:
            (nSlots, slotSets) = (
                Query.read(vr, iid) if qw == "q" else Word.read(vr, iid)
            )
            slots = flatten(slotSets)
            dataRows = []
            if len(slots):
                hflist = ", ".join(f"word.{hf[0]}" for hf in hebrewFields)
                slotsVal = ",".join(str(x) for x in slots)
                sql = f"""
select
    book.name, chapter.chapter_num, verse.verse_num,
    {hflist}
from word
inner join word_verse on
    word_verse.anchor = word.word_number
inner join verse on
    verse.id = word_verse.verse_id
inner join chapter on
    verse.chapter_id = chapter.id
inner join book on
    chapter.book_id = book.id
where
    word.word_number in ({slotsVal})
order by
    word.word_number
;
"""
                dataRows = PASSAGE_DBS[vr].executesql(sql) if vr in PASSAGE_DBS else []
        allRows = csv([headRow] + list(dataRows))
        return allRows
