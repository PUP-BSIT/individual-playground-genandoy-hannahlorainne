def list_all_movies(movie_dict):
    if not movie_dict:
        print("No movies available.")
    else:
        print("\nMovies:")
        for title, details in movie_dict.items():
            print(f"Title: {title}")
            if not details:
                print("  No details available.")
            else:
                for key, value in details.items():
                    print(f"  {key}: {value}")
            print()