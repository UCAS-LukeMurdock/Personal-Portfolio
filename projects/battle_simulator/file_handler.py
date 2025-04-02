# Luke Murdock, File Handler and Int Input Handler
import csv

def read_file(): # Turns a file into a list of dictionary characters
    characs = []
    with open("projects/battle_simulator/characters.csv", "r") as file:
        reader = csv.reader(file)
        for row_index, row in enumerate(reader):
            if row_index == 0:
                detail_types = row
                continue
            dict = {}
            for detail_index, detail in enumerate(row):
                if detail_index == 2 or detail_index == 3 or detail_index == 4 or detail_index == 5 or detail_index == 6 or detail_index == 7:
                    detail = int(detail)
                dict.update({detail_types[detail_index]:detail})
            characs.append(dict)
    return characs

def write_file(characs): # Writes the list of dictonary onto the file
    with open ("projects/battle_simulator/characters.csv", "w", newline="") as file:
        fieldnames = ["Name","Class","Level","Health","Strength","Defense","Speed","Money","Potion","Sword","Equipped"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(characs)

def intput(prompt, min = -1, max = -1): # Checks and prompts user to solve errors in integer inputs (Has Range If Needed)
    try:
        response = int(input(prompt).strip())
    except:
        print("Not An Integer")
        response = intput(prompt,min,max)
    if (min != -1 or max != -1) and (response < min or response > max): # If either min or max aren't -1 and the input is out of range then the user has to reinput
        print(f"Not In Range: {min}-{max}")
        response = intput(prompt,min,max)
    return response

def find(prompt, characs): # Finds the index of the desired character so then it can be used to access the character later
    ind = -1
    charac_name = input(prompt).strip()
    for charac_ind, charac in enumerate(characs):
        if charac_name.upper() == charac["Name"].upper():
            ind = charac_ind
    return charac_name, ind