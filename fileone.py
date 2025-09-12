# competitor_name = input('Enter Competitor name')
# c_url = f'https://{competitor_name}.com'
# print ('Competitor url: ' + c_url)
#orgtext = input("Enter original text")
#rword = input ("enter the part of text to be replaced")
#replacement = input ("enter the replacement text")

#if rword in orgtext:
#    print ("replacement can be done")
#else:
#    print (" replacement cant be done")    
#newtext = orgtext.replace(rword,replacement)
#print (newtext)
import lxml.etree
import pandas as pd
import requests
import lxml
import html5lib as hd
from bs4 import BeautifulSoup
import csv


listurls = []
listedurlcont = []
sitemapxml = requests.get("https://www.manageengine.com/network-monitoring/sitemap.xml")
sitemaptree = lxml.etree.fromstring (sitemapxml.content)
listurls = sitemaptree.xpath (f"//ns:loc[contains(text(), '{"manageengine.com/network-monitoring/help/"}')]/text()", namespaces={"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"})
print ('found: ', len(listurls), ' urls')
#print ('focusing on: ', listurls[2])
for url in listurls:
    if (requests.get(url).status_code!=200):
        print ('not 200:', url, "status: ",requests.get(url).status_code)
    else:
        webpagecontent = requests.get(url).content
        soup = BeautifulSoup (webpagecontent, "html.parser")
        for tag in soup.find_all('p'):
            #print (tag.text)
            listedurlcont.append (tag.text)

#with open ('/Users/vignesh-20727/Desktop/extractedcontent.csv', 'w', newline = "") as csvfile:
#    csv_writer = csv.writer(csvfile)
#    csv_writer.writerows(listedurlcont)
#print ("final content urls size: ", len(listedurlcont) )








#print(webpagecontent.content)


#print ("here are the final urls \n", listurls)
#addmore = 'Y'
#while (addmore != 'N'):
    #n = int(input ("enter a number"))
    #listn.append (n)
    #addmore = input ("Do you want to add more to list?")
#print ("final list: ", listn)

