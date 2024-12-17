from datetime import datetime
import json

class Task:
    def __init__(self, id, title, description, done, priority, due_date):
        self.id:int = id
        self.title:str = title
        self.description:str = description
        self.done:bool = done
        self.priority:str = priority
        self.due_date:str = due_date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'priority': self.priority,
            'due_date': self.due_date
        }

    def from_dict(self, task_dict):
        task = Task(task_dict['id'], task_dict['title'], task_dict['description'], task_dict['done'], task_dict['priority'], task_dict['due_date'])
