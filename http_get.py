# Line one
# Line Two
#!/bin/env python
#encoding=utf-8
#coding=utf-8

import urllib
import httplib2
import re

#keyword = raw_input("input you search keyword: ")
#strInUrl = raw_input("input you URL: ")


def fOpenUrl(strUrl):
    http=httplib2.Http()
    response,content=http.request(strUrl,"GET")
    return content


#regx_results = re.compile(r"<li class=.results.>.*?<h2><a title=.(.*?). href=.*?<a onclick=.*?;. href=.(.*?).><i class=.*?href=.(.*?).><i.*?</i>",re.S)

#url="http://btku.me/q/"+keyword+"/"
url="http://www.dygang.com/"
#url2="http://www.dygang.com/ys/20150719/32461.htm"

regx_search = re.compile(r'<TD><a href="(.*?)" target=._blank. class="c2">(.*?)</a>',re.S)
regx_site = re.compile(r'<a href="(ed2k://.*?)">.*?</a></td>',re.S)


def fHtmlFilter(objRegx,strHtml):
    strres=objRegx.findall(strHtml)
    return strres


def fDownSite(str):
    html = fOpenUrl(str)
#    print html
    results = fHtmlFilter(regx_site,html)
    if len(results)>1:
        for indx in range(len(results)):   
            print "%s\n"% results[indx]
    elif len(results)  == 1:
        print "%s\n"% results
    




    
              
def fPrintHtml(str):
    for indx in str:
        print"#####################"
        for indy in range(len(indx)):
            #print "%s\n"% indx[indy]
            if indy == 0: 
                print "URL sites: %s\n"% indx[indy]
                fDownSite(indx[indy])  
            elif indy == 1:
                print "Movie name: %s\n"% indx[indy]




    
html = fOpenUrl(url)
results = fHtmlFilter(regx_search,html)
fPrintHtml(results)

#for indx in range(5):
#    url=url+str(indx)       
#    html = fOpenUrl(url)
#    results = fHtmlFilter(regx_results,html)
#    fPrintHtml(results)



