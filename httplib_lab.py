#!/bin/env python
#encoding=utf-8
#coding=utf-8

import urllib
import httplib2
import re

keyword = raw_input("input you search keyword: ")
regx_results = re.compile(r"<li class=.results.>.*?<h2><a title=.(.*?). href=.*?<a onclick=.*?;. href=.(.*?).><i class=.*?href=.(.*?).><i.*?</i>",re.S)
url="http://btku.me/q/"+keyword+"/"


def fOpenUrl(strUrl):
    http=httplib2.Http()
    response,content=http.request(url,"GET")
    return content


def fHtmlFilter(objRegx,strHtml):
    strres=objRegx.findall(strHtml)
    return strres

              
def fPrintHtml(str):
    for indx in str:
        print"#####################"
        for indy in range(len(indx)):
            print "%s\n"% indx[indy]

    
html = fOpenUrl(url)
results = fHtmlFilter(regx_results,html)
fPrintHtml(results)

for indx in range(5):
    url=url+str(indx)       
    html = fOpenUrl(url)
    results = fHtmlFilter(regx_results,html)
    fPrintHtml(results)



