from datetime import datetime
import json
import csv


class Task:
    def __init__(self, id, title, description, done, priority, due_date):
        self.id: int = id
        self.title: str = title
        self.description: str = description
        self.done: bool = done
        self.priority: str = priority
        self.due_date: str = due_date

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
        return Task(task_dict['id'], task_dict['title'], task_dict['description'], task_dict['done'],
                    task_dict['priority'], task_dict['due_date'])


class TaskManager:
    def __init__(self, tasks_path='data/tasks.json'):
        self.tasks_path: str = tasks_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.tasks_path, 'r') as file:
                return [task.from_dict() for task in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return 'Ошибка при загрузке файла'

    def save_tasks(self):
        with open(self.tasks_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def task_is_done(self, task_id):
        task = next((task for task in self.tasks if task.id == task_id), None)
        task.done = True
        self.save_tasks()

    def see_list_tasks(self):
        return self.tasks

    def see_task(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    def update_task(self, task_id, title=None, description=None, priority=None, due_date=None):
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            if title:
                task.title = title
            if description:
                task.description = description
            if priority:
                task.priority = priority
            if due_date:
                task.due_date = due_date
            self.save_tasks()
            return f'Задача с id={task_id} была успешно обновлена'
        else:
            return f'Задача с id={task_id} не найдена'

    def export_to_csv(self, file_path):
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=['id', 'title', 'description', 'done', 'priority', 'due_date']
            )
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())
        return f"Задачи загружены в файл={file_path}."

    def import_from_csv(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task.from_dict(
                        {
                            'id': int(row['id']),
                            'title': row['title'],
                            'description': row['description'],
                            'done': row['done'],
                            'priority': row['priority'],
                            'due_date': row['due_date']
                        }
                    )
                    self.tasks.append(task)
            return f'Задача была успешно выгружена с файла={file_path}'
        except FileNotFoundError:
            return f'Файл={file_path} не найден'

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()
        return f'Задача с id={task_id} была успешно удалена'

    def filter_tasks(self, filter_by='priority', value="Высокий"):
        return [
            task for task in self.tasks if getattr(task, filter_by, None) == value
        ]