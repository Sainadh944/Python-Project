tasks=[]

def display_task():
    if len(tasks)==0:
        print("No tasks yet")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")

def add_task():
    task=input("enter a task")
    tasks.append(task)
    print("Task added")

def remove_task():
    display_task()
    index=int(input("enter the task number to remove: "))-1

    if 0<=index<=len(tasks):
        removed_task=tasks.pop(index)
        print(f"removed task: {removed_task}")
    else:
        print("Invalid number")

def main():
    while True:
        print("\nTo-Do List")
        print("1. Display Tasks")
        print("2.Add Task")
        print("3.Remove Task")
        print("4.Quit")

        choice= input("Enter your choice(1-4): ")

        if choice=='1':
            display_task()
        elif choice=='2':
            add_task()
        elif choice=='3':
            remove_task()
        elif choice=='4':
            print("Quitting the program...")
            break
        else:
            print("Invalide choice. please try again")
main()