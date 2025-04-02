# Luke Murdock, Managing Battles
from projects.battle_simulator.file_handler import read_file, write_file, intput, find
import random

def level_up(characs, ind): # Lets the user choose which stat to improve when leveling up
    stat = intput("You Leveled Up!\nChoose Which Stat to be Improved\nHealth(1) Strength(2) Defense(3) Speed(4)\n", 1,4)
    if stat == 1:
        characs[ind]["Health"] += 1
    elif stat == 2:
        characs[ind]["Strength"] += 1
    elif stat == 3:
        characs[ind]["Defense"] += 1
    elif stat == 4:
        characs[ind]["Speed"] += 1
    return characs

def who(): # Lets the user choose who they want to be and and who they want to fight
    characs = read_file()
    fighter_name, fighter_ind = find("Who do you want to fight as? [Exit(0)]:\n", characs)
    if fighter_name == "0":
        return False, False, False
    opponent_name, opponent_ind = find("Who do you want to fight against?:\n", characs)
    fighter, opponent = characs[fighter_ind], characs[opponent_ind]
    if fighter_ind == -1 or opponent_ind == -1:
        print("\nAt Least One of Those Characters Can't Be Found")
        fighter, fighter_ind, opponent = who()
    return fighter, fighter_ind, opponent

def battle(): # Sets up and starts the battle and then lets the characters choose their actions and do their turns. It also carries out status conditions and handles results at the end.
    characs = read_file()
    fighter, fighter_ind, opponent = who()
    if fighter == False:
        return
    user_hp = 10 * fighter["Health"]
    op_hp = 10 * opponent["Health"]
    # Default Statuses
    user_poison, user_poison_count, user_frozen, user_frozen_count, user_protect, user_protect_count, user_protected_hp, gave_up = False,4,False,2,False,3,0,False
    op_poison, op_poison_count, op_frozen, op_frozen_count, op_protect, op_protect_count, op_protected_hp, = False,4,False,2,False,3,0
    while user_hp > 0 and op_hp > 0:
        print(f"{fighter['Name']}'s (Your) HP: {user_hp}     {opponent['Name']}'s (Opponent's) HP: {op_hp}\n")
        user_action = intput(f"Attack(1) Defend(2) Dodge(3) Heal(4) Class Power(5){'' if fighter["Potion"] == 'none' else ' Potion(6)'} Give Up(0)\n", 0, 5 if fighter["Potion"] == 'none' else 6)
        if user_action == 0:
            user_hp = 0
            gave_up = True
            return
        if opponent["Potion"] == 'none':
            op_action = random.randint(1,5)
        else:
            op_action = random.randint(1,6)

        def turn(attacker, attacker_action, defender, defender_action, defender_hp): # Carries out the specified action for either the user's or machine's turn
            attack, poison, frozen, protect = False,False,False,False
            if defender_action == 2 and random.randint(0,abs(10-defender["Speed"])) == 1: # Dodging
                print(f"{defender["Name"]} Dodged!")
            elif defender_action != 2 and attacker_action == 1: # Finding Attack Damage
                if attacker_action == 1 and defender_action != 2:
                    attack = attacker["Strength"] - defender["Defense"]//6
                elif attacker_action == 1 and defender_action == 2:
                    attack = attacker["Strength"] - defender["Defense"]//3 *2
                print(f"{attacker["Name"]} Hit {defender["Name"]}{f' But {defender["Name"]} was in a Defense Stance' if defender_action == 2 else ''}!")
            if defender_action == 4: #Healing
                defender_hp += defender["Health"]//4
                print(f"{defender["Name"]} Successfully Healed!")
            if attacker_action == 5: # Using a Class Power
                if attacker["Class"] == "Basic Human":
                    print(f"{attacker["Name"]} Can't Use a Class Power since they are a Basic Human")
                elif attacker["Class"] == "Knight":
                    if defender_action != 3:
                        attack = attacker["Strength"] 
                        print(f"{attacker["Name"]} used Thrust on {defender["Name"]}!")
                    else:
                        print(f"{attacker["Name"]} used Thrust but {defender["Name"]} Dodged!")
                elif attacker["Class"] == "Ranger":
                    attack = attacker["Strength"] + attacker["Speed"] - defender["Defense"]
                    print(f"{attacker["Name"]} Shot {defender["Name"]}!")
                elif attacker["Class"] == "Mage":
                    if defender_action != 3:
                        defender_hp -= attacker["Health"]*2 - defender["Defense"]//2*3
                        print(f"{attacker["Name"]} Blasted {defender["Name"]}!")
                    else:
                        print(f"{attacker["Name"]} used Blast but {defender["Name"]} Dodged!")
            elif attacker_action == 6: # Using a Potion
                if attacker["Potion"] == "none":
                    print(f"{attacker["Name"]} doesn't have any Potions")
                else:
                    if attacker["Potion"] == "Poison":
                        print(f"{attacker["Name"]} Poisoned {defender["Name"]}!")
                        poison = True
                    elif attacker["Potion"] == "Freeze":
                        print(f"{attacker["Name"]} Froze {defender["Name"]}!")
                        frozen = True
                    elif attacker["Potion"] == "Protect":
                        print(f"{attacker["Name"]} used Protection!")
                        protect = True
            if attack is not False and attack >= 0: # Dealing Damage
                if attacker_action == 5 and attacker["Class"] == "Ranger":
                    defender_hp -= attack
                else:
                    if attacker["Equipped"] == "no":
                        defender_hp -= attack
                    else:
                        defender_hp -= attack + 5
            elif attack is not False and attack < 0:
                print(f"{attacker["Name"]}'s Attack wasn't Strong enough to do any Damage to {defender["Name"]}")
            return defender_hp, poison, frozen, protect
        
        # Doing Turns and Status Conditions
        # Opponent's Turn
        if user_frozen_count < 2:
            print(f"{opponent["Name"]} is still Frozen{' but Melting' if user_frozen_count == 1 else ''}!")
            user_frozen_count += 1
        else:
            user_hp, op_poison, op_frozen, op_protect = turn(opponent, op_action, fighter, user_action, user_hp)
            if op_poison == True:
                op_poison_count = 0
                opponent["Potion"] = 'none'
            elif op_frozen == True:
                op_frozen_count = 0
                opponent["Potion"] = 'none'
            elif op_protect == True:
                op_protect_count = 0
                op_protected_hp = op_hp
                opponent["Potion"] = 'none'
            if user_poison_count < 4:
                print(f"{opponent["Name"]} felt the poison!")
                op_hp -= 3
                user_poison_count += 1
                if user_poison_count == 4:
                    print(f"{opponent["Name"]} has finally recovered from the poison!")
            if user_protect_count < 3:
                print(f"All damage {fighter["Name"]} recieved was negated because they were protected")
                user_hp = user_protected_hp
                user_protect_count += 1
        # User's Turn
        if op_frozen_count < 2:
            print(f"{fighter["Name"]} is still Frozen{' but Melting' if op_frozen_count == 1 else ''}!")
            op_frozen_count += 1
        else:
            op_hp, user_poison, user_frozen, user_protect = turn(fighter, user_action, opponent, op_action, op_hp)
            if user_poison == True:
                user_poison_count = 0
                fighter["Potion"] = 'none'
                characs[fighter_ind]["Potion"] = 'none'
            elif user_frozen == True:
                user_frozen_count = 0
                fighter["Potion"] = 'none'
                characs[fighter_ind]["Potion"] = 'none'
            elif user_protect == True:
                user_protect_count = 0
                user_protected_hp = user_hp
                fighter["Potion"] = 'none'
                characs[fighter_ind]["Potion"] = 'none'
            if op_poison_count < 4:
                print(f"{fighter["Name"]} felt the poison!")
                user_hp -= 3
                op_poison_count += 1
                if op_poison_count == 4:
                    print(f"{fighter["Name"]} has finally recovered from the poison!")
            if op_protect_count < 3:
                print(f"All damage {opponent["Name"]} recieved was negated because they were protected")
                op_hp = op_protected_hp
                op_protect_count += 1
    # End Results
    if user_hp <= 0:
        print("\nYou Lost")
        if gave_up == False:
            characs[fighter_ind]["Money"] += 1
            print(f"{fighter['Name']} earned $1")
    elif op_hp <= 0:
        print("\nYou Won!")
        characs[fighter_ind]["Money"] += 2
        print(f"{fighter['Name']} earned $2")
        characs[fighter_ind]["Level"] += 1
        characs = level_up(characs, fighter_ind)
    write_file(characs)