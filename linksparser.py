#!/usr/bin/env python3
from lxml import html
import requests
import re

domains = set()
links = set()

'''
page = requests.get('http://nivanthaka.com')
tree = html.fromstring(page.content)

#print(page)

links = tree.xpath('//a/@href')
link_text = tree.xpath('//a/text()')

print(re.findall(r'http[s]*://[\w.-]+\.[a-z\.]+', 'http://www.test123.com.au/test.php'))


domains = set()

for link in tree.xpath('//a/@href'):
    #print(link)
    #print(re.findall(r'http[s]*://[a-z0-9]*[.]+[a-z]+', link))
    domain = re.findall(r'http[s]*://[\w.-]+\.[a-z\.]+', link)
    #domains.add(re.findall(r'http[s]*://[\w.-]+\.[a-z\.]+', link));
    if len(domain) > 0:
        #print(domain[0])
        domains.add(domain[0])
    
print(domains)
'''
def parsePage(link):
    global domains, links
    
    page = requests.get(link)
    tree = html.fromstring(page.content)
    
    for link in tree.xpath('//a/@href'):
        valid_link = re.findall(r'http[s]*://\S+', link)
        if len(valid_link) > 0:
            links.add(valid_link[0])
        domain = re.findall(r'http[s]*://[\w.-]+\.[a-z\.]+', link)
        if len(domain) > 0:
            domains.add(domain[0])
    
    
def printList():
    print("=================== Links ===================")
    for link in links:
        print(link) 
    print("=============================================")
    print("================== Domains ==================")
    for domain in domains:
        print(domain)
    print("=============================================")

parsePage('http://nivanthaka.com')

#print(links)
#print(domains)
printList()