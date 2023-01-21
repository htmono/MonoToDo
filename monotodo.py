# Tarvittavat toiminnot:
# luo uusi tehtävä/task ja tallenna se listaan(?)
# poista tehtävä listalta
# näytä lista tehtävistä
# tallenna lista tiedostoon
# lataa lista tiedostosta

taskList = ['testi', 'ykskaks', 'jehjehkolme']

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

def listTasks():
    print("Your tasks: ")
    for x in taskList:
        print(f"Task {taskList.index(x) + 1}: {x}")

def showHelp():
    print("This is a placeholder help text")

# Main loop
def main():
    # Introbanner
    print("Welcome to")
    print("  __  __  ___  _  _  ___    _____ ___      ___   ___  ")
    print(" |  \/  |/ _ \| \| |/ _ \  |_   _/ _ \ ___|   \ / _ \ ")
    print(" | |\/| | (_) | .` | (_) |   | || (_) |___| |) | (_) |")
    print(" |_|  |_|\___/|_|\_|\___/    |_| \___/    |___/ \___/ ")
    print("                                                      ")
    print("------------------------------------------------------")

    while True:

        stuff = (input(": "))

        # Create Task with "add" or "a"
        if stuff.lower() == str.lower("add") or stuff.lower() == str.lower("a"):
            createTask()

        # List all your tasks with "list" or "l"
        if stuff.lower() == str.lower("del") or stuff.lower() == str.lower("d"):
            deleteTask()

        elif stuff.lower() == str("list") or stuff.lower() == str("l") or stuff.lower() == str("ls"):
            listTasks()

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