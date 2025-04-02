#Luke Murdock, Final Project

import random

hpPmax = 100
strength = 0
sight = 0
axe = True
axeCl = False
gotPotion = False
invent = ["Axe", "Sword"]
adventure = ["Ocean -> "]

firstTimeT = True
firstTimeV = True
firstTimeCl = True
firstRFiend = True
firstTimeCa = True
firstTimeM = True

winGame = False
lostGame = False
lostBattle = False
ending2 = False
islandRule = False


def ask(choiceRange, ocean = False):
    while True:
        try:
            choice = int(input(""))
        except:
            print("Input not accepted. Try again")
            continue
        if choice <= 0 or choice > choiceRange:
            print("Number not accepted. Try again")
            continue
        if ocean == True and choice == 2:
            print("Are you sure you want to lose the game? Yes(1) No(2)")
            oceanChoi = ask(2)
            if oceanChoi == 2:
                print("Where do you want to go then?")
                continue
            
        break
    return choice

    return choice
def askInventory():
    print("\nExplore Further(1) Open Inventory and Stats(2)")
    askInvent = ask(2)
    if askInvent == 2:
        inventAccess()
def inventAccess():
    while True:
        print(f"\nInventory: {invent} \nStats: {hpPmax} HP | {strength} Strength | {sight} Sight")
        inventChoice = input("Type which Item/Stat you want to know about or 1 to leave:\n").title()
        print("")
        if inventChoice == "Axe" and inventChoice in invent:
            print("Damage: 15\nDescription: You got this throwing axe from the pirates. To use this weapon you have to throw it, so be careful. This item is light but is also increased with strength.")
        elif inventChoice == "Sword" and inventChoice in invent:
            print("Damage: 10\nDescription: An ancient sword found on the beach")
        elif inventChoice == "Sand Gem" and inventChoice in invent:
            print("Damage: Sight\nDescription: From the eye of a sandstorm, this gem has a chance to blind its victim for a turn")
        elif inventChoice == "Bow" and inventChoice in invent:
            print("Damage: 20\nDescription: Takes a turn to charge up and then launches a powerful arrow")
        elif inventChoice == "Ice Wand" and inventChoice in invent:
            print("Damage: 0\nDescription: This wand freezes its victim for two turns, but needs time to recharge")
        elif inventChoice == "Rock Gem" and inventChoice in invent:
            print("Damage: Strength\nDescription: Created from the pressure of a mountain, this gem can shoot rocks that can confuse their victim")
        elif inventChoice == "Inferno Sword" and inventChoice in invent:
            print("Damage: 25\nDescription: This blade burns like the heart of a volcano")
        elif inventChoice == "Potion" and inventChoice in invent:
            print("Can be used up in battle to heal you to your max HP")
        elif inventChoice == "Hp":
            print("This is your maximum health. If your health reaches zero, you lose the game. You regenerate all your health after each battle. Also, you can sometimes increase your maximum health")
        elif inventChoice == "Strength":
            print("This increases the damage of a sword and other heavy items")
        elif inventChoice == "Sight":
            print("This increases the damage of a bow and other light items")
        elif inventChoice == "1":
            break
        else:
            print("That is not in your inventory")

