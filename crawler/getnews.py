import newspaper
from multiprocessing import Process
from elasticsearch import Elasticsearch
import datetime
import json
import time

es = Elasticsearch("http://ec2-52-90-108-15.compute-1.amazonaws.com:80/elasticsearch/");

def startnewspaper(url):
	while True: 
		paper = newspaper.build(url)
		print "Found ", len(paper.articles)," Articles for url " + url
		for article in paper.articles:
			article.download()
			article.parse()
			article.nlp()
			article_body = {"title":article.title , "text": article.text , "timestamp": datetime.datetime.now() , "authors" : article.authors , "url":article.url,"keywords":article.keywords,"summary":article.summary}
			res = es.index(index="article-index", doc_type="article", body=article_body)
			# article_id = res[u'_id']
			# article_body['timestamp'] = str(article_body['timestamp'])
			# with open('data/'+ article_id, 'w') as outfile:
			# 	json.dump(article_body, outfile)
		time.sleep(60);

if __name__ == '__main__':
	processes = list()
	f=open('newspaperlist.txt', 'r')
	for line in f:
		p = Process(target=startnewspaper, args=(line,))
		p.start()
		processes.append(p)
		time.sleep(15);
	for process in processes:
		process.join()

	
