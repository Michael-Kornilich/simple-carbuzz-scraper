# carbuzz scraper
from bs4 import BeautifulSoup
import requests
from datetime import datetime

res = requests.get('https://carbuzz.com/')

if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
else:
    quit(print(f'Invalid status code: {res.status_code}'))

print(f"As of {datetime.now().strftime('%A, %B %d  - %H:%M')}\n")

for item in soup.select(".sentinel-home-list .w-display-card-content.regular.article-block"):
    post_time_raw = item.find(class_="display-card-date")["datetime"]
    post_time = datetime.strptime(post_time_raw, "%Y-%m-%dT%H:%M:%SZ")

    news_title = item.find('a')['title']
    link = "https://carbuzz.com" + item.find('a')['href']

    print(f"{post_time.strftime('%A, %B %d - %H:%M')}\n"
          f"{news_title}\n"
          f"({link})", end='\n' * 2)