def battle(hpOmax, damageO, nameO, bossBattle = False):
    global axe, invent, hpPmax, strength, sight, lostBattle, ending2

    hpO = hpOmax
    hpP = hpPmax
    bowWait = False
    frozen = False
    frozenCounter = 0
    usedWand = False
    blind = False
    dodge = False
    dodgeO = False
    stren = 0 #Temporary strength boost
    sigh = 0 #Temporary sight boost
    confus = 1
    dodgeUp = False
    defense = 0
    axe = True

    while hpP > 0 and hpO > 0:
        print(f"\nYour HP: {hpP}/{hpPmax}  {nameO.title()}'s HP: {hpO}/{hpOmax}")
        if bowWait == True:
            if dodgeO is True:
                print(f"{nameO.title()} dodged and you missed your shot!")
            elif dodgeO == False:
                hpO -= 20 + sight + sigh
                print(f"You shot {nameO}")
            bowWait = False
        elif bowWait == False:
            while True:
                while True:
                    action = input(f"Dodge(1) Focus(2) Item(Choose) {invent}\n").title() #title's answer to make it work wihout capitalization
                    if action in invent or action == "1" or action == "Dodge" or action == "2" or action == "Focus": #If their input works
                        break
                    else: #If input doesn't work
                        print("Input not accepted. Try again")

                if action == "1" or action == "Dodge":
                    dodgeChance = random.randint(1, 100)
                    if dodgeUp == False:
                        if dodgeChance <= 20:
                            dodge = False
                            print("You failed at dodging!")
                            break

                        elif dodgeChance <= 60:
                            dodge = True
                            print("You prepare to dodge")
                            break

                        elif dodgeChance <= 100:
                            dodge = True
                            print("You prepare to dodge and you get to take another action!")
                            continue
                    elif dodgeUp == True:
                        dodgeUp = False
                        if dodgeChance <= 10:
                            dodge = False
                            print("You failed at dodging!")
                            break

                        elif dodgeChance <= 45:
                            dodge = True
                            print("You prepare to dodge")
                            break

                        elif dodgeChance <= 100:
                            dodge = True
                            print("You prepare to dodge and you get to take another action!")
                            continue

                elif action == "2" or action == "Focus":
                    boostNum = 0
                    while boostNum < 2:
                        waitChance = random.randint(1,11)
                        if waitChance == 1 or waitChance == 2: #HP Boost
                            if hpP >= hpPmax:
                                continue
                            elif hpP <= hpPmax:
                                hpP += 15
                                print("You focused and now feel enhanced")
                        elif waitChance == 3 or waitChance == 4: #Strength Boost
                            stren += 2
                            print("You focused and now feel enhanced")
                        elif waitChance == 5 or waitChance == 6: #Sight Boost
                            sigh += 2
                            print("You focused and now feel enhanced")
                        elif waitChance == 7 or waitChance == 8: #Dodge Boost
                            if dodgeUp == True:
                                continue
                            elif dodgeUp == False:
                                dodgeUp = True
                                print("You feel more ready to dodge")
                        elif waitChance == 9 or waitChance == 10: #Defense Boost
                            defense += 10
                            print("You take a defense stance")
                        elif waitChance == 11: #Failed
                            if boostNum == 0:
                                print("You failed to center your concentration, but you keep trying")
                            else:
                                print("You tried to focus again, but your concentration broke")
                        boostNum += 1
                    break

                elif action == "Potion":
                    hpP = hpPmax
                    invent.remove("Potion")
                    print("You drank the potion")
                    break

                elif action == "Bow":
                        print("You charge your bow")
                        bowWait = True
                        break

                elif dodgeO == False:
                    
                    if action == "Axe":
                        hpO -= 15 + strength + stren + sight + sigh
                        print(f"You throw your axe and it hits {nameO}!")
                        invent.remove("Axe")
                        axe = False
                        break
                    elif action == "Sword":
                        hpO -= 10 + strength + stren
                        print(f"You hit {nameO}!")
                        break

                    elif action == "Sand Gem":
                        hpO -= sight + sigh
                        blind = random.choice([True, True, False])
                        if blind == True:
                            print(f"You hit and blinded {nameO}!")
                        elif blind == False:
                            print(f"You just hit {nameO}!")
                        break

                    elif action == "Ice Wand":
                        if usedWand == False:
                            usedWand = True
                            frozen = True
                            print(f"You froze {nameO}!")
                            print("The Ice Wand's power looks completely drained.")
                        elif usedWand == True:
                            print("Oh no! The Ice Wand doesn't work anymore. It looks drained.")
                        break

                    elif action == "Rock Gem":
                        hpO -= strength + stren
                        print(f"You hit {nameO}!")
                        confus = 2
                        break

                    elif action == "Inferno Sword":
                        hpO -= 25 + strength + stren
                        print(f"You hit {nameO}!")
                        break

                if dodgeO == True:
                    print("The Twin dodged!")
                    break

        # OPPONENT'S TURN         ADDDDD CRITSSSSS
        dodgeO = False
        if frozen == True or blind == True:
            print(f"{nameO.title()} can't do anything")
            if frozen == True:
                frozenCounter += 1 
                if frozenCounter >= 2:
                    frozen = False
        elif frozen == False or blind == False:
            
            if bossBattle == True:
                while True:
                    actionO = random.choice([True, True, False])

                    if actionO == False:
                        dodgeOChance = random.randint(1, 100)
                        if dodgeOChance <= 70:
                            dodgeO = True
                            break
                        elif dodgeOChance <= 100:
                            dodgeO = True
                            continue

                    if actionO == True:
                        if dodge is True:
                            print("You dodged!")
                            dodge = False
                        elif dodge is False:
                            hpP -= (damageO / confus) - defense
                            print("You got hit!")
                        break
            else:
                if dodge is True:
                    print("You dodged!")
                    dodge = False
                elif dodge is False:
                    hpP -= (damageO / confus) - defense
                    print("You got hit!")
        confus = 1
        blind = False
        defense = 0

            
    print(f"\nYour HP: {hpP}/{hpPmax}  {nameO.title()}'s HP: {hpO}/{hpOmax}")
    if hpP < hpO:
        print("You lost the battle! :(")
        lostBattle = True
    elif hpO <= 0:
        lostBattle = False
        print(f"You {'barely ' if hpP <= 5 else''}won the battle!") # Adds barely if almost dead
        if axe == False:
            print("You fetch your fallen axe.")
            invent.insert(0, "Axe")

        if hpP >= 70:
            hpPmax += 5
            strength += 1
            sight += 1
        elif hpP >= 30:
            hpPmax += 10
            strength += 2
            sight += 2
        elif hpP < 30:
            hpPmax += 20
            strength += 4
            sight += 4

    if bossBattle == True and hpP < 20 and lostBattle == False:
        ending2 = True


