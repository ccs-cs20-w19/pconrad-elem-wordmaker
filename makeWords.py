import pytest

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
   
