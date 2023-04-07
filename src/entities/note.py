
import datetime

class Note:
    def __init__(self, user, text):
        self.user=user
        self.text=text
        self.time=datetime.date.today()