def beach():
    global adventure
    adventure.append("Beach -> ")
    print("\nYou had been sailing at sea for 5 months with your pirate crew, when you finally came to an island with many differing terrains. One mountain towers over them all. The captain decides to send you onto the island to find treasure to make sure he doesn't lose any valuable members of the crew. The pirate ship crosses the last part of the deep blue ocean and lands on the biggest beach that could be seen. The crew will sail to the other side of the island to pick you up there. You hop off the boat and onto the sand, which looks suspiciously like treasure.\n")
    print("Waves crash onto the beach of this new island. The sand is a shining gold and there are beautiful seashells scattered across the scene. You pick up some sand and let it fall through your fingers. Even though it looks like gold, it clearly is not, now that you're seeing it up close. Out of the corner of your eye, you see a sparkling light. A lone blade embedded in the center of the beach. You run up to it and pull the sword smoothly out of the sand. \n\nYou got a Sword!")

    askInventory()
    print("You see sprawling plains to the left and a perilous desert to the right. \nWhere do you go? Plains(1) Desert(2)")
    locChoi1 = ask(2)
    if locChoi1 == 1:
        plains()
    elif locChoi1 == 2:
        desert()

    if winGame == True:
        print("Won Game")
        print(f"The items you found: {invent[1:]}")
        if islandRule == False:
            adventure.append("Ocean")
        elif islandRule == True:
            adventure.append("Island")
    elif lostBattle == True or lostGame == True:
        print("Lost Game")
    if lostBattle == True:
        adventure.append("END")
        print(f"The items you found: {invent}")
    if lostGame == True:
        print(f"The items you found: {invent[1:]}")

    trail = ""
    for place in adventure:
        trail += place
    print(trail)

def plains():
    global hpPmax
    global strength
    global sight
    global adventure
    adventure.append("Plains -> ")
    print("The wind cuts through thousands of blades of grass. The ocean of green rolls over curving hills. In the distance, the mountain looms a bit closer, which creates this beautiful, safe valley. You see sparse, colorful flowers at the bottom of the hills. You stroll through the fields of grass to these bits of vibrant color. As you come closer you see three distinct flowers. The first is a scarlet red, petals coming together to make what looked like a cup. The second is as blue as the ocean you came from, tiny petals sprouting from every branch. The last is a fiery orange, one huge flower with hundreds of petal layers.\n")
    print("Which do you eat? Red(1) Blue(2) Orange(3) All(4) None(5)")
    plainsChoi = ask(5)
    if plainsChoi == 1:
        hpPmax += 20
        print("You feel something inside of you change, but you don't know what.")
    elif plainsChoi == 2:
        sight += 5
        print("You feel something inside of you change, but you don't know what.")
    elif plainsChoi == 3:
        strength += 5
        print("You feel something inside of you change, but you don't know what.")
    elif plainsChoi == 4:
        hpPmax -= 30
        sight += 10
        strength += 10
        print("You feel something inside of you change, but you don't know what.")
    elif plainsChoi == 5:
        print("You instead find a pink flower that has a peice of paper attached to it that writes, 'This flower comes from the east flower field where its siblings reside. That field is also home to the rich human who can dodge and sometimes even dodge and attack at the same time! He rarely ever fails dodging.'")

    askInventory()
    print("You see a frigid tundra ahead of you and a crowded forest to the right. \nWhere do you go? Tundra(1) Forest(2)")
    locChoi2 = ask(2)
    if locChoi2 == 1:
        tundra()
        return
    elif locChoi2 == 2:
        forest()
        return
    else:
        print("Something Went Wrong")

