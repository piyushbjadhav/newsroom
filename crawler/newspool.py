import newspaper
from multiprocessing import Pool
from elasticsearch import Elasticsearch
import datetime
import json
import time

es = Elasticsearch("http://ec2-52-90-108-15.compute-1.amazonaws.com:80/elasticsearch/");

def startnewspaper(url):
	print url
	try:
		paper = newspaper.build(url,memoize_articles=False)
		print "Found ", len(paper.articles)," Articles for url " + url
		for article in paper.articles:
			article.download()
			article.parse()
			article.nlp()
			# article_body = {"title":article.title , "text": article.text , "timestamp": datetime.datetime.now() , "authors" : article.authors , "url":article.url,"keywords":article.keywords,"summary":article.summary}
			# res = es.index(index="article-index", doc_type="article", body=article_body)
	except Exception as e:
		print "caught Exception Moving on ...";

if __name__ == '__main__':
	p = Pool(32)
	with open('newspaperlist.txt', 'r') as f:
		newspapers = [line.strip() for line in f]
	while True:
		p.map(startnewspaper,newspapers)