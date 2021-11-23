#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np
import requests
import xml.etree.ElementTree as ET

print('Hello python')

print(sys.argv[0])
print("====================")
#url >> text >> xml >> dict
xml_url = 'https://www.w3schools.com/xml/cd_catalog.xml'

#read from url ->  text
print(requests.get(xml_url)) #if sucess, <Response [200]> 
print(requests.get(xml_url).text) #content of xml 

#read text to xml
xmlTree = ET.fromstring(requests.get(xml_url).text) #CATALOG element
print(xmlTree)

list_dict = []
for cd in xmlTree:
    print("%s - [%s]" % (cd.find('TITLE').text, cd.find('ARTIST').text))
    list_dict.append({
        'title':cd.find('TITLE').text,
        'artist':cd.find('ARTIST').text,
        'country':cd.find('COUNTRY').text,
        'company':cd.find('COMPANY').text,
        'price':cd.find('PRICE').text,
        'year':cd.find('YEAR').text,
        })
#print(list_dict)
df = pd.DataFrame(list_dict)
print(df)