def desert():
    global lostBattle
    global invent
    global adventure
    adventure.append("Desert -> ")
    print("The sand of the desert is pale in contrast to the beach. The dunes of sand stretch past the horizon. Your skin starts to feel the scorching air, so you look for some way to cool down. There is no water or shelter in sight, but there is a cloud of dust brewing up ahead. The sandstorm grows and consumes you. As you push your way through the wind, you reach the eye of the storm. In the center of the storm is a petrified skeleton made of the desert. Where its heart should be, sits a glowing yellow gemstone. You pull your newly found sword out and ready yourself to face the sandfiend.\n")
    battle(70, 15, "the Sandfiend")
    if lostBattle == False:
        print("The stormfiend falls over. It crumbles to dust and its sandy remains get swept away by the wind. Its crystal heart rolls on the sand towards your feet. You pick up the sand gem.")
        invent.append("Sand Gem")
    elif lostBattle == True:
        return
    
    askInventory()
    print("You see the sprawling plains again, to the north this time, and a dense forest forward. \nWhere do you go? Plains(1) Forest(2)")
    locChoi3 = ask(2)
    if locChoi3 == 1:
        plains()
        return
    elif locChoi3 == 2:
        forest()
        return
    else:
        print("Something Went Wrong")

def tundra():
    global invent
    global adventure
    adventure.append("Tundra -> ")
    global firstTimeT
    if firstTimeT == True:
        global hpPmax
        hpPmax += 5
        print("Here in the tundra, snow is everywhere. Every single object is covered with the white powder. Evergreen trees surround you, as you walk ever onward, your shoes crunch down the cold ice. You see a jut in the snow and decide to look at it.\n")
    elif firstTimeT == False:
        print(f"You enter the freezing tundra again. {'You welcome the warmth of you Inferno Sword.' if 'Inferno Sword' in invent else 'Your start to shiver.'}")

    if "Ice Wand" not in invent:
        print(f"{'You see that same bump in the snow. ' if firstTimeT == False else''}Do you uncover the snow? Yes(1) No(2)")
        iceChoi = ask(2)
        if iceChoi == 1:
            print("\n\nYour cold hands shiver as they wipe off the snow from the hidden object. You uncover a chunk of smooth ice that you see your reflection in. The ice slightly distorts the image, but captures your key features. You abandon the ice and trudge on.\n")
        elif iceChoi == 2:
            print("You ignore the bump in the snow and keep walking. You see a stone pillar that has the words, 'Focusing has a chance to let you heal 15 HP if you are damaged, gain 2 Strength temporarily, or gain 2 Sight temporarily.'\n")
        print(f"You reach a{'nother' if iceChoi == 2 else ''} stone pillar with a riddle etched on it and a square to write your answers:")
        print("They look the same, yet they're not one, ".center(100))
        print("Two bodies, but their lives are spun, ".center(100))
        print("From the same thread, side by side, ".center(100))
        print("Always together, nowhere to hide, ".center(100))
        print("One of them may lead, the other kicked to the side, ".center(100))
        print("Though their paths are different, they would often walk as two, ".center(100))
        print("They’ve split their ways, yet their fates are still intertwined. ".center(100))
        print("What are they?".center(100))
        tundraAnswer = input("Write Guess(es):")
        if "twin" in tundraAnswer.lower():
            print("\nThe word 'twin' lit up and a blue wand with an icy gem at its top emerged from the stone. You solved the riddle and got an Ice Wand!")
            invent.append("Ice Wand")
        else:
            print("\nNothing happened, so you left.")
    
    firstTimeT = False
    askInventory()
    print("You stand at the feet of a volcano and mountain. \nWhere do you go? Volcano(1) Mountain(2)")
    locChoi4 = ask(2)
    if locChoi4 == 1:
        volcano()
        return
    elif locChoi4 == 2:
        mountain()
        return
    else:
        print("Something Went Wrong")

