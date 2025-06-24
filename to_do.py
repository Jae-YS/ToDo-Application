def add_task(task_list, task):
    """Add a new task to the list."""
    if task:
        task_list.append(task)
        print(f"Added task: {task}")
    else:
        print("No task provided to add.")
    return task_list


def view_tasks(task_list):
    """Display all tasks in the list."""
    if len(task_list) == 0:
        print("No tasks available to view.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(task_list):
        print(f"{idx + 1}. {task}")
    return task_list


def remove_task(task_list, idx):
    """Remove a task by its 1-based index."""
    if not idx.isdigit():
        print("Please enter a valid task number.")
        return task_list

    idx = int(idx)
    if idx < 1 or idx > len(task_list):
        print("Task number out of range.")
        return task_list

    removed = task_list.pop(idx - 1)
    print(f"Removed task: {removed}")
    return task_list


def run():
    """Main loop for CLI To-Do manager."""
    print("Welcome to your To-Do List Manager")
    option = 0

    task_list = []

    while option != 4:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        try:
            option = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        else:
            if option == 4:
                print("Exiting the To-Do List Manager.")
                break
            elif option < 1 or option > 4:
                print("Invalid option. Please choose a number between 1 and 4.")
                continue
            elif option == 1:
                value = input("Enter task to add: ")
                add_task(task_list, value)
            elif option == 2:
                task_list = view_tasks(task_list)
            elif option == 3:
                if not task_list:
                    print("No tasks available to remove.")
                    continue
                index = input("Enter task number to remove: ")
                task_list = remove_task(task_list, index)

        finally:
            print("-" * 40)

    return


def main():
    """Entry point."""
    run()


if __name__ == "__main__":
    main()
