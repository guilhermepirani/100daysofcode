import requests
from bs4 import BeautifulSoup


response =  requests.get('https://news.ycombinator.com/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# Scraping first article
article_tag = soup.find(name='a', class_='storylink')
article_text = article_tag.getText()
article_link = article_tag.get('href')
article_upvote = soup.find(name='span', class_='score').getText()

# print(article_text)
# print(article_link)
# print(article_upvote)

# Scraping All articles on page
articles = soup.find_all(name='a', class_='storylink')
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get('href'))

# Transforming upvotes from 'x points' to int(x)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

# print(article_texts)
# print(article_links)
print(article_upvotes)

# Getting highest upvoted article, may happen that an article doesn't have a score
i = article_upvotes.index(max(article_upvotes)) + (len(articles) - len(article_upvotes))
print(i)

print(article_texts[i])
print(article_links[i])

