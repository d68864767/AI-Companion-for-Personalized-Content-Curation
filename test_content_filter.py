```python
import unittest
from unittest.mock import MagicMock
from user_profile import UserProfile
from content_filter import ContentFilter

class TestContentFilter(unittest.TestCase):
    def setUp(self):
        self.user_profile = UserProfile()
        self.user_profile.interests = ["AI", "Programming", "Technology"]
        self.filter = ContentFilter(self.user_profile)

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

        actual_filtered_content = self.filter.filter_content(all_content)
        self.assertEqual(actual_filtered_content, expected_filtered_content)

    def test_filter_by_reading_habits(self):
        self.filter.check_reading_habits = MagicMock(return_value=True)
        filtered_content = [
            {
                'title': 'AI is changing the world',
                'link': 'https://www.example.com/news/ai-is-changing-the-world',
                'summary': 'This is a summary of the article'
            }
        ]

        expected_final_content = [
            {
                'title': 'AI is changing the world',
                'link': 'https://www.example.com/news/ai-is-changing-the-world',
                'summary': 'This is a summary of the article'
            }
        ]

        actual_final_content = self.filter.filter_by_reading_habits(filtered_content)
        self.assertEqual(actual_final_content, expected_final_content)

if __name__ == '__main__':
    unittest.main()
```
