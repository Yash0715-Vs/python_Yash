import json
import os


FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Warning: tasks.json contains invalid data.")
        return []

    except Exception as e:
        print("Error loading tasks:", e)
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)

    except Exception as e:
        print("Error saving tasks:", e)


def add_task(tasks):

    title = input("Enter task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks(tasks):

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n========== YOUR TASKS ==========")

    for index, task in enumerate(tasks, start=1):

        if task["completed"]:
            status = "✓ Completed"
        else:
            status = "✗ Pending"

        print(
            f"{index}. {task['title']} "
            f"[{status}]"
        )


def complete_task(tasks):

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(
            input("\nEnter task number to complete: ")
        )

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        task = tasks[number - 1]

        if task["completed"]:
            print("Task is already completed.")
            return

        task["completed"] = True

        save_tasks(tasks)

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(
            input("\nEnter task number to delete: ")
        )

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(number - 1)

        save_tasks(tasks)

        print(
            f"Task '{removed_task['title']}' "
            "deleted successfully!"
        )

    except ValueError:
        print("Please enter a valid number.")


def search_task(tasks):

    if not tasks:
        print("No tasks available.")
        return

    keyword = input(
        "Enter keyword to search: "
    ).lower()

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for index, task in enumerate(tasks, start=1):

        if keyword in task["title"].lower():

            status = (
                "Completed"
                if task["completed"]
                else "Pending"
            )

            print(
                f"{index}. {task['title']} "
                f"[{status}]"
            )

            found = True

    if not found:
        print("No matching tasks found.")


def main():

    tasks = load_tasks()

    while True:

        print("\n========== TO-DO MANAGER ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            search_task(tasks)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


main()