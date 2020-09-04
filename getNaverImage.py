from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os

base_img_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

print('검색어를 입력하시오')
search_img_url = input()

img_url = base_img_url+ quote_plus(search_img_url)


html = urlopen(img_url).read()
soup = BeautifulSoup(html,'html.parser')
img = soup.find_all(class_='_img')

path = './'+search_img_url+'/'
os.mkdir(path)

n=1
for i in img:
    imgDownUrl = i['data-source']
    with urlopen(imgDownUrl) as f:
        with open('./'+search_img_url+'/'+search_img_url+str(n)+'.jpg','wb') as h:
            image = f.read()
            h.write(image)

    n=n+1

print('다운로드 완료 ')


