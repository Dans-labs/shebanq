#!/usr/bin/env python
#-*- coding:utf-8 -*-

booklangs = {
'Hebrew': dict(
    la=(u'latin', u'Latina'),
    en=(u'english', u'English'),
    fr=(u'french', u'Français'),
    de=(u'german', u'Deutsch'),
    nl=(u'dutch', u'Nederlands'),
    el=(u'greek', u'Ελληνικά'),
    he=(u'hebrew', u'עברית'),
    ru=(u'russian', u'Русский'),
    es=(u'spanish', u'Español'),
    ko=(u'korean', u'한국어'),
    sw=(u'swahili', u'Kiswahili'),
    tr=(u'turkish', u'Türkçe'),
    id=(u'indonesian', u'Bahasa Indonesia'),
    ar=(u'arabic', u'العَرَبِية'),
    zh=(u'chinese', u'中文'),
    hi=(u'hindi', u'हिन्दी'),
    fa=(u'farsi', u'فارسی'),
    pt=(u'portuguese', u'Português'),
    syc=(u'syriac', u'ܠܫܢܐ ܣܘܪܝܝܐ'),
    da=(u'danish', u'Dansk'),
    am=(u'amharic', u'ኣማርኛ'),
    bn=(u'bengali', u'বাংলা'),
    ja=(u'japanese', u'日本語'),
    pa=(u'punjabi', u'ਪੰਜਾਬੀ'),
    ur=(u'urdu', u'اُردُو'),
    yo=(u'yoruba', u'èdè Yorùbá'),
),
'Greek': dict(
    la=(u'latin', u'Latina'),
    en=(u'english', u'English'),
),
}
booknames = {
'Hebrew': dict(
    la=tuple(u'''
            Genesis
            Exodus
            Leviticus
            Numeri
            Deuteronomium
            Josua
            Judices
            Samuel_I
            Samuel_II
            Reges_I
            Reges_II
            Jesaia
            Jeremia
            Ezechiel
            Hosea
            Joel
            Amos
            Obadia
            Jona
            Micha
            Nahum
            Habakuk
            Zephania
            Haggai
            Sacharia
            Maleachi
            Psalmi
            Iob
            Proverbia
            Ruth
            Canticum
            Ecclesiastes
            Threni
            Esther
            Daniel
            Esra
            Nehemia
            Chronica_I
            Chronica_II
    '''.strip().split()),
    en=tuple(u'''
            Genesis
            Exodus
            Leviticus
            Numbers
            Deuteronomy
            Joshua
            Judges
            1_Samuel
            2_Samuel
            1_Kings
            2_Kings
            Isaiah
            Jeremiah
            Ezekiel
            Hosea
            Joel
            Amos
            Obadiah
            Jonah
            Micah
            Nahum
            Habakkuk
            Zephaniah
            Haggai
            Zechariah
            Malachi
            Psalms
            Job
            Proverbs
            Ruth
            Song_of_songs
            Ecclesiastes
            Lamentations
            Esther
            Daniel
            Ezra
            Nehemiah
            1_Chronicles
            2_Chronicles
    '''.strip().split()),
    nl=tuple(u'''
            Genesis
            Exodus
            Leviticus
            Numeri
            Deuteronomium
            Jozua
            Richteren
            1_Samuel
            2_Samuel
            1_Koningen
            2_Koningen
            Jesaja
            Jeremia
            Ezechiel
            Hosea
            Joël
            Amos
            Obadja
            Jona
            Micha
            Nahum
            Habakuk
            Zefanja
            Haggaï
            Zacharia
            Maleachi
            Psalmen
            Job
            Spreuken
            Ruth
            Hooglied
            Prediker
            Klaagliederen
            Esther
            Daniel
            Ezra
            Nehemia
            1_Kronieken
            2_Kronieken
        '''.strip().split()),
    de=tuple(u'''
            Genesis
            Exodus
            Levitikus
            Numeri
            Deuteronomium
            Josua
            Richter
            1_Samuel
            2_Samuel
            1_Könige
            2_Könige
            Jesaja
            Jeremia
            Ezechiel
            Hosea
            Joel
            Amos
            Obadja
            Jona
            Micha
            Nahum
            Habakuk
            Zefanja
            Haggai
            Sacharja
            Maleachi
            Psalmen
            Ijob
            Sprichwörter
            Rut
            Hoheslied
            Kohelet
            Klagelieder
            Ester
            Daniel
            Esra
            Nehemia
            1_Chronik
            2_Chronik
        '''.strip().split()),
    fr=tuple(u'''
            Genèse
            Exode
            Lévitique
            Nombres
            Deutéronome
            Josué
            Juges
            1_Samuel
            2_Samuel
            1_Rois
            2_Rois
            Isaïe
            Jérémie
            Ézéchiel
            Osée
            Joël
            Amos
            Abdias
            Jonas
            Michée
            Nahoum
            Habaquq
            Sophonie
            Aggée
            Zacharie
            Malachie
            Psaumes
            Job
            Proverbes
            Ruth
            Cantique_des_Cantiques
            Ecclésiaste
            Lamentations
            Esther
            Daniel
            Esdras
            Néhémie
            1_Chroniques
            2_Chroniques
        '''.strip().split()),
    el=tuple(u'''
            Γένεση
            Έξοδος
            Λευιτικό
            Αριθμοί
            Δευτερονόμιο
            Ιησούς
            Κριταί
            Σαμουήλ_A'                    
            Σαμουήλ_Β'
            Βασιλείς_A'
            Βασιλείς_Β'
            Ησαΐας
            Ιερεμίας
            Ιεζεκιήλ
            Ωσηέ
            Ιωήλ
            Αμώς
            Οβδιού
            Ιωνάς
            Μιχαίας
            Ναούμ
            Αβακκούμ
            Σοφονίας
            Αγγαίος
            Ζαχαρίας
            Μαλαχίας
            Ψαλμοί
            Ιώβ
            Παροιμίαι
            Ρουθ
            Άσμα_Ασμάτων
            Εκκλησιαστής
            Θρήνοι
            Εσθήρ
            Δανιήλ
            Έσδρας
            Νεεμίας
            Χρονικά_Α'
            Χρονικά_Β'
        '''.strip().split()),
    he=tuple(u'''
            בראשית
            שמות
            ויקרא
            במדבר
            דברים
            יהושע
            שופטים
            שמואל_א
            שמואל_ב
            מלכים_א
            מלכים_ב
            ישעיהו
            ירמיהו
            יחזקאל
            הושע
            יואל
            עמוס
            עובדיה
            יונה
            מיכה
            נחום
            חבקוק
            צפניה
            חגי
            זכריה
            מלאכי
            תהילים
            איוב
            משלי
            רות
            שיר_השירים
            קהלת
            איכה
            אסתר
            דניאל
            עזרא
            נחמיה
            דברי_הימים_א
            דברי_הימים_ב
        '''.strip().split()),
    ru=tuple(u'''
            Бытия
            Исход
            Левит
            Числа
            Второзаконие
            ИисусНавин
            КнигаСудей
            1-я_Царств
            2-я_Царств
            3-я_Царств
            4-я_Царств
            Исаия
            Иеремия
            Иезекииль
            Осия
            Иоиль
            Амос
            Авдия
            Иона
            Михей
            Наум
            Аввакум
            Софония
            Аггей
            Захария
            Малахия
            Псалтирь
            Иов
            Притчи
            Руфь
            ПесниПесней
            Екклесиаст
            ПлачИеремии
            Есфирь
            Даниил
            Ездра
            Неемия
            1-я_Паралипоменон
            2-я_Паралипоменон
    '''.strip().split()),
    es=tuple(u'''
            Génesis
            Éxodo
            Levítico
            Números
            Deuteronomio
            Josué
            Jueces
            1_Samuel
            2_Samuel
            1_Reyes
            2_Reyes
            Isaías
            Jeremías
            Ezequiel
            Oseas
            Joel
            Amós
            Abdías
            Jonás
            Miqueas
            Nahúm
            Habacuc
            Sofonías
            Hageo
            Zacarías
            Malaquías
            Salmos
            Job
            Proverbios
            Rut
            Cantares
            Eclesiastés
            Lamentaciones
            Ester
            Daniel
            Esdras
            Nehemías
            1_Crónicas
            2_Crónicas
    '''.strip().split()),
    ko=tuple(u'''
            창세기
            탈출기
            레위기
            민수기
            신명기
            여호수아
            재판관기
            사무엘_첫째
            사무엘_둘째
             열왕기_첫째
            열왕기_둘째
            이사야
            예레미야
            에스겔
            호세아
            요엘
            아모스
            오바댜
            요나
            미가
            나훔
            하박국
            스바냐
            학개
            스가랴
            말라기
            시편
            욥
            잠언
            룻
            솔로몬의_노래
            전도서
            애가
            에스더
            다니엘
            에스라
            느헤미야
            역대기_첫째
            역대기_둘째
    '''.strip().split()),
    sw=tuple(u'''
            Mwanzo
            Kutoka
            Mambo_ya_Walawi
            Hesabu
            Kumbukumbu_la_Torati
            Yoshua
            Waamuzi
            1_Samweli
            2_Samweli
            1_Wafalme
            2_Wafalme
            Isaya
            Yeremia
            Ezekieli
            Hosea
            Yoeli
            Amosi
            Obadia
            Yona
            Mika
            Nahumu
            Habakuki
            Sefania
            Hagai
            Zekaria
            Malaki
            Zaburi
            Ayubu
            Mithali
            Ruthi
            Wimbo_Ulio_Bora
            Mhubiri
            Maombolezo
            Esta
            Danieli
            Ezra
            Nehemia
            1_Mambo_ya_Nyakati
            2_Mambo_ya_Nyakati
    '''.strip().split()),
    tr=tuple(u'''
            Yaratılış
            Mısır'dan_Çıkış
            Levililer
            Çölde_Sayım
            Yasa'nın_Tekrar
            Yeşu
            Hakimler
            1_Samuel
            2_Samuel
            1_Krallar
            2_Krallar
            Yeşaya
            Yeremya
            Hezekiel
            Hoşea
            Yoel
            Amos
            Ovadya
            Yunus
            Mika
            Nahum
            Habakkuk
            Sefanya
            Hagay
            Zekeriya
            Malaki
            Mezmurlar
            Eyüp
            Süleyman'ın_Özdeyişleri
            Rut
            Ezgiler_Ezgisi
            Vaiz
            Ağıtlar
            Ester
            Daniel
            Ezra
            Nehemya
            1_Tarihler
            2_Tarihler
    '''.strip().split()),
    id=tuple(u'''
            Kejadian
            Keluaran
            Imamat
            Bilangan
            Ulangan
            Yosua
            Hakim-hakim
            1_Samuel
            2_Samuel
            1_Raja-raja
            2_Raja-raja
            Yesaya
            Yeremia
            Yehezkiel
            Hosea
            Yoel
            Amos
            Obaja
            Yunus
            Mikha
            Nahum
            Habakuk
            Zefanya
            Hagai
            Zakharia
            Maleakhi
            Mazmur
            Ayub
            Amsal
            Rut
            Kidung_Agung
            Pengkhutbah
            Ratapan
            Ester
            Daniel
            Ezra
            Nehemia
            1_Tawarikh
            2_Tawarikh
    '''.strip().split()),
    ar=tuple(u'''
            تكوين
            خروج
            لاويين
            عدد
            تثنية
            يشوع
            قضاة
            1_صموئيل
            2_صموئيل
            1_ملوك
            2_ملوك
            اشعياء
            ارميا
            حزقيال
            هوشع
            يوئيل
            عاموس
            عوبديا
            يونان
            ميخا
            ناحوم
            حبقوق
            صفنيا
            حجى
            زكريا
            ملاخي
            مزامير
            ايوب
            امثال
            راعوث
            نشيد_الانشاد
            جامعة
            مراثي
            استير
            دانيال
            عزرا
            نحميا
            1_اخبار
            2_اخبار
    '''.strip().split()),
    zh=tuple(u'''
            创世记
            出埃及记
            利未记
            民数记
            申命记
            约书亚记
            Judges
            撒母耳记上
            撒母耳记下
            列王纪上
            列王纪下
            以赛亚书
            耶利米书
            以西结书
            何西阿书
            约珥书
            阿摩司书
            俄巴底亚书
            约拿书
            弥迦书
            那鸿书
            哈巴谷书
            西番雅书
            哈该书
            撒迦利亚书
            玛拉基书
            诗篇
            以斯帖记
            箴言
            路得记
            雅歌
            传道书
            耶利米哀歌
            以斯帖记
            但以理书
            以斯拉记
            尼希米记
            历代志上
            历代志下
    '''.strip().split()),
    hi=tuple(u'''
            उत्पाति
            निर्गमन
            लैव्यव्यवस्थ
            गिनती
            व्यवस्थाविवरण
            यहोशू
            न्यायियों
            1_शमूएल
            2_शमूएल
            1_राजाओं
            2_राजाओं
            यशायाह
            यिर्मयाह
            यहेजकेल
            होशे
            योएल
            आमोस
            ओबधाह
            योना
            मीका
            नहूम
            हबक्कूक
            सपन्याह
            हाग्गै
            जकर्याह
            मलाकी
            भजन_संहिता
            अय्यूब
            नीतिबचन
            रुत
            श्रेष्ठगीत
            सभोपदेशक
            विलापगेत
            एस्तेर
            दानिय्यल
            एज्रा
            नहेम्याह
            1_इतिहास
            2_इतिहास
    '''.strip().split()),
    fa=tuple(u'''
            پيدايش
            خروج
            لاويان
            اعداد
            تثنيه
            يوشع
            داوران
            اول_سموئيل
            دوم_سموئيل
            اول_پادشاهان
            دوم_پادشاهان
            اشعیا
            اِرميا
            حزقیال
            هوشع
            يوئيل
            عاموس
            عوبديا
            يونس
            ميكاه
            ناحوم
            حبقوق
            صفنيا
            حجی
            زآريا
            ملاآی
            مزامير
            ايوب
            امثال
            روت
            غزل_غزلهای_سليمان
            جامعه
            مراثی_ارميا
            استر
            دانيال
            عزرا
            نحميا
            اول_تواريخ_ايام
            دوم_تواريخ
    '''.strip().split()),
    pt=tuple(u'''
            Gênesis
            Êxodo
            Levítico
            Números
            Deuteronômio
            Josué
            Juízes
            1_Samuel
            2_Samuel
            1_Reis
            2_Reis
            Isaías
            Jeremias
            Ezequiel
            Oséias
            Joel
            Amós
            Obadias
            Jonas
            Miquéias
            Naum
            Habacuque
            Sofonias
            Ageu
            Zacarias
            Malaquis
            Salmos
            Jó
            Provérbios
            Rute
            Cantares_de_Salomâo
            Eclesiastes
            Lamentações
            Ester
            Daniel
            Esdras
            Neemias
            1_Crônicas
            2_Crônicas
    '''.strip().split()),
    syc=tuple(u'''
            ܒܪܝܬܐ
            ܡܦܩܢܐ
            ܟܗܢ̈ܐ
            ܡܢܝܢܐ
            ܬܢܝܢ_ܢܡܘܣܐ
            ܝܫܘܥ_ܒܪܢܘܢ
            ܕܝܢ̈ܐ
            ܐ_ܫܡܘܐܝܠ
            ܒ_ܫܡܘܐܝܠ
            ܐ_ܡܠܟ̈ܐ
            ܒ_ܡܠܟ̈ܐ
            ܐܫܥܝܐ
            ܐܪܡܝܐ
            ܚܙܩܝܐܝܠ
            ܗܘܫܥ
            ܝܘܐܝܠ
            ܥܡܘܣ
            ܥܘܒܕܝܐ
            ܝܘܢܢ
            ܡܝܟ݂ܐ
            ܢܚܘܡ
            ܚܒ݂ܩܘܩ
            ܨܦܢܝܐ
            ܚܓܝ
            ܙܟ݂ܪܝܐ
            ܡܠܐܟ݂ܝ
            ܡܙܡܘܪ̈ܐ
            ܐܝܘܒ݂
            ܡܬܠ̈ܐ
            ܪܥܘܬ݂
            ܬܫܒܚܬ_ܬܫܒܚ̈ܬ݂ܐ
            ܩܘܗܠܬ
            ܐܘܠܝ̈ܬ݂ܐ
            ܐܣܬܝܪ
            ܕܢܝܐܝܠ
            ܥܙܪܐ
            ܢܚܡܝܐ
            ܐ_ܒܪܝܡܝܢ
            ܒ_ܒܪܝܡܝܢ
    '''.strip().split()),
    da=tuple(u'''
            1.Mosebog
            2.Mosebog
            3.Mosebog
            4.Mosebog
            5.Mosebog
            Josva
            Dommer
            1.Samuel
            2.Samuel
            1.Kongebog
            2.Kongebog
            Esajas
            Jeremias
            Ezekiel
            Hoseas
            Joel
            Amos
            Obadias
            Jonas
            Mika
            Nahum
            Habakkuk
            Sefanias
            Haggaj
            Zakarias
            Malakias
            Salmerne
            Job
            Ordsprogene
            Ruth
            Højsangen
            Prædikeren
            Klagesangene
            Ester
            Daniel
            Ezra
            Nehemias
            1.Krønikebog
            2.Krønikebog
    '''.strip().split()),
    am=tuple(u'''
            ኦሪት_ዘፍጥረት
            ኦሪት_ዘጸአት
            ኦሪት_ዘሌዋውያን
            ኦሪት_ዘኍልቍ
            ኦሪት_ዘዳግም
            መጽሐፈ_ኢያሱ_ወልደ_ነዌ
            መጽሐፈ_መሣፍንት
            መጽሐፈ_ሳሙኤል_ቀዳማዊ
            መጽሐፈ_ሳሙኤል_ካል
            መጽሐፈ_ነገሥት_ቀዳማዊ።
            መጽሐፈ_ነገሥት_ካልዕ።
            ትንቢተ_ኢሳይያስ
            ትንቢተ_ኤርምያስ
            ትንቢተ_ሕዝቅኤል
            ትንቢተ_ሆሴዕ
            ትንቢተ_ኢዮኤል
            ትንቢተ_አሞጽ
            ትንቢተ_አብድዩ
            ትንቢተ_ዮናስ
            ትንቢተ_ሚክያስ
            ትንቢተ_ናሆም
            ትንቢተ_ዕንባቆም
            ትንቢተ_ሶፎንያስ
            ትንቢተ_ሐጌ
            ትንቢተ_ዘካርያስ
            ትንቢተ_ሚልክያ
            መዝሙረ_ዳዊት
            መጽሐፈ_ኢዮብ።
            መጽሐፈ_ምሳሌ
            መጽሐፈ_ሩት
            መኃልየ_መኃልይ_ዘሰሎሞን
            መጽሐፈ_መክብብ
            ሰቆቃው_ኤርምያስ
            መጽሐፈ_አስቴር።
            ትንቢተ_ዳንኤል
            መጽሐፈ_ዕዝራ።
            መጽሐፈ_ነህምያ።
            መጽሐፈ_ዜና_መዋዕል_ቀዳማዊ።
            መጽሐፈ_ዜና_መዋዕል_ካልዕ።
    '''.strip().split()),
    bn=tuple(u'''
            আদিপুস্তক
            যাত্রাপুস্তক
            লেবীয়_পুস্তক
            গণনা_পুস্তক
            দ্বিতীয়_বিবরণ
            যোশুয়া
            বিচারকচরিত
            সামুয়েল_১
            সামুয়েল_২
            রাজাবলি_১
            রাজাবলি_২
            ইসাইয়া
            যেরেমিয়া
            এজেকিয়েল
            হোসেয়া
            যোয়েল
            আমোস
            ওবাদিয়া
            যোনা
            মিখা
            নাহুম
            হাবাকুক
            জেফানিয়া
            হগয়
            জাখারিয়া
            মালাখি
            সামসঙ্গীত
            যোব
            প্রবচন
            রুথ
            পরম_গীত
            উপদেশক
            বিলাপ_গাথা
            এস্থার
            দানিয়েল
            এজরা
            নেহেমিয়া
            বংশাবলি_১
            বংশাবলি_২
    '''.strip().split()),
    ja=tuple(u'''
            創世記
            出エジプト記
            レビ記
            民数記
            申命記
            ヨシュア記
            士師記
            サムエル記第一
            サムエル記第二
            列王記第一
            列王記第二
            イザヤ書
            エレミア書
            エゼキエル書
            ホセア書
            ヨエル書
            アモス書
            オバデア書
            ヨナ書
            ミカ書
            ナホム書
            ハバクク書
            ゼパニア書
            ハガイ書
            ゼカリア書
            マラキ書
            詩篇
            ヨブ記
            箴言
            ルツ記
            雅歌
            伝道者の書
            哀歌
            エステル記
            ダニエル書
            エズラ記
            ネヘミア記
            歴代誌第一
            歴代誌第二
    '''.strip().split()),
    pa=tuple(u'''
            ਉਤਪਤ
            ਕੂਚ
            ਲੇਵੀਆਂ_ਦੀ_ਪੋਥੀ
            ਗਿਣਤੀ
            ਬਿਵਸਥਾ_ਸਾਰ
            ਯਹੋਸ਼ੁਆ
            ਨਿਆਂਈਆਂ_ਦੀ_ਪੋਥੀ
            1_ਸਮੂਏਲ
            2_ਸਮੂਏਲ
            1_ਰਾਜਿਆਂ
            2_ਰਾਜਿਆਂ
            ਯਸਾਯਾਹ
            ਯਿਰਮਿਯਾਹ
            ਹਿਜ਼ਕੀਏਲ
            ਹੋਸ਼ੇਆ
            ਯੋਏਲ
            ਆਮੋਸ
            ਓਬਦਯਾਹ
            ਯੂਨਾਹ
            ਮੀਕਾਹ
            ਨਹੂਮ
            ਹਬਕੱੂਕ
            ਸਫ਼ਨਯਾਹ
            ਹੱਜਈ
            ਜ਼ਕਰਯਾਹ
            ਮਲਾਕੀ
            ਜ਼ਬੂਰ
            ਅੱਯੂਬ
            ਕਹਾਉਤਾਂ
            ਰੂਥ
            ਸਲੇਮਾਨ_ਦਾ_ਗੀਤ
            ਉਪਦੇਸ਼ਕ
            ਵਿਰਲਾਪ
            ਅਸਤਰ
            ਦਾਨੀਏਲ
            ਅਜ਼ਰਾ
            ਨਹਮਯਾਹ
            1_ਇਤਹਾਸ
            2_ਇਤਹਾਸ
    '''.strip().split()),
    ur=tuple(u'''
            پیدائش
            خروج
            احبار
            گنتی
            استثناء
            یشوع
            قضاة
            اوّل_سموئیل
            دوم_سموئیل
            اوّل_سلاطین
            دوم_سلاطین
            یسعیاہ
            یرمیاہ
            حزقی_ایل
            ہوسیع
            یوایل
            عاموس
            عبدیاہ
            یونس
            میکاہ
            نا_حُوم
            حبقّوق
            صفنیاہ
            حجيّ
            زکریاہ
            ملاکی
            زبُور
            ایّوب
            امثال
            روت
            غزل_الغزلات
            واعظ
            نوحہ
            ایستر
            دانیال
            عز_را
            نحمیاہ
            اوّل_تواریخ
            دوم_تو_اریخ
        '''.strip().split()),
    yo=tuple(u'''
            Genesisi
            Eksodu
            Lefitiku
            Numeri
            Deuteronomi
            Josua
            Awọn_Onidajọ
            Samueli_Kinni
            Samueli_Keji
            Awon_Ọba_Kinni
            Awon_Ọba_Keji
            Isaiah
            Jeremiah
            Esekieli
            Hosea
            Joeli
            Amọsi
            Obadiah
            Jonà
            Mika
            Nahumu
            Habakkuku
            Sefaniah
            Haggai
            Sekariah
            Malaki
            Psalmu
            Jobu
            Òwe
            Rutu
            Orin_Solomọni
            Oniwasu
            Ẹkún_Jeremiah
            Esteri
            Danieli
            Esra
            Nehemiah
            Kronika_Kinni
            Kronika_Keji
        '''.strip().split()),
),
'Greek': dict(
    la=tuple(u'''
            secundum_Matthæum
            secundum_Marcum
            secundum_Lucam
            secundum_Ioannem
            Actus
            ad_Romanos
            1_ad_Corinthios
            2_ad_Corinthios
            ad_Galatas
            ad_Ephesios
            ad_Philippenses
            ad_Colossenses
            1_ad_Thessalonicenses
            2_ad_Thessalonicenses
            1_ad_Timotheum
            2_ad_Timotheum
            ad_Titum
            ad_Philemonem
            ad_Hebræos
            Iacobi
            1_Petri
            2_Petri
            1_Ioannis
            2_Ioannis
            3_Ioannis
            Iudæ
            Apocalypsis
        '''.strip().split()),
    en=tuple(u'''
            Matthew
            Mark
            Luke
            John
            Acts
            Romans
            1_Corinthians
            2_Corinthians
            Galatians
            Ephesians
            Philippians
            Colossians
            1_Thessalonians
            2_Thessalonians
            1_Timothy
            2_Timothy
            Titus
            Philemon
            Hebrews
            James
            1_Peter
            2_Peter
            1_John
            2_John
            3_John
            Jude
            Revelation
        '''.strip().split()),
),
}