def forest():
    global lostBattle
    global invent
    global adventure
    adventure.append("Forest -> ")
    print("You step into the woods. The countless trees block out most of the sunlight. What little light does come through, makes the greenery shimmer. Moss-covered boulders stick out from between the dense foliage. Grass, leaves, rocks, sticks, and underbrush cover the ground. You hear the snapping of a stick and jump. You look back and the tall, sleek figure of a wood elf emerges from behind a tree.")
    battle(80, 20, "the Elf")
    if lostBattle == False:
        print("The defeated elf salutes you. She offers her green crystalline bow and you take it. She then vanishes into the wilderness.")
        invent.append("Bow")
    elif lostBattle == True:
        return
    
    askInventory()
    print("You see a freezing tundra to the north and a mountainous area ahead of you. \nWhere do you go? Tundra(1) Rocky Area(2)")
    locChoi5 = ask(2)
    if locChoi5 == 1:
        tundra()
        return
    elif locChoi5 == 2:
        cliff()
        return
    else:
        print("Something Went Wrong")

def volcano():
    global invent
    global adventure
    adventure.append("Volcano -> ")
    global firstTimeV
    if firstTimeV == True:
        global hpPmax
        hpPmax += 5
        print(f"The closer you come towards the volcano, the hotter everything feels. {'Your Ice Wand keeps your temperature stable, though. ' if 'Ice Wand' in invent else ''}Lava pops and bubbles out of holes in the rock, making tiny streams and rivers of lava. You are about to reach the caldera of the volcano but you can no longer find a way up.")
        firstTimeV = False
    elif firstTimeV == False:
        print(f"You scale the volcano {'and enjoy the nice sights from the caldera.' if 'Inferno Sword' in invent else 'and your Ice Wand keeps the terrible heat that radiates from the lava at bay.' if 'Ice Wand' in invent else 'and you hesitate moving farther because of the immense heat coming from the lava.'}")
    if "Ice Wand" in invent and "Inferno Sword" not in invent:
        volcanoPlan = input("""A single red river flows from the top of the volcano and gradually comes down.
How do you plan to get up? HINT: Think about your items 
Write your plan:
""")
        volcanoPlan = volcanoPlan.lower()
        if "cold" in volcanoPlan or "frozen" in volcanoPlan or "freeze" in volcanoPlan or "wand" in volcanoPlan or "ice" in volcanoPlan:
            print("\nYou use your Ice Wand to freeze the lava river. You clamber up your newly created road to reach the caldera. Your Ice Wand glows a bright ice blue and all of the lava begins to slow down. In a few seconds the whole volcano is no longer hot, except for a glowing, red blade in the center of the caldera. You run down and grab the flaming inferno sword. You see a crimson cyrstal at its hilt. You leave the volcano on the other side and see the deep blue of the ocean on the horizon.")
            invent.append("Inferno Sword")
        else:
            print("\nYour plan doesn’t work so you decide to keep climbing to the other side of the volcano.")
    elif "Inferno Sword" not in invent :
        print("You can't find a way to the very top of the volcano.")
    askInventory()
    print("You see a coastline where your ship has docked and there's a mountain south of you. You haven’t gained any gold yet, so if you go to the ocean, that means you've failed your quest. \nWhere do you go? Mountain(1) Ocean(2)")
    locChoi6 = ask(2, ocean = True)
    if locChoi6 == 1:
        mountain()
        return
    elif locChoi6 == 2:
        oceanEnd()
        return
    else:
        print("Something Went Wrong")

