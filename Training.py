#This is for training.     Calculate all probabilities and store them in a vector. Better to store it in a file  for easier access 
from __future__ import division
import sys,os
''' 
1. The spam and non-spam is already 50%  . So they by default are 0.5
2. Now we need to calculate probability of each word    , in spam and non-spam separately
  2.1  we can make two dictionaries, defaultdicts basically,  for spam and non-spam 
  2.2 When time comes to calculate probabilities, we just need to substitute values
'''
from collections import *
from math import *

spamDict = defaultdict(int)
nonspamDict = defaultdict(int)
spamFolders = ["spam-train"]
nonspamFolders = ["nonspam-train"]
path = sys.argv[1] #Base path
spamVector = open(sys.argv[2],'w') #WRite all spam values into this 
nonspamVector = open(sys.argv[3],'w') #Non-spam values

#Go through all files in spam and  iteratively add values
spamSize = 0
nonspamSize = 0
vocabSize = 2500

for f in os.listdir(os.path.join(path,spamFolders[0])):
	data = open(os.path.join(path,spamFolders[0],f),'r')

	for line in data:
		words = line.split(" ")
		spamSize = spamSize + len(words)
		for w in words:
			spamDict[w]+=1

for f in os.listdir(os.path.join(path,nonspamFolders[0])):
	data = open(os.path.join(path,nonspamFolders[0],f),'r')
	for line in data:
		words = line.split(" ")
		nonspamSize = nonspamSize + len(words)
		for w in words:
			nonspamDict[w]+=1
logProbspam = {}
logProbnonSpam = {} #This is to store the log probabilities
spamDenominator = spamSize + vocabSize
nonspamDenominator = nonspamSize + vocabSize
for k in spamDict.keys():
	#Need to calculate P(x | y = 1)

	numerator =  spamDict[k] + 1  # Frequency
	print 'Word',k,' frequency',spamDict[k]
	#denominator = spamSize + vocabSize
	p = log((numerator)/spamDenominator)
	logProbspam[k] = p
for k in nonspamDict.keys():
	numerator = nonspamDict[k] + 1 #frequency
	#denominator = nonspamSize + vocabSize
	p = log((numerator)/nonspamDenominator)
	logProbnonSpam[k] = p

for k in logProbnonSpam.keys():
	nonspamVector.write(k+" "+str(logProbnonSpam[k])+"\n")
for k in logProbspam.keys():
	spamVector.write(k+" "+str(logProbspam[k])+"\n")
