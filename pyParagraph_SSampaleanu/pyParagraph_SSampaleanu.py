# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:01:29 2018

@author: Stef
"""
words = []
    #   stores each word's length as element of list
sentences = []
    #   stores each sentence's length as element of list
    
pyPar = open('pyParagraphTest.txt','r')
paragraph = pyPar.read()
print("Here is the passage we'll analyze:")
print('"' + paragraph + '"')

for i in range(0,len(paragraph)):
    
    if paragraph[i] == " ":
            # if char is a space
        words.append(wordLength)
        wordLength = 0
        sentenceLength = sentenceLength + 1
        
    elif (paragraph[i] == "." or paragraph[i] == "?" or paragraph[i] == "!"):
            # if char is ending punctuation
        sentences.append(sentenceLength)
        sentenceLength = 0
        if i == len(paragraph)-1:
            words.append(wordLength)
            
    elif (paragraph[i] != "-" and paragraph[i] != "'" and paragraph[i] != '"'):
            # if char is a letter 
        wordLength = wordLength + 1
        
wordCount = len(words)
sentCount = len(sentences)

print("--------------------------------")
print("Paragraph Analysis")
print("--------------------------------")        
print("Approximate number of words: " + str(wordCount))
print("Approximate number of sentences: " + str(sentCount))
print("Average word length: " + str((sum(words))/wordCount) + " characters")
print("Average sentence length: " + str(wordCount/sentCount) + " words")
