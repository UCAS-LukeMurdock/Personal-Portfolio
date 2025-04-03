# Luke Murdock, Personal Portfolio

from projects import to_do_list, random_password_generator as password_gen, personal_library, movie_recommender as movie, financial_calculator as fin_calc, final_text_advent as final, battle_simulator, music_festival, high_score_tracker

def menu(): # Introduces the program and then lets the user choose one of the programs
    print("\033c",end="")
    print("Welcome to my Personal Portfolio, where you can see descriptions of and use/play python programs that I have made and helped make during mainly my Programming 2 class at UCAS.") # What it is
    print("To use this program, just type the number that corresponds to the program you want to run, then you will see a description of it and its creation, where you can decide if you want to run the program or not. If you decide to use the program, you will run it until it is done, and then you can choose another one or exit this Portfolio.") # How to use it
    while True:
        choice = input("\n\n\nWhich program do you want to use?\n1. High Score Tracker\n2. Music Festival Management\n3. Battle Simulator\n4. Random Password Generator\n5. Movie Recommender\n6. Personal Library\n7. To Do List\n8. Financial Calculator\n9. Text Based Adventure (Final for Programming 1)\n10. Exit this Program\nChoice: ")
        if choice == "1":
            start = input("""
High Score Tracker
Description:
    This project lets the user play one of three games and then it saves their high score on their profile. The games you can play are all pretty simple but two have graphics. The first two are reflex games, where you get points if you can click the blinking screen or box in time. The last game is a basic number guessing game. This program also lets the user see the high score board or look at profiles. It was pretty fun creating this program, since it wasn’t too big, other than the three games inside of it. Since the games weren’t too complicated, the only hard part was the logic behind saving profiles and sorting them. This was the second group project I did for my class, so we were still pretty unfamiliar with how to program together efficiently. Additionally, I was the Senior Programmer for this project, and I learned how to help my team members, organize group communication, and make compromises. In terms of actual programming, I learned how to use files and dictionaries better.

Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            high_score_tracker.main()
        elif choice == "2":
            start = input("""
Music Festival Management
Description:
    This project lets the user manage a music festival by organizing artists, venues, tickets, and time slots. Its main focus is using different types of lists, so it doesn’t save information from one run to the next. Also, it isn’t the most cohesive program ever, since it was the first group project I was a part of. It wasn’t too hard for me to code this project because I was familiar with manipulating lists. I didn't know anyone in my group that well, which decreased my enjoyment when working on the project. This project taught me the basics of how to code as a group and understand different types of lists. I wasn’t given  a role for this group project, but I was probably closest to being the UI/UX Designer. You can log in as an admin by entering the password: Admin123.
    
Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            music_festival.main()
        elif choice == "3":
            start = input("""
Battle Simulator
Description:
    This battle simulator program lets you create RPG characters using generated ideas for inspiration, by fully generating characters, or by completely creating them yourself. Once your characters are finished being created, their stats can be displayed and compared through graphs, they can fight each other (with the user and the program each controlling one), and you can use the money you get from battling to shop as a character for items that they can then use in future battles. I found figuring out how to use libraries a bit annoying, and I still don't understand them too well. It also took me a long time to finish this project, which wasn’t too fun. Though, creating this program did teach me how to use inner and helper functions, and I also learned how to use a few libraries decently well, which is nice.

Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            battle_simulator.main()
        elif choice == "4":
            start = input("""
Random Password Generator
Description:
    This program lets a user decide what requirements to put on the password generator. These requirements include if the password contains upper case, lower case, or special characters, if it has numbers in it, and last of all, how long it is. The generator will then print out 4 randomly generated passwords they could use that fit their requirements. I found it pretty tricky to get the different password requirements to work in tandem, but it wasn't too bad. Creating the password from those requirements was also hard for me to get working. Overall, it was a nice, simple program to work on, where I learned how ascii characters work a little more, along with some other minor things about passwords and characters.

Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            password_gen.main()
        elif choice == "5":
            start = input("""
Movie Recommender
Description:
    This project uses a csv file with around a hundred movies and their details in it. The program reads this file and then displays the long list of movies by either displaying all of them at once or just the ones recommended through two filters. These filters are both set by the user deciding what to filter from a couple of the movie details. I found it decently fun to be able to manipulate so much data, but it was still hard for me at first to understand dictionaries, even though this was the second time I had to use them. I learned about how to use csv files which weren't too bad but I still don't understand the intricacies of manipulating files.

Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            movie.main()
        elif choice == "6":
            start = input("""
Personal Library
Description:
    This project lets you manipulate a preset library that I have created. The library consists of a list made up of dictionaries, each dictionary being a book with information on it. You can display all of the books either with or without their details, search through the library for specific books, add new books to the library with their details, remove books, or edit a book's details. This project is an updated version of the first version I created, which used a list of book titles for the library, but now it uses dictionaries instead of just titles. I disliked having to go back and change a month-old program but it was good practice for maintaining future projects. The creation process of this program wasn't terrible but I do like lists a little bit better than dictionaries sometimes, especially at the time when I was creating this project. This program taught me how to use dictionaries but it still took me a while to understand them. After a few more projects, I now feel like I can confidently use dictionaries.

Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            personal_library.main()
        elif choice == "7":
            start = input("""
To-do List
Description:
    This project lets you create a to-do list with tasks, and then it lets you check specific tasks off or uncheck them. You can also delete a task off of the list when you are done with it. You can create more tasks as needed whenever you want to. I enjoyed this project because I like to-do lists, and it wasn't too hard since it used dictionaries and a file. While creating this program, I learned how to write a list of dictionaries to a file and how to read a file in a way that creates a list of dictionaries, which is what I have been doing ever since. This is one of the first times I used a txt file, so it gave me experience in using them.

Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            to_do_list.main()
        elif choice == "8":
            start = input("""
Financial Calculator
Description:
    This project lets the user simulate and see the outcome of basic financial situations, such as allocating a budget, tipping, finding the sale price, calculating compound interest, and tracking a savings goal. I wasn't too familiar with some of these financial situations, which made it harder to figure out how to do the needed math, but other than that, coding this project wasn't too bad. I learned more about finances and how to calculate things in python. This project taught how to create functions for each section of code, which is also known as functional decomposition.

Click Enter to Start Program or 0 to go to Main Menu\n""")
            if start == '0':
                continue
            fin_calc.main()
        elif choice == "9":
            start = input("""
Text-based Adventure  (This is the oldest of these projects)
Description:
    This project lets you play a text-based adventure about a pirate who gets left on a diverse-terrained island to find treasure. The character only has the axe he owns and the sword he finds on the island. This program is probably the biggest program I have ever made by myself. The character has an inventory that they can use in battles along the way, they have stats that also affect battling, they have innate abilities such as focusing and dodging during battle, and through solving puzzles and fighting a variety of creatures, including the boss, the player can uncover some lore and backstory to this island. I found this program very fun, though very time-consuming. I spent a lot of time during a school break coding and refining it. Creating this program taught me how to how to make a battling system, have a working inventory, and create a large program.

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