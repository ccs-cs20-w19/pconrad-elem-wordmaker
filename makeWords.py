import pytest
import twl
import tryPeriodic

def printAllWords():
  for word in twl.iterator():
    ways = wordToElems(word)
    if ways != set():
      print(ways)



def countWords():
 allWordCount = 0
 canMakeCount = 0
 cantMakeCount = 0
 for word in twl.iterator():
    allWordCount += 1 
    ways = wordToElems(word)
    if ways != set():
        canMakeCount += 1
    else:
        cantMakeCount +=1
 print("words",allWordCount,"can",canMakeCount,"can't",cantMakeCount)


def findLongestWordsSpellings():
 longestSoFar = 0
 for word in twl.iterator():
    ways = wordToElems(word)
    if ways != set():
        lengthOfThisWord = len(word)
        if lengthOfThisWord > longestSoFar:
            setOfLongest = [ ways ]
            longestSoFar = lengthOfThisWord
        elif lengthOfThisWord == longestSoFar:
            setOfLongest.append(ways)
 return setOfLongest


def findLongestWords():
 longestSoFar = 0
 for word in twl.iterator():
    ways = wordToElems(word)
    if ways != set():
        lengthOfThisWord = len(word)
        if lengthOfThisWord > longestSoFar:
            setOfLongest = [ word ]
            longestSoFar = lengthOfThisWord
        elif lengthOfThisWord == longestSoFar:
            setOfLongest.append(word)
 return setOfLongest

def findMostSpellings():
 longestSoFar = 0
 for word in twl.iterator():
    ways = wordToElems(word)
    if ways != set():
        sizeOfThisSet = len(ways)
        if sizeOfThisSet > longestSoFar:
            setOfLongest = [ ways ]
            longestSoFar = sizeOfThisSet
        elif sizeOfThisSet == longestSoFar:
            setOfLongest.append(ways)
 return setOfLongest
 
# From https://stackoverflow.com/questions/16891340/remove-a-prefix-from-a-string
def stripPrefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  

def wordToElems(word, elemlist=tryPeriodic.getSymbolList()):
    if word == '':
        return {''}
    word = word.lower()
    result = set()
    prefixes = wordToElemPrefixes(word,elemlist)
    
    for p in prefixes:
        # strip off the prefix, call this "restOfWord"
        restOfWord = stripPrefix(word,p.lower())
        # get the set of all the ways of making "restOfWord" with elements
        suffixes = wordToElems(restOfWord,elemlist)
        for s in suffixes:
            result.add( p + s)

        # add this prefix with all of those into my result set
    return result    

def wordToElemPrefixes(word,elemlist=tryPeriodic.getSymbolList()):
    word=word.lower()
    result = set()
    for e in elemlist:
        if word.startswith(e.lower()):
            result.add(e)
    return result

def makeWordsFromScrabbleDict(numElems):
    "numElems is how many elements to use at a time"
    elemList = tryPeriodic.getSymbolList()
    result = set() # empty set
    candidates = makeCandidateWords(elemList, numElems)
    for w in candidates:       
        if twl.check(w.lower()) :
            result.add(w)    
    return result

def makeWords(elemList,numElems,wordList):
    "numElems is how many elements to use at a time"

    result = set() # empty set
    candidates = makeCandidateWords(elemList, numElems)
    for w in candidates:
        if w.upper() in wordList:
            result.add(w)    
    return result

def makeCandidateWords(elemList,numElems):
    if numElems == 1:
        return elemList
    result = []
    words = makeCandidateWords(elemList, numElems-1)
    for c in elemList:
        for w in words:
            result.append(c+w)
    return result


def test_makeCandidateWords_2a():
   elemlist=["O","N","H","C"]
   expected=["OO","ON","OH","OC",
             "NO","NN","NH","NC",
             "HO","HN","HH","HC",
             "CO","CN","CH","CC"]
   assert makeCandidateWords(elemlist, 2)==expected

def test_makeCandidateWords_3():
   elemlist=["Li","P"]
   expected=["LiLiLi","LiLiP",
             "LiPLi","LiPP",
             "PLiLi","PLiP",
             "PPLi","PPP"]
   assert makeCandidateWords(elemlist, 3)==expected   

def allUpper(setOfStrings):
    result = set()
    for s in setOfStrings:
        result.add(s.upper())
    return result

def test_allUpper_1():
    assert(allUpper({"LiP","TiN"})=={"TIN","LIP"})

def test_makeWords_2a():
   elemlist=["O","N","H","C"]
   wordlist=["NO","ON","TO","AN"]
   expected={"NO","ON"}
   result= makeWords(elemlist, 2, wordlist)
   assert (allUpper(result)==expected)
   
def test_makeWords_3a():
   elemlist=["O","N","H","C"]
   wordlist=["CON","HON","OOH","ASH","LIP"]
   expected={"CON","HON","OOH"}
   result= makeWords(elemlist, 3, wordlist)
   assert allUpper(result)==expected
   

def test_makeWords_2b():
   elemlist=["Li","P","O","N","Ti","I"]
   wordlist=["LIP","ASH","CON","TIN","NIP","TIP","POP","PI","IN","ON"]
   expected={"LIP","TIN","TIP","PI","IN","ON"}
   assert allUpper(makeWords(elemlist, 2, wordlist))==expected
   
def test_makeWords_3b():
   elemlist=["Li","P","Ti","N","O"]
   wordlist=["LIP","ASH","CON","TIN","NIP","TIP","LION","POP"]
   expected={"POP","LION"}
   assert allUpper(makeWords(elemlist, 3, wordlist))==expected
   

def test_checkWordToElemPrefixes_cat():
   elemlist=["C","Ca","H","Li"]
   assert wordToElemPrefixes("cat",elemlist)=={"C","Ca"}

def test_checkWordToElemPrefixes_an():
   elemlist=["O","N","H","C","Li","Ca"]
   assert wordToElemPrefixes("an",elemlist)==set()

def test_checkWordToElemPrefixes_lip():
   elemlist=["Li","P","Ti","N","O"]
   assert wordToElemPrefixes("lip",elemlist)=={"Li"}

def test_wordToElems_lip():
    elemlist=["Li","P","Ti","N","O"]
    assert wordToElems("lip",elemlist)=={"LiP"}

def test_wordToElems_sin():
    elemlist=["Li","P","Ti","N","O","In","S","Si","I"]
    assert wordToElems("sin",elemlist)=={"SIN","SiN","SIn"}

    
def test_stripPrefix_lion():
    assert stripPrefix("lion","li")=="on"
