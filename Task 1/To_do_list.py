tasks = []

def add(task):
    tasks.append(task)
    print("Task added:", task)

def list_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

def delete(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print("Deleted:", deleted_task)
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            index = int(input("Enter task index to delete: "))
            delete(index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    print("Welcome to the To-Do List App!")
    main()
