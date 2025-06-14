todo_list = []

def showmenu():
    print("\n📋 TO-DO LIST MENU")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    showmenu()
    choice = input("Choose an option (1-4): ")

    if choice=='1':
        print("\n Your tasks:")

        if not todo_list:
            print("No tasks yet!")
            
        else:
            for index, task in enumerate(todo_list, start=1):
                 print(f"{index}. {task}")


    elif choice=='2':
        task = input("Enter the task: ")
        todo_list.append(task)
        print(f"✅ '{task}' added to your list!")
 
    elif choice=='3':
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"❌ '{removed}' removed from your list.")
        else:
            print("⚠️ Invalid task number.")

    elif choice=='4':
        print("👋 Exiting To-Do List. Stay productive!")
        break
    else:
        print("❌ Invalid choice. Please select 1-4.")