def mountain():
    global gotPotion
    global adventure
    adventure.append( "Mountain -> ")
    global firstTimeM
    if firstTimeM == True:
        global strength
        strength += 2
        global invent
        firstTimeM = False
    if gotPotion == False:
        print(f"There is a tiny patch of snow on top of the towering mountain. The high elevation makes the air thin and hard to breathe. You grow tired and cold as you climb. {'Your Inferno Sword is the only thing keeping you warm. ' if 'Inferno Sword' in invent else ''}Finally, you reach this clearing of white and find a stone pedestal with a singular bottle in the middle.")
        print("Do you take the light red bottle? Yes(1) No(2)")
        mountChoi = ask(2)
        if mountChoi == 1:
            print("You tuck the bottle away for safekeeping.")
            invent.append("Potion")
            gotPotion = True
        if mountChoi == 2:
            print("You leave the bottle alone, but while contemplating you see a note on the stone that says, 'Focusing has a chance to increase your dodging ability the next time you try to dodge. It also has a chance of making you take 10 less damage the next time you get hit.' You then keep on journeying.")
        
    elif gotPotion == True:
        print(f"You climb the mountain once again{' with the warmth of your sword at your side.' if 'Inferno Sword' in invent else '.'}")

    askInventory()
    print("You can climb down the mountain to the pink blur you see in the distance or you can go to the coastline and leave this island without any gold to share with the other pirates. To the north is the volcano. To the south is the rocky cliff area. To the west is the tundra. \nWhere do you go? Flower Field(1) Ocean(2) Volcano(3) Cliff(4) Tundra(5)")
    locChoi7 = ask(5, ocean = True)
    if locChoi7 == 1:
        flower(False)
        return
    elif locChoi7 == 2:
        oceanEnd()
        return
    elif locChoi7 == 3:
        volcano()
        return
    elif locChoi7 == 4:
        cliff()
        return
    elif locChoi7 == 5:
        tundra()
        return
    else:
        print("Something Went Wrong")

def cliff():
    global axeCl
    global adventure
    adventure.append( "Cliff -> ")
    global firstRFiend
    global firstTimeCl
    if firstTimeCl == True:
        global lostBattle
        global invent
        global axe
        if firstRFiend == True:
            print("The mountainous area has scattered boulders, rocks, and pebbles throughout and ends at a sheer cliff. You walk backwards away from the steep canyon, and bump into a boulder. The boulder shivers and starts to break apart into smaller segments. In a minute, the boulder formed into a human shaped rock cluster. The animate rock then runs towards you.")
            firstRFiend = False
        elif firstRFiend == False:
            print("You come to the rocky clearing and crevice again. The rockfiend is nowhere to be found, hidden as one of the countless boulders. As you walk to grab your fallen axe, the rockfiend reawakens.")
        battle(90, 25, "the Rockfiend")
        if lostBattle == False:
            print("The boulder crumbles further and turns into pebbles. One piece doesn’t fall apart, which is a crystal that shines greyness on everything around it. You pick this up and hope it will be useful.")
            invent.append("Rock Gem")
            if axeCl == True:
                print("You fetch your axe that you lost when you got thrown off the cliff.")
                invent.insert(0, "Axe")
                axeCl = False
        elif lostBattle == True:
            print("The Rockfiend knocks you off the cliff.")
            if axe == False:
                axeCl = True
                print("You lost your axe to the rockfiend!")
            canyon()
            return
        firstTimeCl = False
    elif firstTimeCl == False:
        print("You come to the rocky clearing and crevice again. Rocks are scattered scross the ground still, but who knows which are actual rocks and not moving rocks.")

    askInventory()
    print("You peer down the side of the cliff and see a slow river at the bottom of the canyon. You can also make out several glowing, multicolored dots. To your left is a mountain you can climb. \nWhere do you go? Canyon(1) Mountain(2)")
    locChoi8 = ask(2)
    if locChoi8 == 1:
        canyon()
        return
    elif locChoi8 == 2:
        mountain()
        return
    else:
        print("Something Went Wrong")

