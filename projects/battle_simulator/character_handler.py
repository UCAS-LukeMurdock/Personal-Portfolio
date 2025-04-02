# Luke Murdock, Character Handler and uses Faker for character ideas and generating characters
from faker import Faker
from faker.providers import DynamicProvider
from projects.battle_simulator.file_handler import read_file, write_file, intput, find

def class_stats(user_class, charac): # Applies Stat Changes depending on Class
    if user_class == 1:
        charac["Class"] = "Basic Human"
        charac["Health"] += 1
        charac["Strength"] += 1
        charac["Defense"] += 1
        charac["Speed"] += 1
    elif user_class == 2:
        charac["Class"] = "Knight"
        charac["Health"] += 1
        charac["Strength"] += 2
        charac["Defense"] += 1
        charac["Speed"] += -1
    elif user_class == 3:
        charac["Class"] = "Ranger"
        charac["Strength"] += 2
        charac["Defense"] += -1
        charac["Speed"] += 2
    elif user_class == 4:
        charac["Class"] = "Mage"
        charac["Health"] += 2
        charac["Strength"] += -1
        charac["Speed"] += 2
    return charac

def fake_character(): # Displays a fake character with a name and a backstory
    fake = Faker()
    name = fake.name()
    print(f"\nName: {name}\nBackstory: {name} was born on {fake.date_of_birth()} in {fake.local_latlng()[4].split("/")[1]} on {fake.street_name()} Street which is located in {fake.country()}. They speak the language of {fake.language_name()}. Their job is a {fake.job()} where they use the {fake.currency_name()}. They own an anient, magical artifact that would normally cost {fake.pricetag()}.")
    retry = intput(f"\nNew Idea(1) Continue(2)\n", 1,2)
    if retry == 1:
        fake_character()
        return

def generate_charac(): # Uses Faker to randomly generate a character with stats and the user decides on one
    fake = Faker()
    stat_provider = DynamicProvider(
        provider_name="stat",
        elements=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],)
    fake.add_provider(stat_provider)
    class_provider = DynamicProvider(
        provider_name="classes",
        elements=["Basic Human", "Knight", "Ranger", "Mage"],)
    fake.add_provider(class_provider)
    while True:
        charac = {
        "Name": fake.name(),
        "Class": fake.classes(),
        "Level": 0,
        "Health": fake.stat(),
        "Strength": fake.stat(),
        "Defense": fake.stat(),
        "Speed": fake.stat(),
        "Money": 0,
        "Potion": "none",
        "Sword": "no",
        "Equipped": "no"}
        stat_total = charac["Health"] + charac["Strength"] + charac["Defense"] + charac["Speed"]
        if stat_total == 16:
            break
    charac = class_stats(charac['Class'], charac)
    print(f"Character Generated\n\n{charac["Name"]}:\nClass- {charac["Class"]}\nLevel- {charac["Level"]}\nMoney- ${charac["Money"]}\nHealth Stat- {charac["Health"]}\nStrength Stat- {charac["Strength"]}\nDefense Stat- {charac["Defense"]}\nSpeed Stat- {charac["Speed"]}\nPotion- {charac["Potion"]}\nSword- {'Basic' if charac["Sword"] == 'no' else 'Sharp' if charac["Equipped"] == 'yes' else 'Basic (Sharp Unequipped)'}")
    retry = intput(f"\nRegenerate(1) Keep(2) Exit(3)\n", 1,3)
    if retry == 1:
        generate_charac()
        return
    if retry == 3:
        return
    characs = read_file()
    characs.append(charac)
    write_file(characs)

def create(): # Lets the user choose a name, class, and stats for a new character
    points_left = 16
    name = input("\nCharacter's Name [Exit(0) Character Idea(1) Generate Character(2)]: \n").strip()
    if name == "0":
        return
    elif name == "1":
        fake_character()
        create()
        return
    elif name == '2':
        generate_charac()
        return
    user_class = intput("\nCharacter's Class (Classes Affect Stats and Powers):\nBasic Human(1) Knight(2) Ranger(3) Mage(4)\n", 1,4)
    print("\nYour character has four stats: Health, Strength, Defense, Speed\nThey are given 16 points overall and you decide how many points are allocated to each stat")
    
    def stat_input(stat_type):
        nonlocal points_left
        stat = intput(f"Character's {stat_type} Stat: ", 0,points_left)
        points_left -= stat
        return stat
    
    health = stat_input("Health")
    stren = stat_input("Strength")
    defen = stat_input("Defense")
    speed = stat_input("Speed")
    charac = {
        "Name": name,
        "Class": "Added Soon",
        "Level": 0,
        "Health": health,
        "Strength": stren,
        "Defense": defen,
        "Speed": speed,
        "Money": 0,
        "Potion": "none",
        "Sword": "no",
        "Equipped": "no"}
    charac = class_stats(user_class, charac)
    print(f"\nApplied Class Stat Changes\n\nCharacter Created\n{charac["Name"]}:\nClass- {charac["Class"]}\nLevel- {charac["Level"]}\nMoney- ${charac["Money"]}\nHealth Stat- {charac["Health"]}\nStrength Stat- {charac["Strength"]}\nDefense Stat- {charac["Defense"]}\nSpeed Stat- {charac["Speed"]}\nPotion- {charac["Potion"]}\nSword- {'Basic' if charac["Sword"] == 'no' else 'Sharp' if charac["Equipped"] == 'yes' else 'Basic (Sharp Unequipped)'}")
    retry = intput(f"\nYou Have {points_left} points left\nRetry(1) Keep(2)\n", 1,2)
    if retry == 1:
        create()
        return
    characs = read_file()
    characs.append(charac)
    write_file(characs)

def display(): # Displays all of the info for all of the characters
    characs = read_file()
    print("\nYour Characters")
    if characs == []:
        print("\nNone")
        return
    for charac in characs:
        print(f"\n{charac["Name"]}:\nClass- {charac["Class"]}\nLevel- {charac["Level"]}\nMoney- ${charac["Money"]}\nHealth Stat- {charac["Health"]}\nStrength Stat- {charac["Strength"]}\nDefense Stat- {charac["Defense"]}\nSpeed Stat- {charac["Speed"]}\nPotion- {charac["Potion"]}\nSword- {'Basic' if charac["Sword"] == 'no' else 'Sharp' if charac["Equipped"] == 'yes' else 'Basic (Sharp Unequipped)'}")

def remove(): # Removes a specifed character by inputted name
    characs = read_file()
    charac_name, ind = find("What is the name of the character you want removed?:\n", characs)
    if ind == -1:
        print(f"\nUnsuccessfully Removed\n{charac_name} Can't Be Found")
        return
    else:
        characs.pop(ind)
        print(f"\n{charac_name} Successfully Removed")
        write_file(characs)