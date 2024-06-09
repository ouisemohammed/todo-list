from models.todo_list import TodoList

class TodoController:
    """
    A controller class to handle user interactions with the to-do list.

    Attributes
    ----------
    todo_list : TodoList
        an instance of the TodoList class to manage tasks

    Methods
    -------
    run():
        Starts the main loop for user input.
    """

    def __init__(self):
        """Initializes the TodoController with a new TodoList instance."""
        self.todo_list = TodoList()

    def run(self):
        """Starts the main loop for user input."""
        while True:
            user_insert = input("Please choose between 'add', 'view', 'delete', 'exit': ")

            if user_insert == "add":
                self.add_task()
            elif user_insert == "view":
                self.view_tasks()
            elif user_insert == "delete":
                self.delete_task()
            elif user_insert == "exit":
                break
            else:
                print("Invalid choice.")

    def add_task(self):
        """Handles adding a task to the to-do list."""
        task = input('Please enter a task: ')
        self.todo_list.add_task(task)

    def view_tasks(self):
        """Handles viewing tasks in the to-do list."""
        self.todo_list.view_tasks()

    def delete_task(self):
        """Handles deleting a task from the to-do list."""
        task = input("Please enter the task to delete: ")
        self.todo_list.delete_task(task)
