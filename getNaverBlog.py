import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

base_url ="https://search.naver.com/search.naver?where=post&sm=tab_jum&query="
search_url = input('검색어를 입력하시오')
url = base_url + (urllib).parse.quote_plus(search_url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

title = soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print('')


