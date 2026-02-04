import json

while True:
    print ("\n To Do List Project \n Menu \n 1)Read \n 2)Create \n 3)Delete \n 4)Quit")
    answer = input ("Select what you want to do (1/2/3/4): ")

    if answer == "2":
        new_task = input ("What you want to add in your list; ")

        try:
            with open("list.json", "r") as f:
                tasks = json.load(f)
        except Exception as e:
                tasks = []

        tasks.append(new_task)

        with open("list.json", "w") as f:
            json.dump(tasks, f, indent=4)
        print ("You sucessfuly add a new task")

    elif answer == "1":
        try:
            with open("list.json", "r") as f:
                tasks = json.load(f)
                for i, task in enumerate (tasks, start = 1):
                    print (f"{i} - {task}")
        except Exception as e:
            print (f"Error: {e}")

    elif answer == "3":

        try:
            with open("list.json", "r") as f:
                tasks = json.load(f)

                for i, task in enumerate (tasks, start = 1):
                    print (f"{i} - {task}")

                new_delete = input ("Which task you want to delete (press number)? ")    

                if new_delete.isdigit():
                    choice = int(new_delete)
                    if 1 <= choice <= len(tasks):
                        tasks.pop(choice -1)
                        with open("list.json", "w") as f:
                            json.dump(tasks, f, indent = 4 )
                        print ("Task deleted!")
                    else:
                        print("Invalid number!")
                else:
                    print ("Please enter a valid number!")   


        except Exception as e:
            print (f"Error: {e}")
    elif answer == "4":
        print ("Quitting..")   
        break 
    else:
        print ("Invalid choice! Select 1,2,3 or 4.")