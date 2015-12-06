import newspaper
from multiprocessing import Process

def startnewspaper(url):
	# Download all articles from the url
	paper = newspaper.build(url)
	for article in paper:
		article.download();
		article.parse();

		# todo: Save article in DB, retrieve id and save text  with filenames id in crawler/files
		print(article.url)
		# recrawl every 60 seconds
		threading.Timer(60, startnewspaper).start()

if __name__ == '__main__':
	# todo: read from the newspaperlist.txt file and create new process for each
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()