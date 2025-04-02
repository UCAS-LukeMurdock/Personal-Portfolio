#Luke Murdock, Movie Recommender
import csv

movies = []

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

# Turns the movies in the file into a list of dictionaries where each movie is one dictionary with it's details as values in it
with open("projects/movie_recommender/Movies list.csv", "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0:
            detail_types = row
            continue
        movie = {}
        for detail_index, detail in enumerate(row):
            movie.update({detail_types[detail_index]:row[detail_index]})
        movies.append(movie)

def display(): # Prints all of the movies with all of their details
    print("\nMovies:\n")
    for movie in movies:
        print(f"Title- {movie["Title"]}\nDirector- {movie["Director"]}\nGenre- {movie["Genre"]}\nRating- {movie["Rating"]}\nLength(min)- {movie["Length (min)"]}\nNotable Actors- {movie["Notable Actors"]}\n")

def recommend(): # Asks for 2 filters and then prints movies that fit both filters
    types = ["Genre", "Director", "Rating", "Notable Actors"]
    results = []
    print("\nFilter Options: Genre(1) Director(2) Rating(3) Notable Actors(4)")
    filter_1 = num_input("\nFirst Filter Type: ", 4) -1
    search_1 = input("Filter Word: ").lower().strip()
    filter_2 = num_input("Second Filter Type: ", 4) -1
    search_2 = input("Filter Word: ").lower().strip()

    for movie in movies:
        if filter_1 == 2: # Checks if user picked Rating or not then searches depending on that
            if search_1 == movie["Rating"].lower() and search_2 in str(movie[types[filter_2]]).lower():
                results.append(movie)
        elif filter_2 == 2:
            if search_2 == movie["Rating"].lower() and search_1 in str(movie[types[filter_1]]).lower():
                results.append(movie)
        elif search_1 in str(movie[types[filter_1]]).lower() and search_2 in str(movie[types[filter_2]]).lower():
            results.append(movie)
    print("\nSearch Results:\n")
    if results == []:
        print("None\n")
    else:
        for result in results:
            print(f"Title- {result["Title"]}\nDirector- {result["Director"]}\nGenre- {result["Genre"]}\nRating- {result["Rating"]}\nLength(min)- {result["Length (min)"]}\nNotable Actors- {result["Notable Actors"]}\n")

def main(): # Introduces the program and then lets the user choose one of the options
    print("Welcome, this is a program with 105 movies which can be displayed or recommended")
    while True:
        choice = num_input("Display(1) Recommend(2) Exit(3)\n", 3)
        if choice == 1:
            display()
        elif choice == 2:
            recommend()
        elif choice == 3:
            print("Come Back Soon!")
            break
        else:
            print("Something Broke!")

if __name__ == "__main__":
    main()