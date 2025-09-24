print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Mark as Complete\n5. Exit\n")
choice=int(input("Enter your choice: "))
tasks=[]
completed_tasks=[]
while choice!=5:
    if choice==1:
        task=input("Enter the task: ")
        tasks.append(task)
        with open("tasks.txt","a") as file:
            file.write(task+"\n")
        print("Task added.")
    elif choice==2:
        ch=int(input("View (1) All Tasks or (2) Completed Tasks (3) Both? "))
        if ch==1:
            print("All Tasks:")
            for i,task in enumerate(tasks):
                print(f"{i+1}. {task} ")
        elif ch==2:
            print("Completed Tasks:")
            for i,task in enumerate(completed_tasks):
                print(f"{i+1}. {task} (Completed) ")
        elif ch==3:
            print("All Tasks:")
            for i,task in enumerate(tasks):
                print(f"{i+1}. {task} ")
            print("\nCompleted Tasks:")
            for i,task in enumerate(completed_tasks):
                print(f"{i+1}. {task} (Completed) ")
        print("\n")
    elif choice==3:
        task_num=int(input("Enter the task number to delete: "))
        if 0<task_num<=len(tasks):
            tasks.pop(task_num-1)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    elif choice==4:
        task_num=int(input("Enter the task number to mark as complete: "))
        if 0<task_num<=len(tasks):
            completed_tasks.append(tasks.pop(task_num-1))
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    else:
        print("Invalid choice.")
    print("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Mark as Complete\n5. Exit \n")
    choice=int(input("Enter your choice: "))
