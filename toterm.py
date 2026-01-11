import os
import json


if os.path.exists('todo.json'):
    with open("todo.json", "r") as f:
        tasks = json.load(f)
else:
    tasks = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "yellow": "\033[33m",
    "bold": "\033[1m",  
    "reset": "\033[0m"
}

while True:
    clear_screen()
    print(f"{colors['bold']}ToDo List in Terminal | [1.0] {colors['reset']}")

    
    if not tasks:
        print("\nNo tasks")
    else:
        for i, task in enumerate(tasks, 1):
            current_tag = task["tag"]
            tag_view = f"<{current_tag}>" if current_tag else ""
            status = "[X]" if task["done"] else "[ ]"
            task_color = colors.get(task["color"], colors["reset"])
            print(f"{i}. {status} {task_color} {task['text']}{colors['reset']} {tag_view}")
    
    print("\n| [1] add tasks | [2] done tasks | [3] delet |\n","-"*45,"\n| [4] exit | [5] add tag | [6] color tasks |")
    choice = input("\nEnter: ")

    if choice == '1':
        text = input("Enter text tasks: ")
        if text:
            tasks.append({"text": text, "done": False, "tag": "", "color": ""})
            
    elif choice == '2':
        try:
            num = int(input("Num tasks: "))
            tasks[num-1]["done"] = not tasks[num-1]["done"]
        except (ValueError, IndexError):
            input("Error! Click Enter")
            
    elif choice == '3':
        try:
            num = int(input("Num tasks: "))
            tasks.pop(num-1)
        except (ValueError, IndexError):
            input("Error! Click Enter")
            
    elif choice == '4':
        print("ok")
        break
    
    elif choice == '5':
        try:
            num = int(input("Num tasks: "))
            tag = input('Enter tag tasks: ')
            if tag:
                tasks[num-1]["tag"] = tag
        except (ValueError, IndexError):
            input("Error! Click Enter")
            
    elif choice == "6":
        try:
            num = int(input("Num tasks: "))
            user_color = input('{colors} -> : ')
            tasks[num-1]["color"] = user_color
        except (ValueError, IndexError):
            input("Error! Click Enter")
    with open('todo.json', 'w') as f:
        json.dump(tasks, f)
