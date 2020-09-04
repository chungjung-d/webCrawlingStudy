from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
print('검색할 키워드를 입력하세요')
plusUrl = input('')

url =baseUrl + quote_plus(plusUrl)

#크롬을 제어하는데 사용된다
driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

r = soup.select('.r')                   #select는 css에서 가져온다
print(r)

for i in r:
    print(i.select(''))

a= cececececee