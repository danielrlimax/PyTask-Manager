from Task import Task
from Status import Status
import json, os

class Manager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    #===Create Task===
    def add_task(self, task: Task): 
        self.tasks.append(task)
        self.save_tasks()

    #===Delete Task===
    def remove_task_by_index(self, index: int): 
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()
            return True
        return False

    #===Update Status===
    def update_task_status(self, index: int, new_status: Status): 
        if 0 <= index < len(self.tasks):
            self.tasks[index].update_status(new_status)
            self.save_tasks()
            return True
        return False

    #===Edit Task===
    def edit_task_by_index(self, index: int, name=None, description=None, status=None): 
        if 0 <= index < len(self.tasks):
            self.tasks[index].update(name, description, status)
            self.save_tasks()
            return True
        return False

    #===List Task===
    def list_tasks(self): 
        return self.tasks

    #===Filter Task===
    def filter_tasks_by_status(self, status: Status):
        return [task for task in self.tasks if task.get_status() == status]

    #===Save Task===
    def save_tasks(self): 
        with open("tasks.json", "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    #===Load Task===
    def load_tasks(self): 
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            self.tasks = []
