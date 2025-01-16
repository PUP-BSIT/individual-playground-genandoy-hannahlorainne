# Initialize movies as a list of dictionaries
movies = [
    {
        "Title": "Portrait of a Lady on Fire", 
        "Director": "Céline Sciamma", 
        "Release Date": "September 18, 2019", 
        "Genre": "Historical Drama", 
        "Language": "French"
    }
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
    if not movies:
        print("No movies available.")
    else:
        print("\nList of Movies:")
        for movie in movies:
            for key, value in movie.items():
                print(f"{key}: {value}")
            print("\n---")
        
def add_movie():
    title = input("Enter film title: ")
    director = input("Enter film director: ")
    release_date = input("Enter film release date: ")
    genre = input("Enter film genre: ")
    language = input("Enter film language: ")

    new_movie = {
        "Title": title,
        "Director": director,
        "Release Date": release_date,
        "Genre": genre,
        "Language": language,
    }

    movies.append(new_movie)
    print("Film added successfully!\n")

def update_movie():
    title = input("Enter the title of the movie to update: ")
    for movie in movies:
        if movie["Title"].lower() == title.lower():
            # Prompt to update each attribute
            new_title = input("Enter new title (leave blank to keep current): ")
            if new_title:
                movie["Title"] = new_title

            new_director = input("Enter new director (leave blank to keep current): ")
            if new_director:
                movie["Director"] = new_director

            new_release_date = input("Enter new release date (leave blank to keep current): ")
            if new_release_date:
                movie["Release Date"] = new_release_date

            new_genre = input("Enter new genre (leave blank to keep current): ")
            if new_genre:
                movie["Genre"] = new_genre

            new_language = input("Enter new language (leave blank to keep current): ")
            if new_language:
                movie["Language"] = new_language

            print("Movie updated successfully.")
            return
    print("Movie not found.")

def delete_movie():
    title_to_delete = input("Enter the title of the movie to delete: ")
    found = False

    for movie in movies:
        if movie["Title"].lower() == title_to_delete.lower():
            movies.remove(movie)
            found = True
            print(f"'{title_to_delete}' has been deleted.")
            break

    if not found:
        print(f"No movie found with the title '{title_to_delete}'.")

def search_movie():
    search_term = input("Enter the Movie title to search: ")
    found_movies = [movie for movie in movies if search_term.lower() in movie['Title'].lower()]
    
    if found_movies:
        print("\nSearch Results:")
        for movie in found_movies:
            print(f"Title: {movie['Title']}, "
                  f"Director: {movie['Director']}, "
                  f"Release Date: {movie['Release Date']}, "
                  f"Genre: {movie['Genre']}, "
                  f"Language: {movie['Language']}")
    else:
        print("No movies found.")

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
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
