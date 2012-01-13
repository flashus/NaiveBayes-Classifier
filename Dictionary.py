#This script reads all files in all directories of the folder taken from the openClassroom site and generates the dictionary, which we can then store in a file 
folders = ["spam-train","spam-test","nonspam-train","nonspam-test"]
import os,sys
#We need a dictionary to store word occurences. What we can do is create a default dict and then update the frequencies. Write it all into a file all at once. 
from collections import * 
import operator
dictionary = defaultdict(int)
listWords = []
fdict = open(sys.argv[2],'w') #File to write all the entries in the dictionary 
for root,dirnames,filenames in os.walk(sys.argv[1]):
	for d in dirnames: #For each directory 
		print 'In directory',d
		for f in os.listdir(d):
			data = open ( os.path.join(sys.argv[1],d,f),'r')
			for line in data:
				words = line.split(" ")#Split words on space 
				for w in words:
					dictionary[w] += 1
count = 0

dictionary = OrderedDict(sorted(dictionary.items(),key = lambda t: t[1]))
#print dictionary
for k in dictionary.keys():
	count = count+1

	fdict.write(k+" "+str(dictionary[k])+"\n")

	#fdict.write(k +" "+str(dictionary[k])+"\n")
	
print 'Number of items in the dict',count
print 'Len of list words is ',len(listWords)

