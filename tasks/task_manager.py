from tasks.task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
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
            if task.id == task_id:
                self.tasks.remove(task)
                print("Tâche supprimée !")
                return

        print("Tâche introuvable.")

    def mark_task_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_done()
                print("Tâche marquée comme faite !")
                return

        print("Tâche introuvable.")