def canyon():
    global firstTimeCa, firstTimeT, firstTimeV, firstTimeCl, firstTimeCa, firstTimeM, lostBattle, adventure
    adventure.append( "Canyon -> ")
    if firstTimeCa == True:
        global sight
        sight += 2
        firstTimeCa = False
    
    if lostBattle == False:
        print("You run towards the cliff and jump off.")
    elif lostBattle == True:
        lostBattle = False
    print("____")
    print("    |")
    print("    |")
    print("    |")
    print("You fall into the river and clamber out onto the other side. It is dark and damp down in the canyon but at least you survived.")
    askInventory()
    print("You look around and see ten dots on the canyon wall, a different colored dot glows per terrain you have visited and completed on the island.")
    dots = 0
    for place in adventure:
        if "Beach" in place:
            print("A dot glows gold for the beach.")
            dots += 1
        elif "Plains" in place:
            print("A dot glows light green for the plains.")
            dots += 1
        elif "Desert" in place:
            print("A dot glows plale yellow for the desert.")
            dots += 1
        elif "Forest" in place:
            print("A dot glows dark green for the forest.")
            dots += 1
    if firstTimeT == False:
        print("A dot glows white for the tundra.")
        dots += 1
    if firstTimeCl == False:
        print("A dot glows light grey for the cliff.")
        dots += 1
    if firstTimeCa == False:
        print("A dot glows black for the canyon.")
        dots += 1
    if firstTimeV == False:
        print("A dot glows red for the volcano.")
        dots += 1
    if firstTimeM == False:
        print("A dot glows dark grey for the mountain.")
        dots += 1
    darkDots = 10 - dots
    print(f"{darkDots} dot{'s are' if darkDots > 1 else ' is'} left dark.")
    print("There is one button in the middle of the dots. \nDo you try pressing the button? Yes(1) No(2)")
    canyonChoi = ask(2)
    if canyonChoi == 1:
        eleIncrease = 0
        if dots == 9:
            eleIncrease = 4
        elif dots == 8:
            eleIncrease = 3
        elif dots == 7:
            eleIncrease = 2
        elif dots == 6:
            eleIncrease = 1
        
        elevator = 0
        elevator = random.randint(1, 10) + eleIncrease
        if elevator > 5:
            print("The cliffside starts to shake as a slab of stone comes out of it. You hop on top and it soars to the peak of the cliff. On this side is a field full of flowers.")
            flower(True)
            return
        if elevator <= 5:
            print("The button does nothing, so you follow the river to the top of the mountain.")
            mountain()
            return
    elif canyonChoi == 2:
        print("Instead of pressing the button, you see a inscription on the wall. It writes, 'The more places you have completed, the more likely the button is to work' You then decide to follow along the river till you reach the top of this island’s mountain.")
        mountain()
        return

def flower(early):
    global invent, hpPmax, lostBattle, winGame, ending2, islandRule, adventure
    adventure.append( "Flower Field -> ")
    allPlaces = False
    if len(adventure) >= 10:
        allPlaces = True
    print(f"The humongous field is filled with millions of neon pink flowers. While admiring this beauty, a person walks towards you. As they come closer, you can make out their familiar features. You realize that this is because they have your features. This new, somehow familiar figure unsheaths a striking sapphire sword with a vibrant blue gem at its heart. Its blade shines with blue energy, which seems to {'triple ' if allPlaces == True else 'increase ' if early == True else'double '}the sword’s size. You almost fall unconscious at the complexity of the weapon’s details. What stops you is the fact that this blade is coming straight towards you.")
    ending2 = False
    if allPlaces == True:
        battle(hpPmax, 45, "the Twin", bossBattle = True)
    elif early == True:
        battle(hpPmax, 25, "the Twin", bossBattle = True)
    elif early == False:
        battle(hpPmax, 35, "the Twin", bossBattle = True)
    if lostBattle == False:
        winGame = True
    elif lostBattle == True:
        return
    if ending2 == False:
        print("You defeat your rude twin and show who is truly superior. You acquire their sword, find a clearing in the flowers with a slit in the ground, and insert the sapphire sword. Inside is loads of gold, jewels, and other precious materials. You take these riches and use them to buy the pirate ship from the old captain of the pirate crew. Your crew sets sail, more happy than they have ever been.")
        invent.append("Sapphire Sword")
    elif ending2 == True:
        print("Your twin realizes they lost and asks for forgiveness from you. They aids this with the promise of sharing this island and with treasures untold. \nDo you agree? Yes(1) No(2)")
        endChoi = ask(2)
        if endChoi == 1:
            print("You and your twin come to terms, so you teach each other some tricks, such as magic or pillaging. You and your twin rule this island peacefully, till the end of time.")
            islandRule = True
        elif endChoi == 2:
            print("You leave your twin behind and find treasure underneath the plentiful pink flowers. You use this to join the pirates again and you leave this island, and its problems behind forever, but keep its bountiful rewards.")

def oceanEnd():
    global lostGame
    global adventure
    adventure.append("Ocean")
    print("You climb down and join your piratemates at the ship. They are very disappointed in you for not bringing treasure, but allow you on the ship. They are excited to see the items you did find and hear your adventures. You take one last glance at the beautiful island before the ship sets sail.")
    lostGame = True

if __name__ == "__main__":
    beach()