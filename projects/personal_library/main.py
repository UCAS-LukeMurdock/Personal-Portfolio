# Luke Murdock, Updated Personal Library

books = [
    {
        "title": "Fablehaven",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 2
    },
    {
        "title": "Dragonwatch",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 5,
        "times read": 1
    },
    {
        "title": "Five Kingdoms",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 5,
        "times read": 2
    },
    {
        "title": "Beyonders",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 1
    },
    {
        "title": "Michael Vey",
        "author": "Richard Paul Evans",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 1
    },
    {
        "title": "Rick Riordan",
        "author": "Brandon Mull",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 1
    },
    {
        "title": "Leven Thumps",
        "author": "Obert Skye",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 0
    },
    {
        "title": "Wings of Fire",
        "author": "Tui T. Sutherland",
        "genre": "Fantasy",
        "stars": 4,
        "times read": 3
    },
    {
        "title": "The Stormlight Archive",
        "author": "Brandon Sanderson",
        "genre": "Fantasy",
        "stars": 5,
        "times read": 1
    },
    {
        "title": "Refugee",
        "author": "Alan Gratz",
        "genre": "Historical Fiction",
        "stars": 3,
        "times read": 1
    },
]

def num_input(prompt, range = 0, data_type = "int"): # Checks and solves errors in int and float inputs (Has Range If Needed)
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

def simple_display(): # Displays the Titles and Authors of the Library
    print("\nLibrary:")
    for book in books:
        print(f"\nTitle- {book['title']}\nAuthor- {book['author']}")

def display_all(list_displayed): # Displays All of the Information from a given list of dictionaries
    for book in list_displayed:
        print(f"\nTitle- {book['title']}\nAuthor- {book['author']}\nGenre- {book['genre']}\nRating- {book['stars']}/5\nTimes Read- {book['times read']}")

def search(): # This function searchs for the user's search prompt inside of the books in the list and prints them
    search_results = []
    search_word = input("Search: ").upper()

    for book in books:
        if search_word in book["title"].upper() or search_word in book["author"].upper() or search_word in book["genre"].upper() or search_word in str(book["stars"]) or search_word in str(book["times read"]):
            search_results.append(book)
    print("\nSearch Results:")
    display_all(search_results)

def add(): # This funciton adds the user's desired book and information to the library list as a dictionary
    title = input("Title of The Book You Want Added: ")
    author = input("Author of The Book You Want Added: ")
    genre = input("Genre of The Book You Want Added: ")
    stars = num_input("Rating out of 5 Stars for The Book You Want Added: ", 5)
    while True:
        times_read = num_input("The Amount of Times You Have Read The Book You Want Added: ")
        if times_read < 0:
            print("Not In Range")
            continue
        elif times_read >= 0:
            break

    add_book = {
        "title": title,
        "author": author,
        "genre": genre,
        "stars": stars,
        "times read": times_read}
    
    books.append(add_book)
    print("Successfuly Added")

def remove(): # This function removes the user's desired book from the list, if it's in the list
    while True:
        book_found = False
        book_title = input("Title of Book You Want Removed (Exit[0]): ").upper()
        for book in books:
            if book_title == book["title"].upper():
                found_book = book
                book_found = True
        if book_title == '0':
            break
        elif book_found == False:
            print("Book Not In Library")
            continue
        elif book_found == True:
            books.remove(found_book)
            print("Successfuly Removed")
            break

def edit_search(): # This function lets the user select a book that they would like to edit and prints it
    while True:
        book_found = False
        book_title = input("Title of Book You Want Edited (Exit[0]): ").upper()
        for book_ind, book in enumerate(books):
            if book_title == book["title"].upper():
                found_book = book
                book_found = True
                found_ind = book_ind
        if book_title == '0':
            break
        elif book_found == False:
            print("Book Not In Library")
            continue
        elif book_found == True:
            print(f"\nBook:\nTitle- {found_book['title']}\nAuthor- {found_book['author']}\nGenre- {found_book['genre']}\nRating- {found_book['stars']}/5\nTimes Read- {found_book['times read']}\n")
            edit(found_ind)
        break

def edit(found_ind): # This function lets the user change any of the details for their selected book from the edit_search() function
        types = ["title", "author", "genre", "stars", "times read"]
        info_type = num_input("What detail do you want to edit?:\nTitle(1) Author(2) Genre(3) Rating(4) Times Read(5) Exit(6)\n", 6)
        if info_type <= 3:
            new = input("New Text: ")
        elif info_type == 4:
            new = num_input("New Rating: ", 5)
        elif info_type == 5:
            while True:
                new = num_input("New Number: ")
                if new < 0:
                    print("Not In Range")
                    continue
                elif new >= 0:
                    break
        elif info_type == 6:
            return
        books[found_ind][types[info_type -1]] = new
        print("Successfuly Edited")
        return

def main(): # This funcion welcomes the user, then lets the user choose what they want to do with the library list
    print("Welcome to my library, where you can see, add, remove, or search through it.")
    while True:
        choice = num_input("\nSimple Display(1) Display All(2) Search(3) Add(4) Remove(5) Edit(6) Exit(7)\n", 7)

        if choice == 1:
            simple_display()
        elif choice == 2:
            print("\nLibrary:")
            display_all(books)
        elif choice == 3:
            search()
        elif choice == 4:
            add()
        elif choice == 5:
            remove()
        elif choice == 6:
            edit_search()
        elif choice == 7:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke")
            continue

if __name__ == "__main__":
    main()