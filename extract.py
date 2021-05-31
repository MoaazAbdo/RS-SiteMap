from sys import path
from xml.dom import minidom
import os, shutil, glob
import requests
import gzip

inputData = input("Please Enter The Path Of SiteMap XML: ")

mydoc = minidom.parse("sitemap.xml")
items = mydoc.getElementsByTagName('loc')

inputList = []
for i in range(len(items)):
    data = items[i].firstChild.data
    if "uk-detail" in data:
        inputList.append(data)

outputDir = inputData.replace(".xml", "")
"""
if os.path.exists(outputDir) == False:
    os.mkdir(outputDir)
else:
    shutil.rmtree(outputDir)
    os.mkdir(outputDir)
"""

for iter in range(len(inputList)):
    #r = requests.get(inputList[iter], allow_redirects=True)
    #open(outputDir+"\\"+inputList[iter].replace("https://uk.rs-online.com/",""), 'wb').write(r.content)
    print(iter)    

xmls = os.listdir(outputDir)

f = open('data.txt', 'a')

for x in range(len(xmls)):
    print(outputDir+"\\"+xmls[x])
    input = gzip.open(outputDir+"\\"+xmls[x], 'r')
    mydoc = minidom.parse(input)
    items = mydoc.getElementsByTagName('xhtml:link')
    for iter2 in range(len(items)):
        print(iter2+1, "=", items[iter2].attributes['href'].value+"\n")
        f.writelines(items[iter2].attributes['href'].value+"\n")

f.close()

"""
input = gzip.open("D:\\xmlExtraction\\sitemap\\uk-detail0.xml.gz", 'r')
mydoc = minidom.parse(input)
items = mydoc.getElementsByTagName('xhtml:link')
for i in range(len(items)):
    print(i+1, "=", items[i].attributes['href'].value)


"""