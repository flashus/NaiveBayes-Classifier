'''Now given a mail, split it in terms of spaces  ,  then ,  add up the log probability of each .  Multiply it with the spam probability  . Do the same thing for non-spam 
   Whichever is higher  wins .  Lets start
'''
import sys,os
from math import *

def makeDict(f):
	temp = {}
	data = open(f,'r')
	for line in data:
		prob = line.split(" ")
		temp[prob[0]] = prob[1]
	return temp
def predict(basepath,f,dictionary):
	toClassify = open(os.path.join(basepath,f),'r')
	for line in toClassify:
		words = line.split(" ")
		#print 'words are',words
		spamP = 0
		nonspamP = 0
		for w in words:
			try:
				if(w in dictionary):
					spamP = spamP + float(spamProbs[w].strip("\n"))
			except:
				pass
				
			try:
				if(w in dictionary):
					nonspamP = nonspamP + float(nonspamProbs[w].strip("\n"))
			except:
				pass
				
	totalSpamP = spamP + log ( 0.5 )
	totalnonSpamP = nonspamP + log ( 0.5 )
	#print 'TOtal spam and non-spam probs are ',totalSpamP,totalnonSpamP
	if(totalSpamP > totalnonSpamP):
		return True
	else:
		return False

spamProbs = makeDict(sys.argv[1]) #Pass the spam log probs here 
nonspamProbs = makeDict(sys.argv[2]) #Pass the non-spam log probs here
dictionaryWords = makeDict(sys.argv[5]) #Pass the dictionary 2500 words here
#print spamProbs
spamCount = 0
nonspamCount = 0
print 'No of files in spam is',len(os.listdir(sys.argv[3]))
for f in os.listdir(sys.argv[3]):
	
	if(predict(sys.argv[3],f,dictionaryWords)):
		spamCount = spamCount + 1
	else:
		nonspamCount = nonspamCount + 1
print 'No. of spam in ',sys.argv[3],' is ',str(spamCount),' no. of non-spam',str(nonspamCount)
print 'No of files in non-spam is',len(os.listdir(sys.argv[4]))
spamCount = 0 
nonspamCount =0
for f in os.listdir(sys.argv[4]):
	
	if(predict(sys.argv[4],f,dictionaryWords)):
		spamCount = spamCount + 1
	else:
		nonspamCount = nonspamCount + 1
print 'No. of spam in ',sys.argv[4],' is ',spamCount,' no. of non-spam',nonspamCount

