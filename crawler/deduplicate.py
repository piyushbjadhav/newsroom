with open('newspaperlist.txt', 'r') as f:
	newspapers = [line.strip() for line in f]
print "Reduced from ",len(newspapers), " to"
newspapers = list(set(newspapers))
print len(newspapers)
with open ('updatedlist.txt','w') as f:
	for url in newspapers:
		f.write(url+'\n')