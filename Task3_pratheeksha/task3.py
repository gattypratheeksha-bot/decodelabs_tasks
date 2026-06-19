movies = {
    "Action": ["Avengers", "John Wick", "Mission Impossible"],
    "Comedy": ["Mr. Bean", "The Mask", "Home Alone"],
    "Science Fiction": ["Interstellar", "Avatar", "The Martian"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"]
}

print("Available Categories:")
for category in movies:
    print("-", category)

user_choice = input("\nEnter your favorite category: ")

if user_choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[user_choice]:
        print("-", movie)
else:
    print("Sorry! Category not found.")
