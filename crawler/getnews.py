import newspaper
import time
from multiprocessing import Process
import MySQLdb
import datetime as dt

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="ppp1234",  # your password
                     db="newsroom")

cursor = db.cursor()

def write_to_db(article, s):
	article.download()
	article.parse()
	

	url=article.url
	title=article.title
	#print "title: "+title

	text =  article.text
	#print "text: "+text


	author = ""
	for a in article.authors:
		author=author + a.encode('utf-8') + ', '

	publish_date='2015-12-04'
	crawl_date=dt.datetime.today().strftime("%Y-%m-%d")
	source=s
	id = 0
	try:
		cursor.execute('''INSERT into articles(url, title, author, published_date, crawled_date, source) values (%s, %s, %s, %s, %s, %s)''', (url.encode('utf-8'), title.encode('utf-8'), author.encode('utf-8'), publish_date, crawl_date, source))
	

	
		db.commit()

		id = cursor.lastrowid
		write_to_file(id, text.encode('utf-8'))

		article.nlp()
		keywords = article.keywords
		for keyword in keywords:
			k = keyword.encode('utf-8')
			cursor.execute('''INSERT into keywords(id, word) values (%s, %s)''',(id,k))
			
	#print str(id)+" "+str(article.authors)

		db.commit()
		
		
	except Exception as e:
		print e

def write_to_file(id,text):
	name='articles/'+str(id)+'.txt'
	f= open(name,'w')
	f.write(text)


def startnewspaper(url,s):
	# Download all articles from the url
	#print "before for..."
	
	i = 0
	while True: 
		paper = newspaper.build(url)
		#print i
		i = i+1

		print "Found ", len(paper.articles)," Articles for url " + url

		for article in paper.articles:
			write_to_db(article, s)
			#article.download();
			#article.parse();
			#print article.text
			#print "Here"
			#print article.url 
			#print article.authors

			# todo: Save article in DB, retrieve id and save text  with filenames id in crawler/files
			#print(article.url)
			# recrawl every 60 seconds
		

		time.sleep(15);
			#threading.Timer(60, startnewspaper).start()

#def storeToDB(article):


if __name__ == '__main__':
	# todo: read from the newspaperlist.txt file and create new process for each
	processes = list()
	#for i in range(0,10):
	f=open('newspaperlist.txt', 'r')
	for line in f:
		data = line.split(",")
		url=data[1]
		source=data[0]
		p = Process(target=startnewspaper, args=(url,source,))
		p.start()
		processes.append(p)
		#p.join()

	for process in processes:
		process.join()

	db.close()
