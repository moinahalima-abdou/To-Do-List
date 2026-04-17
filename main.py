from tasks.task_manager import TaskManager
from storage.storage import Storage


def show_menu():
    print("\n===== TO DO LIST =====")
    print("1. Ajouter une tâche")
    print("2. Lister les tâches")
    print("3. Supprimer une tâche")
    print("4. Marquer une tâche comme faite")
    print("5. Quitter")


def main():
    storage = Storage()
    manager = TaskManager(storage)

    while True:
        show_menu()
        choice = input("Choisis une option : ")

        if choice == "1":
            title = input("Titre de la tâche : ")
            description = input("Description (optionnel) : ")
            manager.add_task(title, description)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            task_id = input("ID de la tâche à supprimer : ")
            manager.delete_task(task_id)

        elif choice == "4":
            task_id = input("ID de la tâche terminée : ")
            manager.mark_task_done(task_id)

        elif choice == "5":
            storage.save_tasks(manager.tasks)
            print("Au revoir 👋")
            break

        else:
            print("Option invalide")


if __name__ == "__main__":
    main()