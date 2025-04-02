# Luke Murdock, Personal Portfolio

from projects import to_do_list, random_password_generator as password_gen, personal_library, movie_recommender as movie, financial_calculator as fin_calc, final_text_advent as final, battle_simulator, music_festival, high_score_tracker

def menu(): # Introduces the program and then lets the user choose one of the programs
    print("\033c",end="")
    print("Welcome to my Personal Portfolio, where you can see descriptions of and use/play programs that I have made and helped make.") # What it is
    print("To use this program, just type the number that corresponds to the program you want to run, then you will see a description of it and its creation, where you can decide if you want to run the program or not. If you decide to use the program, you will run it until it is done, and then you can choose another one or exit this Portfolio.") # How to use it
    while True:
        choice = input("\n\n\nWhich program do you want to use?\n1. High Score Tracker\n2. Music Festival Management\n3. Battle Simulator\n4. Random Password Generator\n5. Movie Recommender\n6. Personal Library\n7. To Do List\n8. Financial Calculator\n9. Text Based Adventure (Final for Programming 1)\n10. Exit this Program\nChoice: ")
        if choice == "1":
            start = input("""
Description:
    What the project does- 
        This project lets the user play one of three games and then save their high score on their profile. They can also see the high score board or look at profiles. 
    How I found the process- 
        I felt pretty good during the creation of this program since we all didn't have too much stuff we needed to accomplish. I still wasn't used to working in a team though.
    What I learned- 
        I learned how to help team members, organize group communicaiton, and make compromises while makinh this project. On the coding side of things, I learned how to use files and dictionaries better.
    My role- Senior Developer
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            high_score_tracker.main()
        elif choice == "2":
            start = input("""
Description:  (The password for admin is 'Admin123') 
    What the project does- 
        This project lets one manage a music festival by organizing artists, venues, tickets, and time slots.
    How I found the process- 
        I felt pretty good coding the project since it wasn't too unfamiliar to manipulate lists. I didn't know anyone in my group, though.
    What I learned- 
        I learned the basics of how to code as a group and understand different types of lists. 
    My role- UI/UX Desginer (We didn't really decide roles in my first group, so I picked this one since I haven't done this role yet)
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            music_festival.main()
        elif choice == "3":
            start = input("""
Description:
    What the project does- 
        The battle simulator lets you create characters by making them with generate ideas or with generated characters so then their stats can be displayed, they can fight other created characters, and so they can shop to get items for battle.
    How I found the process-
        I found it kind of annoying to have to figure out how to use libraries and still don't understand them the best. It also took me a long time to finish the project.
    What I learned- 
        I learned how to use inner and helper functions, and also I learned how to use a few libraries decently well.
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            battle_simulator.main()
        elif choice == "4":
            start = input("""
Description:
    What the project does- 
        This program lets a user decide what requirements to put on the generator. It will then print out 4 passwords they could use that fit their requirements.
    How I found the process- 
        I found it pretty tricky to get the requirements to work but it wasn't too bad.
    What I learned- 
        I learned how ascii characters work a little more a long with some other things that have to do with passwords and characters.
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            password_gen.main()
        elif choice == "5":
            start = input("""
Description:
    What the project does- 
        This project lets you look through a long list of movies by either displaying all of them or just the ones recommended through two filters. 
    How I found the process- 
        I found it decently fun to be able to manipulate so much data but it was still hard for me at first to understand dictionaries even though this was the second time we used them.
    What I learned- 
        I learned about how to use csv files which weren't too bad but I still don't understand their intracacies. 
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            movie.main()
        elif choice == "6":
            start = input("""
Description:
    What the project does- 
        This project lets you manipulate a list of dictionaries, each being a book with information on it. 
    How I found the process- 
        I disliked having to go back and change month-old code but it was good practice for future projects. It wasn't terrible but I do like lists a little bit better than dictionaries sometimes.
    What I learned- 
        This project is an updated version of the first version which used a list for the library but now it also uses dictionaries. This helped teach me how to use dictionaries but I still didn't fully understand them until like the second or third group project. 
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            personal_library.main()
        elif choice == "7":
            start = input("""
Description:
    What the project does- 
        This project lets you create a to-do list and then check things off the list or uncheck them. You can also delete a task off of it.
    How I found the process- 
        I enjoyed this project because I like to-do lists and it wasn't too hard with dictionaries and a file.
    What I learned- 
        I learned how to write to a file so then it creates a list of dictionaries which is what I have been doing ever since.
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            to_do_list.main()
        elif choice == "8":
            start = input("""
Description:
    What the project does- 
        This project lets someone simulate and show the outcome of basic financial situations, such as allocating a budget, tipping, finding the sale price, calculating compound interest, and having a savings goal.
    How I found the process- 
        I wasn't too familar with some of these financial situations, which made it harder to figure out how to do the needed math, but other than that it wasn't too bad.
    What I learned- 
        I learned more about finances and how to calculate things in python. This project taught how to create functions for each section of code also known as functional decomposition.
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            fin_calc.main()
        elif choice == "9":
            start = input("""
Description:  (This is the oldest of all of the projects on this portfolio.)
    What the project does- 
        This project lets you play a text-based adventure about a pirate who gets left on a diverse island to find treasure.
    How I found the process- 
        I found this program very fun, though very time-consuming. I spent a decent amount of Thanksgiving Break coding and refining it.
    What I learned- 
        I learned how to do a battling system, have an inventory, and create a big program.
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            final.beach()
        elif choice == "10":
            print("\n\nCome Back Soon!\n\n")
            break
        else:
            print("\nInvalid Input (Insert an Integer in the Range)")
menu()