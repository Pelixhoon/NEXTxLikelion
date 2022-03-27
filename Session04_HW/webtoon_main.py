import requests
from bs4 import BeautifulSoup
from webtoon import extract_info
import csv

file = open('webtoon.csv', mode='w', newline='')
writer = csv.writer(file) 
writer.writerow(["title","artist","rating"])

final_result = []
# 웹툰 제목, 작가 이름, 평점 정보 입력
WEBTOON_URL = 'https://comic.naver.com/webtoon/weekdayList?week=sat'
webtoon_html = requests.get(WEBTOON_URL)
webtoon_soup = BeautifulSoup(webtoon_html.text, "html.parser")

webtoon_list_box= webtoon_soup.find("ul", {"class":"img_list"})
webtoon_list = webtoon_list_box.find_all("li")

final_result += extract_info(webtoon_list)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['artist'])
    row.append(result['rating'])
    writer.writerow(row)
print(final_result)

