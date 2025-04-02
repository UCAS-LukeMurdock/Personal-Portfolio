#Luke Murdock, Random Password Generator

import random, string

def num_input(prompt, data_type, range = 0): # Checks and solves errors in int and float inputs
    while True:
        try: 
            if data_type == "int":
                response = int(input(prompt))
            elif data_type == "float":
                response = float(input(prompt))
        except ValueError:
            print("Invalid Input Type")
            continue
        if range == 0 or (response > 0 and response <= range):
            break
        else:
            print("Not In Range")
            continue
    return response

def uppercase(): # Returns the uppercase letters if wanted
    upper = num_input("Uppercase Letters(1) No(2):\n", "int", range = 2)
    if upper == 1:
        return list(string.ascii_uppercase)
    else:
        return

def lowercase(): # Returns the lowercase letters if wanted
    lower = num_input("Lowercase Letters(1) No(2):\n", "int", range = 2)
    if lower == 1:
        return list(string.ascii_lowercase)
    else:
        return

def number(): # Returns numbers if wanted
    num = num_input("Numbers(1) No(2):\n", "int", range = 2)
    if num == 1:
        return list(string.digits)
    else:
        return
    
def special(): # Returns special characters if wanted
    spec = num_input("Special Characters(1) No(2):\n", "int", range = 2)
    if spec == 1:
        return list(string.punctuation)
    else:
        return

def arrange(chars, length): # Puts together a password of the wanted length
    word = ""
    letters = 1
    while letters <= length:
        for char in chars:
            if random.randint(1,150) == 1:
                word += char
                letters += 1
                break
        
    return word

def main(): # Lets the user leave or use the functions to create a list and passwords with the wanted characters.
    print("Welcome to this generator that creates random passwords based on your requirements.")
    while True:
        chars = []
        choice = num_input("Stay(1) Exit(2)\n", "int", range = 2)
        if choice == 2:
            print("Come back soon!")
            break
        try:
            chars.extend(uppercase())
        except:
            pass
        try:
            chars.extend(lowercase())
        except:
            pass
        try:
            chars.extend(number())
        except:
            pass
        try:
            chars.extend(special())
        except:
            pass
        if chars == []:
            print("No Characters Selected For Password")
            continue
        length = num_input("Length: ", "int", 1)
        
        for word_num in range(1,5):
            word = arrange(chars, length)
            print(f"Password {word_num}: {word}")

if __name__ == "__main__":
    main()