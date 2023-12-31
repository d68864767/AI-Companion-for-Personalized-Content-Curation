```python
import requests
from bs4 import BeautifulSoup

class ContentScraper:
    def __init__(self, user_profile):
        self.user_profile = user_profile
        self.sources = ["https://www.example.com/news", "https://www.example.com/blogs", "https://www.example.com/socialmedia"]

    def scrape_content(self):
        print("Scraping content...")
        all_content = []
        for source in self.sources:
            content = self.scrape_source(source)
            all_content.extend(content)
        return all_content

    def scrape_source(self, source):
        print(f"Scraping source: {source}")
        response = requests.get(source)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')
        content = []
        for article in articles:
            title = article.find('h2').text
            link = article.find('a')['href']
            summary = article.find('p').text
            content.append({
                'title': title,
                'link': link,
                'summary': summary
            })
        return content

    def filter_content(self, all_content):
        print("Filtering content...")
        filtered_content = []
        for content in all_content:
            for interest in self.user_profile.interests:
                if interest.lower() in content['title'].lower():
                    filtered_content.append(content)
                    break
        return filtered_content
```
