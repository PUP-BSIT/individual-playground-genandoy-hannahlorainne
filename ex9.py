# List of movies.
movies = [
    {"Title": "Portrait of a Lady on Fire", 
     "Director": "Céline Sciamma", 
     "Release date": "September 18, 2019", 
     "Genre": "Historical Drama", 
     "Language": "French"},
     
    # Placeholder entries for adding more movie records
    {"Title": "", "Director": "", "Release date": "", "Genre": "", "Language": ""},
    {"Title": "", "Director": "", "Release date": "", "Genre": "", "Language": ""},
    {"Title": "", "Director": "", "Release date": "", "Genre": "", "Language": ""},
    {"Title": "", "Director": "", "Release date": "", "Genre": "", "Language": ""},
]

# Main menu function
def show_menu():
    print("\n----- Netflix Movies Recommendations -----")
    print("1. List All Movies")
    print("2. Add a Movie")
    print("3. Update a Movie")
    print("4. Delete a Movie")
    print("5. Search for a Movie")
    print("6. Exit")

# Function to list all movies
def list_all_movies():
    # TODO: Clarence - Implement function to list all movies
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['Title']} - {movie['Director']} - {movie['Release date']} - {movie['Genre']} - {movie['Language']}")

# Function to add a movie
def add_movie():
    # TODO: Mejares - Implement function to add a new movie
    title = input("Enter title: ")
    director = input("Enter director: ")
    release_date = input("Enter release date: ")
    genre = input("Enter genre: ")
    language = input("Enter language: ")
    movies.append({"Title": title, "Director": director, "Release date": release_date, "Genre": genre, "Language": language})
    print("Movie added successfully.")

# Function to update a movie
def update_movie():
    # TODO: Uy - Implement function to update an existing movie
    index = int(input("Enter the movie number to update: ")) - 1
    if 0 <= index < len(movies):
        movies[index]['Title'] = input("Enter new title: ")
        movies[index]['Director'] = input("Enter new director: ")
        movies[index]['Release date'] = input("Enter new release date: ")
        movies[index]['Genre'] = input("Enter new genre: ")
        movies[index]['Language'] = input("Enter new language: ")
        print("Movie updated successfully.")
    else:
        print("Invalid movie number.")

# Function to delete a movie
def delete_movie():
    # TODO: Hannah - Implement function to delete a movie
    index = int(input("Enter the movie number to delete: ")) - 1
    if 0 <= index < len(movies):
        deleted_movie = movies.pop(index)
        print(f"Deleted movie: {deleted_movie['Title']}")
    else:
        print("Invalid movie number.")

# Function to search for a movie
def search_movie():
    # TODO: Krislyn - Implement function to search for a movie by title
    title = input("Enter movie title to search: ").lower()
    results = [movie for movie in movies if title in movie["Title"].lower()]
    if results:
        for movie in results:
            print(f"{movie['Title']} - {movie['Director']} - {movie['Release date']} - {movie['Genre']} - {movie['Language']}")
    else:
        print("No movies found with that title.")

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            list_all_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            update_movie()
        elif choice == "4":
            delete_movie()
        elif choice == "5":
            search_movie()
        elif choice == "6":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()
