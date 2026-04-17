from tasks.task import Task


class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

        if self.tasks:
            self.next_id = max(int(task.id) for task in self.tasks) + 1
        else:
            self.next_id = 1

    def add_task(self, title, description=""):
        task = Task(title, description)
        task.id = self.next_id
        self.next_id += 1

        self.tasks.append(task)
        print("Tâche ajoutée !")

    def list_tasks(self):
        if not self.tasks:
            print("Aucune tâche.")
            return

        for task in self.tasks:
            status = "✔" if task.done else "❌"
            print(f"{task.id} | {task.title} | {status}")

    def delete_task(self, task_id):
        for task in self.tasks:
            if int(task.id) == int(task_id):
                self.tasks.remove(task)
                print("Tâche supprimée !")
                return

        print("Tâche introuvable.")

    def mark_task_done(self, task_id):
        for task in self.tasks:
            if int(task.id) == int(task_id):
                task.mark_as_done()
                print("Tâche marquée comme faite !")
                return

        print("Tâche introuvable.")