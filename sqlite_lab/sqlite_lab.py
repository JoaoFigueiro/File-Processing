import sqlite3

# These commented lines are just some examples of what I learned.
# conn = sqlite3.connect("hello.db")
# conn = sqlite3.connect("C:\sqlite\hello.db")
# conn = sqlite3.connect(":memory:")

# conn = sqlite3.connect("todo.db")

# c = conn.cursor()
# c.execute(
# """
# CREATE TABLE IF NOT EXISTS tasks (
#     id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     priority INTEGER NOT NULL
# );
# """
# )
# tasks = [
#     ("My first task", 1),
#     ("My second task", 5),
#     ("My third task", 10),
# ]
# c.executemany("INSERT INTO tasks (name, priority) VALUES (?,?)", tasks)
# conn.commit()
# conn.close()

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.c = self.conn.cursor()
        self.create_task_table()
        
    def create_task_table(self):
        self.c.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
        );
        """
        )
    
    def find_task(self, name: str)-> str | None: 
        task = self.c.execute("SELECT * FROM tasks WHERE name = ?;", (name,))
        
        return task.fetchone()
    
    def find_task_by_id(self, id: str | int)-> str | None: 
        task = self.c.execute("SELECT * FROM tasks WHERE id = ?;", (id,))
        
        return task.fetchone()
    
    def validate_name(self, name)-> bool: 
        if name.isspace(): 
            print("Task name shouldn't be empty!")
            return False 
        else: 
            return True

    def validate_priority(self, priority)->bool: 
        if priority < 1: 
            print("Task priority must be greater than 1.")
            return False
        else: 
            return True 
    
    def add_task(self):
        while True: 
            name = input("Enter task name: ")

            if not self.validate_name(name): 
                continue 

            task_exists = self.find_task(name)
            
            if task_exists: 
                print("Task name already exists!") 
                continue   

            priority = int(input("Enter priority: "))
            
            if not self.validate_priority(priority): 
                continue 

            break 

        self.c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", (name, priority))
        self.conn.commit()

    def show_tasks(self): 
        tasks = self.c.execute("SELECT * FROM tasks;").fetchall()
        
        print(tasks)

    def change_priority(self): 
        id = input("Enter task id to change the priority: ")

        if not self.find_task_by_id(id): 
            print(f"Task with {id} not found!")
            return 
        
        priority = int(input("Enter new task priority: "))

        if not self.validate_priority(priority): 
            return 

        self.c.execute("UPDATE tasks SET priority = ? WHERE id = ?", (priority, id))
        self.conn.commit()

        print(f"Task {id} updated!")

    def delete_task(self):
        id = input("Enter task ID to be deleted: ")

        if not self.find_task_by_id(id): 
            print(f"Task with {id} not found!")
            return 
        
        self.c.execute("DELETE FROM tasks WHERE id = ?", (id, ))
        self.conn.commit()

        print(f"Task {id} deleted!")

    def show_menu(self): 
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Change Priority")
        print("4. Delete Task")
        print("5. Exit")

app = Todo()

valid_options = ["1", "2", "3", "4", "5"]

while True: 
    app.show_menu()

    option = input("Please, select an option: ")

    if option not in valid_options: 
        print("Invalid option!")
        continue 

    match option: 
        case "1": 
            app.show_tasks()
        case "2": 
            app.add_task()
        case "3": 
            app.change_priority()
        case "4": 
            app.delete_task()
        case "5": 
            exit()