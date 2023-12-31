```python
class ContentFilter:
    def __init__(self, user_profile):
        self.user_profile = user_profile

    def filter_content(self, all_content):
        print("Filtering content...")
        filtered_content = []
        for content in all_content:
            for interest in self.user_profile.interests:
                if interest.lower() in content['title'].lower():
                    filtered_content.append(content)
                    break
        return filtered_content

    def filter_by_reading_habits(self, filtered_content):
        print("Filtering content by reading habits...")
        final_content = []
        for content in filtered_content:
            if self.check_reading_habits(content):
                final_content.append(content)
        return final_content

    def check_reading_habits(self, content):
        # This is a placeholder function. You need to implement the logic to check the content against the user's reading habits.
        # For example, if the user prefers short articles, you could check the length of the content['summary'] and decide whether to include the content based on that.
        # You could also check the content['title'] or content['link'] against the user's reading habits.
        # This function should return True if the content matches the user's reading habits, and False otherwise.
        return True
```
