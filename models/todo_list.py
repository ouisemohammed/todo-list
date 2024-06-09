#this code is genrated using chatGpt

class TodoList:
    """
    A class to represent a to-do list.

    Attributes
    ----------
    tasks : list
        a list to store tasks

    Methods
    -------
    add_task(task: str):
        Adds a task to the to-do list.

    view_tasks():
        Prints all tasks in the to-do list.

    delete_task(task: str):
        Deletes a task from the to-do list.
    """

    def __init__(self):
        """Initializes an empty to-do list."""
        self.tasks = []

    def add_task(self, task: str):
        """Adds a task to the to-do list."""
        self.tasks.append(task)
        print("Task added.")

    def view_tasks(self):
        """Prints all tasks in the to-do list."""
        if not self.tasks:
            print("You have no tasks.")
        else:
            for task in self.tasks:
                print(task)

    def delete_task(self, task: str):
        """Deletes a task from the to-do list."""
        if not self.tasks:
            print("There are no tasks.")
        else:
            if task in self.tasks:
                self.tasks.remove(task)
                print("Task deleted.")
            else:
                print("No task with such a name.")
