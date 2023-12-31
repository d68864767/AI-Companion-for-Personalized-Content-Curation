```python
import unittest
from unittest.mock import patch
from user_profile import UserProfile
from content_recommendation import ContentRecommendation

class TestContentRecommendation(unittest.TestCase):
    def setUp(self):
        self.user_profile = UserProfile()
        self.user_profile.interests = ['AI', 'Machine Learning', 'Python']
        self.filtered_content = [
            {'title': 'AI in healthcare', 'link': 'https://example.com/ai-in-healthcare', 'summary': 'This article discusses the use of AI in healthcare.'},
            {'title': 'Introduction to Machine Learning', 'link': 'https://example.com/intro-to-ml', 'summary': 'This article is an introduction to machine learning.'},
            {'title': 'Advanced Python Programming', 'link': 'https://example.com/advanced-python', 'summary': 'This article covers advanced topics in Python programming.'}
        ]
        self.content_recommendation = ContentRecommendation(self.user_profile, self.filtered_content)

    def test_recommend_content(self):
        recommended_content = self.content_recommendation.recommend_content()
        self.assertEqual(len(recommended_content), min(5, len(self.filtered_content)))
        for content in recommended_content:
            self.assertIn(content, self.filtered_content)

    @patch('builtins.print')
    def test_update_user_profile(self, mock_print):
        user_feedback = 'I liked the article on AI in healthcare.'
        self.content_recommendation.update_user_profile(user_feedback)
        mock_print.assert_called_with(user_feedback)

if __name__ == '__main__':
    unittest.main()
```
