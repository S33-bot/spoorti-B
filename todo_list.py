# Simple To-Do List Application

tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(i, "-", task)

while True:
    print("\n----- TO-DO LIST MENU -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()

    elif choice == '2':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '3':
        show_tasks()
        try:
            num = int(input("Enter task number to update: "))
            if 1 <= num <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[num-1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except:
            print("Invalid input.")

    elif choice == '4':
        show_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print("Task removed:", removed)
            else:
                print("Invalid task number.")
        except:
            print("Invalid input.")

    elif choice == '5':
        print("Exiting To-Do List Application.")
        break

    else:
        print("Invalid choice! Try again.")