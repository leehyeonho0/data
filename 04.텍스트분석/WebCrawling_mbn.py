# 비주얼스튜디오로 코드 저장 (WebCrawling_mbn.py)
import os, re, csv
import requests # URL 주소에 있는 내용을 요청할 때 사용하는 모듈
import urllib.request as ur  # 웹에서 얻은 데이터를 다루는 파이썬 패키지
from bs4 import BeautifulSoup as bs

# 기사 제목, 본문, 하이퍼링크 파일로 저장하기
url = 'https://www.mbn.co.kr/news/date/'
soup = bs(ur.urlopen(url).read(), 'html.parser')

f = open('article_mbn.txt','w')
for i in soup.find_all('dt', {"class":"tit"}):
    try:
        f.write('='*60 + '\n')
        f.write(' 기사 제목 : ')
        f.write(i.text + '\n')  # 기사 제목
        
        f.write(' URL : ')
        f.write('http:' + i.find_all('a')[0].get('href') + '\n')  # URL링크
    
        soup2 = bs(ur.urlopen('http:' + i.find_all('a')[0].get('href')).read(), 'html.parser')
        for j in soup2.find_all('div', {"class":"detail"}):
            f.write('\n' + ' 기사 본문 : ')
            f.write(j.text + '\n')   # 기사 본문

    except:
        pass
f.close()