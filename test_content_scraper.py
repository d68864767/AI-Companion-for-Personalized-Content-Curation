```python
import unittest
from unittest.mock import patch, Mock
from user_profile import UserProfile
from content_scraper import ContentScraper

class TestContentScraper(unittest.TestCase):
    def setUp(self):
        self.user_profile = UserProfile("John Doe", ["AI", "Programming", "Technology"])
        self.scraper = ContentScraper(self.user_profile)

    @patch('requests.get')
    def test_scrape_source(self, mock_get):
        mock_response = Mock()
        mock_response.text = """
        <html>
            <body>
                <article>
                    <h2>AI is changing the world</h2>
                    <a href="https://www.example.com/news/ai-is-changing-the-world">Read more</a>
                    <p>This is a summary of the article</p>
                </article>
            </body>
        </html>
        """
        mock_get.return_value = mock_response

        expected_content = [{
            'title': 'AI is changing the world',
            'link': 'https://www.example.com/news/ai-is-changing-the-world',
            'summary': 'This is a summary of the article'
        }]

        actual_content = self.scraper.scrape_source("https://www.example.com/news")
        self.assertEqual(actual_content, expected_content)

    def test_filter_content(self):
        all_content = [
            {
                'title': 'AI is changing the world',
                'link': 'https://www.example.com/news/ai-is-changing-the-world',
                'summary': 'This is a summary of the article'
            },
            {
                'title': 'Cooking tips for beginners',
                'link': 'https://www.example.com/blogs/cooking-tips-for-beginners',
                'summary': 'This is a summary of the blog post'
            }
        ]

        expected_filtered_content = [
            {
                'title': 'AI is changing the world',
                'link': 'https://www.example.com/news/ai-is-changing-the-world',
                'summary': 'This is a summary of the article'
            }
        ]

        actual_filtered_content = self.scraper.filter_content(all_content)
        self.assertEqual(actual_filtered_content, expected_filtered_content)

if __name__ == '__main__':
    unittest.main()
```
