import solr

# create a connection to a solr server
s = solr.SolrConnection('http://ec2-54-209-22-205.compute-1.amazonaws.com:8983/solr/')
dir(s)
# add a document to the index
s.add(id=1, title='Lucene in Action', author=['Erik Hatcher', 'Piyush Jadhav'])
s.commit()
