todo_list = []

#starting the while loop to get the project going
while(True):

#asking the user for his action 
    user_insert = input("please choose between 'add , view , delete, exit :'")
    
#checking different cases of user insert even if the user inserted something no aviable
    if user_insert == "add":
        task = input('please inter a task :')
        todo_list.append(task)
        print("task added")
    elif user_insert == "view":
        if not todo_list:
            print("you have no tasks")
        else:
            for task in todo_list:
                print(task)
    elif user_insert == "delete":
        if not todo_list:
            print('there are no tasks')
        else:
            task = input("please insert a task:")
            if task in todo_list:
                todo_list.remove(task)
                print("task deleted")
            else:
                print("NO task with such a name")
    elif user_insert == "exit":
        break
    else:
        print('Invalid Choice') 
