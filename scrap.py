#!/usr/bin/ python3
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://medium.com/@nathancheng/the-cure-for-type-2-diabetes-is-known-but-few-are-aware-5dd3064328b6').text

soup = BeautifulSoup(source, 'lxml')


for article in soup.find_all('article'):
    
    title= article.find('p',{"id":"a800"}).get_text()
    print(title)
    print('\n\n')
    a= article.find('p',{"id":"efe6"}).get_text()
    print(a)
    print('\n\n')
    b= article.find('p',{"id":"0768"}).get_text()
    print(b)
    print('\n\n')
    c= article.find('p',{"id":"2ef6"}).get_text()
    print(c)
    print('\n\n')
    d= article.find('p',{"id":"02fe"}).get_text()
    print(d)
    print('\n\n')
    e= article.find('p',{"id":"1ad1"}).get_text()
    print(e)
    print('\n\n')
    f= article.find('p',{"id":"0102"}).get_text()
    print(f)
    print('\n\n')
    g= article.find('p',{"id":"f89b"}).get_text()
    print(g)
    print('\n\n')
    h= article.find('p',{"id":"fa8e"}).get_text()
    print(h)
    print('\n\n')
    i= article.find('p',{"id":"bc5b"}).get_text()
    print(i)
    print('\n\n')
    j= article.find('p',{"id":"a567"}).get_text()
    print(j)
    print('\n\n')
    k= article.find('p',{"id":"3371"}).get_text()
    print(k)
    print('\n\n')
    l= article.find('p',{"id":"7d66"}).get_text()
    print(l)
    print('\n\n')
    m= article.find('p',{"id":"6870"}).get_text()
    print(m)
    print('\n\n')
    n= article.find('p',{"id":"b057"}).get_text()
    print(n)
    print('\n\n')
    o= article.find('p',{"id":"f275"}).get_text()
    print(o)
    print('\n\n')
    p= article.find('p',{"id":"d489"}).get_text()
    print(p)
    print('\n\n')
    q= article.find('p',{"id":"3fe9"}).get_text()
    print(q)
    print('\n\n')
    r= article.find('p',{"id":"c501"}).get_text()
    print(r)
    print('\n\n')
    s= article.find('p',{"id":"c371"}).get_text()
    print(s)
    print('\n\n')
	

    

