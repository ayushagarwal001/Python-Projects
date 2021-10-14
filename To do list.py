# To do list 

tasks = []

while True:
    print('''Choice (a/d/v/e/x): ?
                Menu options
                a = add task
                d = delete task
                v = view task
                e = edit task
                x = exit           
                ''')
    inp = input("Enter a choice.")
    if inp == "a":
        print('Choice (a/d/v/e/x): a ')
        inp1 = input("Enter the task to be added to 'to do list'. ")
        tasks.append(inp1)
    elif inp == "d":
        inp2 = int(input("Enter the index of task to be removed."))
        d1 = tasks.pop(inp2)
        print(d1, "has been removed from 'to do list'.")
    elif inp == "v":
        for x in tasks:
            print(x)
    elif inp == "e":
        inp3 = int(input("Enter the index of task to be edited."))
        inp4 = input("Enter the edited task.")
        tasks[inp3] = inp4
    elif inp == "x":
        break
    else:
        print("Please enter correct input.")
   

    
    