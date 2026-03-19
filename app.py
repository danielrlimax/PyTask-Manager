from Manager import Manager
from Task import Task
from Status import Status
from datetime import date

def main():
    manager = Manager()

    while True:
        print("\n==== TO-DO LIST ====")
        print("1 - Create Task")
        print("2 - List Tasks")
        print("3 - Remove Task")
        print("4 - Update Status")
        print("5 - Edit Task")
        print("6 - Filter by Status")
        print("0 - Exit")

        option = input("Choose an option: ")

        #===Create Task===
        if option == "1":
            name = input("Task name: ").strip()
            if not name:
                print("Name cannot be empty!")
                continue
            description = input("Description: ").strip()
            creation_date = date.today().strftime("%Y/%m/%d")
            task = Task(name, description, Status.TODO, creation_date)
            manager.add_task(task)
            print("Task created!")
        
        #===List Task===
        elif option == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("No tasks found.")
            for i, task in enumerate(tasks):
                print(f"{i} - {task}")

        #===Remove Task===
        elif option == "3":
            tasks = manager.list_tasks()
            for i, task in enumerate(tasks):
                print(f"{i} - {task}")
            index = int(input("Select index to remove: "))
            if manager.remove_task_by_index(index):
                print("Task removed.")
            else:
                print("Invalid index!")

        #===Update Status===
        elif option == "4":
            tasks = manager.list_tasks()
            for i, task in enumerate(tasks):
                print(f"{i} - {task}")
            index = int(input("Select task index: "))
            print("1 - To Do\n2 - Doing\n3 - Done")
            status_input = input("Choose new status: ")
            status_map = {"1": Status.TODO, "2": Status.DOING, "3": Status.DONE}
            status = status_map.get(status_input)
            if status and manager.update_task_status(index, status):
                print("Status updated.")
            else:
                print("Invalid selection!")

        #===Edit Task===
        elif option == "5":
            tasks = manager.list_tasks()
            for i, task in enumerate(tasks):
                print(f"{i} - {task}")
            index = int(input("Select task index: "))
            name = input("New name (leave blank to keep): ")
            desc = input("New description (leave blank to keep): ")
            status_input = input("New status (To Do / Doing / Done, leave blank to keep): ")
            status = None
            if status_input:
                try:
                    status = Status(status_input)
                except ValueError:
                    print("Invalid status!")
                    continue
            if manager.edit_task_by_index(index, name or None, desc or None, status):
                print("Task updated.")
            else:
                print("Invalid index!")

        #===Filter by Status===
        elif option == "6":
            status_input = input("Filter status (To Do / Doing / Done): ")
            try:
                status = Status(status_input)
            except ValueError:
                print("Invalid status!")
                continue
            tasks = manager.filter_tasks_by_status(status)
            if not tasks:
                print("No tasks found.")
            for i, task in enumerate(tasks):
                print(f"{i} - {task}")

        #===Exit===
        elif option == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()