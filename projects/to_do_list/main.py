#Luke Murdock, To Do List

tasks = []
# Splits the text file into lists and turns that into a list of dictionaries
with open("projects/to_do_list/list.txt", "r") as file:
    reader = file.read().split("\n")
    for row_index, row in enumerate(reader):
        details = row.split("|")
        if row_index == 0:
            detail_types = [detail for detail in details]
            continue
        task = {}
        for detail in details:
            task.update({detail_types[details.index(detail)]:detail})
        tasks.append(task)

def num_input(prompt, range = 0, data_type = "int"): # Checks and solves errors in int and float inputs (Has Range If Needed)
    while True:
        try: 
            if data_type == "int":
                response = int(input(prompt).strip())
            elif data_type == "float":
                response = float(input(prompt).strip())
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

def display(): # Prints all of the to-do list's tasks and their status
    print("\nTo-Do List:\n")
    if tasks == []:
        print("None")
    for task in tasks:
        print(f"Task- {task['Name']}\nStatus- {task['Status']}\n")

def add(): # Adds desired task as incomplete to the list
    name = input("Task: ").strip()
    tasks.append({"Name": name, "Status": "Not Done"})
    print("Successfully Added")
    write()
    
def mark(): # Lets the user choose to mark or unmark the desired task as done
    marked = False
    choice = num_input("\nMark(1) Unmark(2) Exit(3)\n", 3)
    status = "Done"
    if choice == 2:
        status = f"Not {status}"
    elif choice == 3:
        return
    name = input("Desired Task: ").strip()
    for task in tasks:
        if name.lower() == task["Name"].lower():
            task["Status"] = status
            marked = True
    if marked == True:
        print(f"Successfully {'M' if choice == 1 else 'Unm'}arked")
    elif marked == False:
        print(f"Unsuccessfully {'M' if choice == 1 else 'Unm'}arked")
    write()

def delete(): # Deletes the desired task from the list
    deleted = False
    name = input("Desired Task: ").strip()
    for task in tasks:
        if name.lower() == task["Name"].lower():
            tasks.remove(task)
            deleted = True
    if deleted == True:
        print(f"Successfully Deleted")
    elif deleted == False:
        print(f"Unsuccessfully Deleted")
    write()

def write(): # Updates the file to what the user has already changed
    with open("projects/to_do_list/list.txt", "w") as file:
        file.write("Name|Status")
        for task in tasks:
            file.write(f"\n{task['Name']}|{task['Status']}")

def main(): # Introduces the program and then lets the user choose one of the options
    print("Welcome to this to-do list program that lets you add, mark complete, unmark, or delete a task from the list")
    while True:
        choice = num_input("\nDisplay(1) Add(2) Mark or Unmark(3) Delete(4) Exit(5)\n", 5)
        if choice == 1:
            display()
        elif choice == 2:
            add()
        elif choice == 3:
            mark()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue

if __name__ == "__main__":
    main()