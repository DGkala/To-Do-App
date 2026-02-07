from todo_functions import *

tasks = load_tasks()
while True:

    print ("\n To Do List Project \n Menu \n 1)Read \n 2)Create \n 3)Delete \n 4)Edit \n 5)Quit")
    answer = input ("Select what you want to do (1/2/3/4/5): ")


    if answer == "2":

        add_task(tasks)

    elif answer == "1":

        show_tasks(tasks)

    elif answer == "3":

        delete_task(tasks)

    elif answer == "4":

        edit_tasks(tasks)

    elif answer == "5":
        print ("Quitting..")   
        break 
    else:
        print ("Invalid choice! Select 1,2,3,4 or 5.")