from datetime import datetime


class Todo:

    def __init__(self, title, urgency):
        self.title = title
        self.urgency = urgency
        self.completed = False
        self.created_at = datetime.now()

    @property
    def status(self):
        todo_status = 'Not Completed!'
        if self.completed:
            todo_status = 'Completed'
        return todo_status
