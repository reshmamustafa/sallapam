def search(indexDir, kwds):
    '''Simple Search
    Input paramenters:
        1. indexDir: directory name of the index
        2. kwds: query string for this simple search
    display_verse(): procedure to display the specified bible verse 
    '''
    lucene.initVM()
    # 1. open the index
    analyzer = StandardAnalyzer(Version.LUCENE_35)
    index = SimpleFSDirectory(File(indexDir))
    reader = IndexReader.open(index)
    n_docs = reader.numDocs()

    # 2. parse the query string
    queryparser = QueryParser(Version.LUCENE_35, "Text", analyzer)
    query = queryparser.parse(kwds)

    # 3. search the index 
    searcher = IndexSearcher(reader)
    hits = searcher.search(query, n_docs).scoreDocs

    # 4. display results
    for i, hit in enumerate(hits):
        doc = searcher.doc(hit.doc)
        book = doc.getField('Book').stringValue()
        chapter = doc.getField('Chapter').stringValue()
        verse = doc.getField('Verse').stringValue()
        display_verse(book, int(chapter), int(verse))

    # 5. close resources
    searcher.close()
search('/home/reshma/Desktop/Luc_index', )