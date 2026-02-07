import json

def load_tasks():
    try:
        with open("list.json", "r") as f:
            return json.load(f)
    except:
        return []
    
def save_tasks(tasks):
    with open("list.json", "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("Your todo list is empty!")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i} - {task}")

def add_task(tasks):
    new_task = input ("What you want to add in your list; ")
    tasks.append(new_task)
    save_tasks(tasks)
    print ("You sucessfuly add a new task")

def delete_task(tasks):
    print("Your current tasks:")
    show_tasks(tasks)
    if not tasks:
        return
    
    new_delete = input ("Which task you want to delete (press number)? ")    
    if new_delete.isdigit():
        choice = int(new_delete)
        if 1 <= choice <= len(tasks):
            tasks.pop(choice -1)
            save_tasks(tasks)
            print ("Task deleted!")
        else:
            print("Invalid number!")
    else:
        print ("Please enter a valid number!")   

def edit_tasks(tasks):
    if not tasks:
        print("Your todo list is empty!")
        return

    print("Your current tasks:")
    show_tasks(tasks)

    choice = input("Which task number do you want to edit? ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(tasks):
            new_name = input("Enter the new name for the task: ")
            tasks[choice - 1] = new_name  
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number!")
    else:
        print("Please enter a valid number!")



