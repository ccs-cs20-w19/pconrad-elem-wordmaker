#!/usr/bin/env python3

import json
import pprint


with open('PeriodicTableJSON.json') as json_data:
  pt = json.load(json_data)

symbolList = []
for element in pt['elements']:
  symbolList.append(element['symbol'])
  if (len(symbolList)%10==0):
    print(symbolList)

   
   

