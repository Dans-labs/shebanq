from books import BOOKS
from verse import VERSE
from viewsettings import VIEWSETTINGS
from word import WORD
from query import QUERY
from querychapter import QUERYCHAPTER
from querysave import QUERYSAVE
from querytree import QUERYTREE
from queryrecent import QUERYRECENT
from note import NOTE
from notesave import NOTESAVE
from notesupload import NOTESUPLOAD
from notetree import NOTETREE
from record import RECORD, RECORDQUERY
from materials import MATERIAL
from side import SIDE
from chart import CHART
from csvdata import CSVDATA


# it is essential that this is performed at the start
# of each Hebrew reuqest
# The first time it computes a query-chapter index.
# All subsequent times, it takes the index from cache.
# If a page would succeed before building this index,
# it might get a sidebar with insufficient material,
# and the insufficient material alrerady cached.


def init():
    QueryChapter = QUERYCHAPTER()
    QueryChapter.makeQCindexes()


def books():
    """Get all bible book names in all their translations.

    This is a utility page for website users.
    This controller is not used by other parts of the webapp.

    See also [books.BOOKS.getNames][].
    """
    Books = BOOKS()
    session.forget(response)
    return Books.getNames()


def text():
    """Serves a **text** page.

    Corresponds with `Text` in the menu bar.

    Only the skeleton of the page is fetched.

    See also [viewsettings.VIEWSETTINGS.page][].
    """
    session.forget(response)
    init()
    Books = BOOKS()
    ViewSettings = VIEWSETTINGS(Books)
    ViewSettings.initState()
    return ViewSettings.page()


def words():
    """Serves **words** overview pages.

    Corresponds with `Words` in the menu bar.

    The words are fetched in pages off all words starting with the same letter.
    """
    session.forget(response)
    init()
    Books = BOOKS()
    ViewSettings = VIEWSETTINGS(Books)
    ViewSettings.initState()
    Word = WORD()
    return Word.page(ViewSettings)


def queries():
    """Serves the **queries** overview page.

    Corresponds with `Queries` in the menu bar.

    The main part is the tree of queries.
    There is also a widget with recent queries and a control to add new queries.
    """
    session.forget(response)
    init()
    Books = BOOKS()
    ViewSettings = VIEWSETTINGS(Books)
    ViewSettings.initState()
    Query = QUERY()
    return Query.page(ViewSettings)


def notes():
    """Serves the **notes** overview page.

    Corresponds with `Notes` in the menu bar.

    The main part is the tree of note sets.
    There is also a widget for bulk uploading sets of notes.
    """
    session.forget(response)
    init()
    Books = BOOKS()
    ViewSettings = VIEWSETTINGS(Books)
    ViewSettings.initState()
    Note = NOTE(Books)
    return Note.page(ViewSettings)


def word():
    """Serves a *word* **record** page.

    Usually an overview page or from a shared link.

    The page consists of a sidebar with the details of the word,
    and the main area displays the occurrences.
    """
    session.forget(response)
    request.vars["mr"] = "r"
    request.vars["qw"] = "w"
    request.vars["page"] = 1
    return ()


def query():
    """Serves a *query* **record** page.

    Usually an overview page or from a shared link.

    The page consists of a sidebar with the details of the query,
    and the main area displays the results.
    """
    session.forget(response)
    request.vars["mr"] = "r"
    request.vars["qw"] = "q"
    if request.extension == "json":
        Query = QUERY()
        return Query.bodyJson()
    else:
        request.vars["page"] = 1
    return ()


def note():
    """Serves a *notes set* **record** page.

    Usually from an overview page or a shared link.

    The page consists of a sidebar with the details of the notes set,
    and the main area displays the notes between the verses.
    """
    session.forget(response)
    request.vars["mr"] = "r"
    request.vars["qw"] = "n"
    request.vars["page"] = 1
    return ()


def material():
    """Serves AJAX call for HTML content for the main area.

    Client code: [materialfetch][].
    """
    session.forget(response)
    Books = BOOKS()
    Word = WORD()
    Query = QUERY()
    Note = NOTE(Books)
    RecordQuery = RECORDQUERY(Query)
    Material = MATERIAL(RecordQuery, Word, Query, Note)
    return Material.page()


def verse():
    """Get the linguistic data of a verse.

    See also [verse.VERSE.get][].

    Client code: [materialaddverserefs][].
    """
    session.forget(response)
    Verse = VERSE()
    return Verse.get()


def sidematerial():
    """Serves AJAX call for HTML content for the sidebar (**main** page).

    Client code: [sidecontentfetch][].
    """
    session.forget(response)
    Books = BOOKS()
    Word = WORD()
    Query = QUERY()
    Note = NOTE(Books)
    RecordQuery = RECORDQUERY(Query)
    Material = MATERIAL(RecordQuery, Word, Query, Note)
    Side = SIDE(Material, Word, Query, Note)
    return Side.page()


def sideword():
    """Serves AJAX call for HTML content for the sidebar (*word* **record** page).

    Used when the user is switching between **main** and **record** pages.

    See also [record.RECORD.body][].

    Client code: [sidecontentfetch][].
    """
    session.forget(response)
    Record = RECORD()
    return Record.body()


def sidequery():
    """Serves AJAX call for HTML content for the sidebar (*query* **record** page).

    Used when the user is switching between **main** and **record** pages.

    See also [record.RECORD.body][].

    Client code: [sidecontentfetch][].
    """
    session.forget(response)
    Record = RECORD()
    return Record.body()


