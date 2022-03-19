from markupsafe import re
from model import Todo


class TodoRepository:

    def __init__(self):
        self.todos = [Todo('todo 1', 'LOW'), Todo('todo 2', 'LOW')]

    def get_todos(self):
        return enumerate(self.todos, start=1)

    def add_todo(self, content, urgency):
        new_todo = Todo(content, urgency)
        self.todos.append(new_todo)
        return self.todos

    def get_todo_by_id(self, id):
        try:
            todo = self.todos[id - 1]
            return todo
        except IndexError:
            return None
