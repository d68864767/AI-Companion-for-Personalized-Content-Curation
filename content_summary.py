```python
from gensim.summarize import summarize

class ContentSummary:
    def __init__(self, content):
        self.content = content

    def generate_summary(self):
        print("Generating content summary...")
        for item in self.content:
            item['summary'] = self.summarize_content(item['summary'])
        return self.content

    def summarize_content(self, text):
        try:
            return summarize(text)
        except ValueError:
            # If the text is too short for gensim to summarize, return the original text
            return text
```