def sidenote():
    """Serves AJAX call for HTML content for the sidebar (*note set* **record** page).

    Used when the user is switching between **main** and **record** pages.

    See also [record.RECORD.body][].

    Client code: [sidecontentfetch][].
    """
    session.forget(response)
    Record = RECORD()
    return Record.body()


def sidewordbody():
    """Serves AJAX call for HTML content for the sidebar (*word* **record** page).

    Used when the user is loading *word* page directly.

    See also [word.WORD.body][].
    """
    session.forget(response)
    if not request.ajax:
        redirect(URL("hebrew", "word", extension="", vars=request.vars))
    Word = WORD()
    return Word.body()


def sidequerybody():
    """Serves AJAX call for HTML content for the sidebar (*query* **record** page).

    Used when the user is loading a *query* page directly.

    See also [query.QUERY.body][].
    """
    session.forget(response)
    if not request.ajax:
        redirect(URL("hebrew", "query", extension="", vars=request.vars))
    Query = QUERY()
    return Query.body()


def sidenotebody():
    """Serves AJAX call for HTML content for the sidebar (*notes set* **record** page).

    Used when the user is loading a *notes set* page directly.

    See also [note.NOTE.body][].
    """
    session.forget(response)
    if not request.ajax:
        redirect(URL("hebrew", "note", extension="", vars=request.vars))
    Books = BOOKS()
    Note = NOTE(Books)
    return Note.body()


def queriesr():
    """Serves AJAX call for json data for recently saved shared queries.

    See also [queryrecent.QUERYRECENT.recent].

    Client code: [queryrecentfetch][]
    """
    session.forget(response)
    QueryRecent = QUERYRECENT()
    return QueryRecent.recent()


def querytree():
    """Serves AJAX call for json data for the tree overview of queries.

    See also [querytree.QUERYTREE.get][].

    Client code: [querytreetree][]
    """
    session.forget(response)
    QueryTree = QUERYTREE()
    return QueryTree.get()


def notetree():
    """Serves AJAX call for json data for the tree overview of notes sets.

    See also [notetree.NOTETREE.get][].

    Client code: [notetreetree][]
    """
    session.forget(response)
    NoteTree = NOTETREE()
    return NoteTree.get()


def getversenotes():
    """Serves AJAX call for json data for all notes belonging to a single verse.

    See also [note.NOTE.getVerseNotes][].

    Client code: [noteversefetch][]
    """
    session.forget(response)
    Books = BOOKS()
    Note = NOTE(Books)
    return Note.getVerseNotes()


def putversenotes():
    """Serves AJAX call for json data to save notes.

    See also [notesave.NOTESAVE.putVerseNotes][].

    Client code: [noteversesendnotes][]
    """
    session.forget(response)
    Books = BOOKS()
    Note = NOTE(Books)
    NoteSave = NOTESAVE(Note)
    return NoteSave.putVerseNotes()


def noteupload():
    """Receives bulk-uploaded notes and stores them.

    See also [notesupload.NOTESUPLOAD.upload][].

    Client code: [uploadsubmit][].
    """
    session.forget(response)
    Books = BOOKS()
    Note = NOTE(Books)
    NotesUpload = NOTESUPLOAD(Books, Note)
    return NotesUpload.upload()


def item():
    """Get csv data of the items associated with a record.

    Items are:
    the occurrences of a word, the results of a query, the notes of a notes set.

    See also [csvdata.CSVDATA.page][].

    Client code: [viewstatecsvurl][].
    """
    session.forget(response)
    Word = WORD()
    Query = QUERY()
    RecordQuery = RECORDQUERY(Query)
    CsvData = CSVDATA(RecordQuery, Word, Query)
    return CsvData.page()


def chart():  # controller to produce a chart of query results or lexeme occurrences
    """Get a heat map of the items associated to a record.

    Items are:
    the occurrences of a word, the results of a query, the notes of a notes set.

    See also [chart.CHART.page][].

    Client code: [chartfetch][].
    """
    session.forget(response)
    Books = BOOKS()
    Word = WORD()
    Query = QUERY()
    Note = NOTE(Books)
    RecordQuery = RECORDQUERY(Query)
    Chart = CHART(Books, RecordQuery, Word, Query, Note)
    return Chart.page()


def itemrecord():
    """Saves a record to the database, typically organizations, projects, queries.

    See also [record.RECORD.setItem][].

    Client code: [treerecord][].
    """
    session.forget(response)
    Query = QUERY()
    RecordQuery = RECORDQUERY(Query)
    return RecordQuery.setItem()


def querysharing():
    """Saves the shared status of a query to the database.

    See also [querysave.QUERYSAVE.sharing][].

    Client code: [sidecontentsendval][].
    """
    session.forget(response)
    Query = QUERY()
    QueryChapter = QUERYCHAPTER()
    QuerySave = QUERYSAVE(Query, QueryChapter)
    return QuerySave.sharing()


def queryupdate():
    """Saves metadata of a query to the database.

    See also [querysave.QUERYSAVE.putRecord][].

    Client code: [sidecontentsendval][].
    """
    session.forget(response)
    Query = QUERY()
    QueryChapter = QUERYCHAPTER()
    QuerySave = QUERYSAVE(Query, QueryChapter)
    return QuerySave.putRecord()
