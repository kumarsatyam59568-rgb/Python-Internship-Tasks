
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    name = input("Enter your task: ").strip()

    if name == "":
        print("Task cannot be empty!")
        return

    tasks.append({
        "name": name,
        "completed": False
    })

    save_tasks()
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n----- YOUR TASKS -----")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} - {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            if tasks[number - 1]["completed"]:
                print("Task is already completed!")
            else:
                tasks[number - 1]["completed"] = True
                save_tasks()
                print("Task completed successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print("Deleted:", removed["name"])
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


tasks = load_tasks()


def main():
    while True:
        print("\n===== TO-DO LIST APP =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using To-Do List App!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
