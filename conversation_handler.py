```python
class ConversationHandler:
    def __init__(self):
        self.conversation_history = []

    def start_conversation(self, recommended_content):
        print("Starting a conversation about the recommended content...")
        for content in recommended_content:
            self.discuss_content(content)

    def discuss_content(self, content):
        print(f"Let's discuss this content: {content['title']}")
        print(f"Summary: {content['summary']}")
        print("What are your thoughts on this content?")
        user_feedback = input()
        self.conversation_history.append({
            'content': content,
            'user_feedback': user_feedback
        })

    def get_conversation_history(self):
        return self.conversation_history

    def get_user_feedback(self):
        user_feedback = [conversation['user_feedback'] for conversation in self.conversation_history]
        return user_feedback
```
