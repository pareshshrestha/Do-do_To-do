"""
This program is a basic text-based to-do list. 
There will be no additional fucntionality but just being able to view and edit the to-do list. 
This project will not have arrays. Just list and dict. 
This is also all made in the same 1 python file.

Completed on: 2/2/2025
"""

def main():
    
    #opening greeting 
    print("Welcome to Dodo.\nYour everyday text-based to-do app.\nLet's get started")
    
    #collection of variables that will host all the data for the program
    task_list = []
    
    #main functionality of the program
    while True:
        #print the actios they can do every iteration
        display_menu()
        
        #gets a number assigned to each past mentioned in display_menu:
        task_num = get_int("Please enter the number assigned to the task you would like to perform.", "That is not a valid input.\nPlease enter a whole number correlating with the task as an integer.", 5)
        
        #prints just the tasks available
        if task_num == 1:
            display_task(task_list)
            print_divider()
        
        #prints the tasks and task status
        elif task_num == 2:
            display_task_with_status(task_list)
            print_divider()
        
        #adds a task and status to the task_list
        elif task_num == 3:
            temp_task = input("Please enter the task. ").strip().capitalize()
            task_list.append({"Task": temp_task, "Status": "Just started."})
        
        #updates the status of a task in task_list
        elif task_num ==4:
            print("Choose from the following actions:\n1. Update a task status.\n2. Mark a task completed.")
            action = get_int("Please enter 1 or 2. ", "Invalid input. Please enter 1 or 2.", 2)
            display_task(task_list)
            update_task_num = get_int("Please select the task number of the task you want marked completed.", "Input error. Please select from the shown list.", len(task_list))
            
            #updates the task number called as whatever the user wants 
            #there can be constrains but as of now the user can enter anything for the status of the task
            if action == 1:
                updated_status = input("Please enter the new updated status for the task. ").strip().capitalize()
                task_list[update_task_num-1]["Status"] = updated_status
            
            #marks a task as completed
            elif action == 2:                
                task_list[update_task_num-1]["Status"] = "Completed"
            
            #catches an error if it takes place outside the score determined by the writer of the code
            else:
                print("There was some error along the way, let's try again.")                        
        
        #ends the entire program
        elif task_num == 5:
            break
        
        #catches any random error not caught by the writer of this code
        #does not break out of the loop so the program restarts again
        else:
            print("That does not fall within the number of actions we can perform. Let's try again from the top.")
    
    print_divider()
    closing_statement(task_list)




#this prints the passed list
def print_list(sorted_list):
    for i in range(len(sorted_list)):        
            print(i+1, ". ", sorted_list[i])
    print()

#this sorts the tasks into pending and completed lists 
#this returns two lists
def sort_task(tasks):
    pending = []
    completed = []
    
    for i in range(len(tasks)):
        if tasks[i]["Status"] == "Completed":
            completed.append(tasks[i]["Task"])
        else:
            pending.append(tasks[i]["Task"]+ ": " +tasks[i]["Status"])
    
    return pending, completed

#This prints tasks and it's status
def display_task_with_status(task_list):
    if len(task_list) == 0:
        print("\nThere are no tasks stored so far.\n")
    else:
        pending, completed = sort_task(task_list)
        print("This is the list of pending tasks and their status:")
        print_list(pending)
        print("This is the list of completed tasks")
        print_list(completed)


#This prints the tasks available so far. 
def display_task(task_list):
    if len(task_list) == 0:
        print("\nThere are no tasks stored so far.\n")
    else:
        for i in range(len(task_list)):
            print(i+1, ". ", task_list[i]["Task"], sep = "")
    
#End of the program
def closing_statement(final_list):
    pending, completed = sort_task(final_list)
    print("\nThis is the total stats of the user:\n")
    print(f"You left {len(pending)} tasks unfinished.")
    print(f"You completed {len(completed)} tasks.\n")
    print("Thank you for using Dodo. Hope you had a productive time!")
    
    
#Tells user what they can do with the app.
def display_menu():
    print()
    print("1. View your to-do list.")
    print("2. View your to-do list and how much you've accomplished.")
    print("3. Add a new task to your list.")
    print("4. Update the status of a task.")
    print("5. To end the program.")
    print()

#Gets the number assigned to the task the user wants to perform
def get_int(prompt,error_msg, valid_range):
    while True:
        try:
            temp_num = int(input(prompt))
            if 0 < temp_num <= valid_range:
                return temp_num
            else:
                print(error_msg) #error regarding number too big
        except ValueError:
            print(error_msg) #error regarding non-integer value

def print_divider():
    print("-:"*20)
    
main()



