# Functionalities:
# Create new task and save it to the list
# delete task from the list
# Show the list
# Save to 'mytasks.json file'
# Load from file automatically at the start

import json
import os.path


# Check if you already have saved file. If not, create new empty list
def isThereSave():
    global taskList
    file_exists = os.path.exists("mytasks.json")
    if file_exists == True:
        taskList = []
        file = open("mytasks.json")
        taskList = json.load(file)
    else:
        taskList = []

def createTask():
    taskList.append(input("Add task to the list: "))

def deleteTask():
    listTasks()
    toPop = int(input("Delete task number: "))
    if toPop >= 1 and toPop <= len(taskList):
        taskList.pop(toPop - 1)
    else:
        # If task number doesn't exist in the list, tell it and list all the current tasks.
        print("!!No such task exists!!")
        listTasks()

# Mark task as done. Give it a '*' marking and move it to another list.
def taskDone():
    pass


def listTasks():
    print("Your tasks: ")
    for x in taskList:
        print(f"Task {taskList.index(x) + 1}: {x}")

def saveTasks():
    with open('mytasks.json', 'w') as file:
        json.dump(taskList, file)

def showHelp():
    print("Available commands:")
    print("[A]dd tasks")
    print("[D]elete task")
    print("[L]ist all your current tasks")
    print("[S]ave")
    print("[E]xit")


# Main loop
def main():
    isThereSave()
    # Introbanner
    print("Welcome to")
    print("  __  __  ___  _  _  ___    _____ ___      ___   ___  ")
    print(" |  \/  |/ _ \| \| |/ _ \  |_   _/ _ \ ___|   \ / _ \ ")
    print(" | |\/| | (_) | .` | (_) |   | || (_) |___| |) | (_) |")
    print(" |_|  |_|\___/|_|\_|\___/    |_| \___/    |___/ \___/ ")
    print("                                                      ")
    print("------------------------------------------------------")
    showHelp()
    while True:

        stuff = (input(": "))

        # Create Task with "add" or "a"
        if stuff.lower() == str.lower("add") or stuff.lower() == str.lower("a"):
            createTask()

        # Delete task with "del" or "d"
        if stuff.lower() == str.lower("del") or stuff.lower() == str.lower("d"):
            deleteTask()

        # List all your tasks with "list" or "l"
        elif stuff.lower() == str("list") or stuff.lower() == str("l") or stuff.lower() == str("ls"):
            listTasks()

        # Save your To-Do list to a file
        elif stuff.lower() == str("save") or stuff.lower() == str("s"):
            saveTasks()

        # Show help with "help" or "h"
        elif stuff.lower() == str("help") or stuff.lower() == str("h"):
            showHelp()

        # Stop running the app with "exit"
        elif stuff == str("exit"):
            break

        else:
            pass
        

if __name__ == "__main__":
    main()