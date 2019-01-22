#!/usr/bin/env python3

import json
import pprint
import pytest

def getSymbolList():
    with open('PeriodicTableJSON.json') as json_data:
      pt = json.load(json_data)

    symbolList = []
    for element in pt['elements']:
      symbolList.append(element['symbol'])

    return symbolList

def test_getSymbolList_len():
   result = getSymbolList()
   assert len(result)==119

def test_getSymbolList_H():
   result = getSymbolList()
   assert "H" in result
   
def test_getSymbolList_Li():
   result = getSymbolList()
   assert "Li" in result
      
   

    
   
   

