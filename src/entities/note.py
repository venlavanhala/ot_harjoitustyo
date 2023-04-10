
import datetime

class Note:
    def __init__(self, user, text):
        self.user=user
        self.time=datetime.date.today()
        self.text=text

