# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:15:07 2017

@author: charleskim
"""

def fileAndDict():
#   Prompt user for input file
    userInput = input("Enter a text file (include quotation marks).\n")
    infile = open(userInput, 'r')
    myList = []
    myDictionary = {}
    for line in infile.readlines():
        words = line.split(" ")
        for element in words:
            myList.append(element)
    first = myList[0]
    second = myList[1]
    
    i = 0
    valueList = []
    while i < len(myList)-2:
        key = myList[i] + " " + myList[i+1]
        wannabeTupe = (myList[i+2], 1)
        tupe = (wannabeTupe,)
#       If the key is in the dictionary's list of keys...
        if key in myDictionary.keys():
#           If there is a tuple for that key with the same third word...
            for tupes in valueList:
                if tupes[0] == myList[i+2]:
#                   Then increase the count for that third word
                    tupeIndex = valueList.index(tupes)
                    valueList.pop(tupeIndex)
                    newWannabeTupe = (myList[i+2], tupes[1] + 1)
                    newTupe = (newWannabeTupe,)
                    myDictionary[key] = valueList.append(newTupe)
                else:
                    valueList = []
                    myDictionary[key] = valueList.append(tupe)
#       If the key is NOT in the dictionary's list of keys...
        else:
            valueList = []
            valueList.append(tupe)
            myDictionary[key] = valueList
        i = i + 1
#    for values in myDictionary.values():
#        values = sorted(values, key = lambda t: (-1 * t[1], t[0].lower()))
    return myDictionary, first, second

def textGenerator():
#   Get the returned values from fileAndDict()
    theDictionary, firstWord, secondWord = fileAndDict()
    answerText = str(firstWord) + " " + str(secondWord) + " "
    wordsPrinted = 0
    while wordsPrinted != 50:
        nextWords = theDictionary.get(str(firstWord) + " " + str(secondWord))
#       If there is no appropriate word to be generated, stop
        if nextWords == None:
            return answerText
        else:
            answerText = answerText + str(nextWords[0][0])  + " "
#           If there is more that one tuple for this key, delete the use one
            if len(nextWords) > 1:     
                    tupleIndex = nextWords.index(nextWords[0])
                    nextWords.pop(tupleIndex)
                    theDictionary[firstWord + " " + secondWord] = nextWords
#           Update first and second words
            firstWord = secondWord
            secondWord = nextWords[0][0]
        wordsPrinted = wordsPrinted + 1
    print answerText
    return answerText

textGenerator()