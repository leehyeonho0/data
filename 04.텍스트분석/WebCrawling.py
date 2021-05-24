import os, re, csv
import requests # URL 주소에 있는 내용을 요청할 때 사용하는 모듈
import urllib.request as ur  # 웹에서 얻은 데이터를 다루는 파이썬 패키지
from bs4 import BeautifulSoup as bs

# 기사 제목, 본문, 하이퍼링크 파일로 저장하기
url = 'https://news.daum.net/'
soup = bs(ur.urlopen(url).read(), 'html.parser')

f = open('article_total.txt','w')

for i in soup.find_all('div', {"class" : "item_issue"}):
    try:
        f.write(i.text + '\n')  # 기사 제목
        f.write(i.find_all('a')[0].get('href') + '\n')  # 기사 URL링크
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
        for j in soup2.find_all('p'):
            f.write(j.text)   # 기사 본문
    except:
        pass

f.close()