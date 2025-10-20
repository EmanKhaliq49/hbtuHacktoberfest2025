import random
import sys

# Define the movies grouped by genre using a dictionary.
# Keys are the genre numbers, and values are another dictionary holding the name and the list of movies.
MOVIE_DATA = {
    1: {"name": "Action", "movies": [
        "The Dark Knight",
        "Mad Max: Fury Road",
        "Inception",
        "Mission: Impossible - Fallout",
        "Dredd"
    ]},
    2: {"name": "Comedy", "movies": [
        "Monty Python and the Holy Grail",
        "Superbad",
        "Airplane!",
        "Shaun of the Dead",
        "The Princess Bride"
    ]},
    3: {"name": "Horror", "movies": [
        "The Exorcist",
        "Hereditary",
        "Psycho",
        "Get Out",
        "A Quiet Place"
    ]},
    4: {"name": "Sci-Fi", "movies": [
        "Dune",
        "Blade Runner 2049",
        "2001: A Space Odyssey",
        "Interstellar",
        "Arrival"
    ]}
}

def display_menu():
    """Prints the genre selection menu."""
    print("-" * 35)
    print("Welcome to the Python Movie Suggester!")
    print("-" * 35)
    print("Please choose a genre by entering the corresponding number:")
    
    # Iterate through the dictionary to display the choices
    for num, genre_info in MOVIE_DATA.items():
        print(f"{num}. {genre_info['name']}")
    
    print("\nTo exit the program, enter 'q'.")
    print("-" * 35)

def get_suggestion(choice):
    """
    Randomly selects and prints a movie based on the user's choice.
    :param choice: The integer corresponding to the genre.
    """
    genre_info = MOVIE_DATA.get(choice)
    
    if genre_info:
        genre_name = genre_info["name"]
        movie_list = genre_info["movies"]
        
        # Use random.choice() for simple, clean random selection
        suggested_movie = random.choice(movie_list)
        
        print("\n" + "=" * 40)
        print(f"Suggestion for the {genre_name} genre:")
        print(f"🍿 We recommend: {suggested_movie}")
        print("=" * 40 + "\n")
    else:
        # This case handles non-existent numbers that aren't q
        print("\nInvalid choice. Please enter a number between 1 and 4, or 'q' to quit.")

def main():
    """Main function to run the movie suggester loop."""
    while True:
        display_menu()
        
        user_input = input("Enter your choice: ").strip().lower()
        
        if user_input == 'q':
            print("\nThanks for using the Movie Suggester. Goodbye!")
            sys.exit(0) # Exit the program gracefully
        
        try:
            choice = int(user_input)
            get_suggestion(choice)
        except ValueError:
            print("\nInvalid input. Please enter a valid number (1-4) or 'q'.")

if __name__ == "__main__":
    main()
