```python
import unittest
from user_profile import UserProfile

class TestUserProfile(unittest.TestCase):
    def setUp(self):
        self.user_profile = UserProfile()

    def test_create_profile(self):
        self.user_profile.create_profile()
        self.assertIsNotNone(self.user_profile.interests)
        self.assertIsNotNone(self.user_profile.reading_habits)

    def test_get_user_interests(self):
        self.user_profile.get_user_interests()
        self.assertIsNotNone(self.user_profile.interests)

    def test_get_user_reading_habits(self):
        self.user_profile.get_user_reading_habits()
        self.assertIsNotNone(self.user_profile.reading_habits)

    def test_update_interests(self):
        initial_interests = self.user_profile.interests
        self.user_profile.update_interests(['new_interest'])
        self.assertNotEqual(initial_interests, self.user_profile.interests)

    def test_update_reading_habits(self):
        initial_habits = self.user_profile.reading_habits
        self.user_profile.update_reading_habits({'new_habit': 'value'})
        self.assertNotEqual(initial_habits, self.user_profile.reading_habits)

if __name__ == "__main__":
    unittest.main()
```
