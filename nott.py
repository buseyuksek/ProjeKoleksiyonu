from datetime import datetime

class Not:
    def __init__(self, content: str, date: str = None):
        self.content = content
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.date} - {self.content}"
