def make_index():
    '''Make index from data source -- bible
    Some global variables used:
        bible: a dictionary that stores all bible verses
        OTbooks: a list of books in old testament 
        NTbooks: a list of books in new testament
        chapsInBook: a list of number of chapters in each book 
    '''
    lucene.initVM()
    path = raw_input("Path for index: ")
    # 1. create an index
    index_path = File(path)
    analyzer = StandardAnalyzer(Version.LUCENE_35)
    index = SimpleFSDirectory(index_path)
    config = IndexWriterConfig(Version.LUCENE_35, analyzer)
    writer = IndexWriter(index, config)

    # 2 construct documents and fill the index
    for book in bible.keys():
        if book in OTbooks:
            testament = "Old"
        else:
            testament = "New"
        for chapter in xrange(1, chapsInBook[book]+1):
            for verse in xrange(1, len(bible[book][chapter])+1):
                verse_text = bible[book][chapter][verse]
                doc = Document()
                doc.add(Field("Text", verse_text, Field.Store.NO, Field.Index.ANALYZED))
                doc.add(Field("Testament", testament, Field.Store.YES, Field.Index.ANALYZED))
                doc.add(Field("Book", book, Field.Store.YES, Field.Index.ANALYZED))
                doc.add(Field("Chapter", str(chapter), Field.Store.YES, Field.Index.ANALYZED))
                doc.add(Field("Verse", str(verse), Field.Store.YES, Field.Index.ANALYZED))
                writer.addDocument(doc)

    # 3. close resources
    writer.close()
    index.close()
