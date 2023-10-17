todo_list = []

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' has been  added to the to-do list sucessfully.")

def view_tasks():
    print("\nTo-Do List:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed. : "))
        if 1 <= task_num <= len(todo_list):
            task = todo_list[task_num - 1]
            print(f"Task '{task}' has been marked as completed successfully.")
            todo_list.pop(task_num - 1)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Function to clear the entire to-do list
def clear_list():
    confirmation = input("Are you sure you want to clear the entire to-do list? (yes/no): ")
    if confirmation.lower() == "yes":
        todo_list.clear()
        print("To-do list has been cleared successfully.")
    else:
        print("Operation canceled. Thank you !")

while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Clear To-Do List")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        clear_list()
    elif choice == '5':
        print("Exiting the To-Do List Application.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
