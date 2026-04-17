import json
from tasks.task import Task


class Storage:
    def __init__(self, filename="data/tasks.json"):
        self.filename = filename

    def save_tasks(self, tasks):
        data = [task.to_dict() for task in tasks]

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            return [self.dict_to_task(item) for item in data]

        except FileNotFoundError:
            return []

    def dict_to_task(self, data):
        task = Task(data["title"], data.get("description", ""))
        task.id = data["id"]
        task.done = data["done"]
        task.created_at = data["created_at"]
        return task