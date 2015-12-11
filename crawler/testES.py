from elasticsearch import Elasticsearch
import datetime 
import newspaper
import json

es = Elasticsearch(["https://search-newsroom-yzzuz54qo6uc2ia7facyfaccty.us-east-1.es.amazonaws.com/"]);
# print es.info()
info = es.info()
print "Connected to ",info[u'cluster_name']
paper = newspaper.build("http://www.cnn.com")
print "Paper cnn built..."
article = paper.articles[0]
print "url ::",article.url
article.download()
article.parse()
article_body = {"title":article.title , "text": article.text , "timestamp": datetime.datetime.now() , "authors" : article.authors , "url":article.url}
res = es.index(index="article-index", doc_type="article", body=article_body)
article_id = res[u'_id']
article_body['timestamp'] = str(article_body['timestamp'])
with open('data/'+ article_id, 'w') as outfile:
    json.dump(article_body, outfile)
