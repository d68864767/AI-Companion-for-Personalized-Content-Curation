```python
class UserProfile:
    def __init__(self):
        self.interests = []
        self.reading_habits = {}

    def create_profile(self):
        print("Creating a new user profile...")
        self.get_user_interests()
        self.get_user_reading_habits()

    def get_user_interests(self):
        print("Please enter your interests (separated by commas): ")
        user_input = input()
        self.interests = [interest.strip() for interest in user_input.split(",")]

    def get_user_reading_habits(self):
        print("Please enter your reading habits (e.g., preferred reading time, favorite content types, etc.): ")
        user_input = input()
        reading_habits = [habit.strip() for habit in user_input.split(",")]
        for habit in reading_habits:
            key, value = habit.split(":")
            self.reading_habits[key.strip()] = value.strip()

    def update_interests(self, new_interests):
        self.interests.extend(new_interests)

    def update_reading_habits(self, new_habits):
        self.reading_habits.update(new_habits)
```
