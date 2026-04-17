import uuid
from datetime import datetime


class Task:
    def __init__(self, title, description=""):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.done = False
        self.created_at = datetime.now().isoformat()

    def mark_as_done(self):
        self.done = True