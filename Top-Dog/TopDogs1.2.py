import random

# Read the file and assume each line is a dog name or entry
with open('Top-Dog/dogs.txt', 'r') as file:
    dogs = file.read().splitlines()

# Function to create cards for each dog
def make_cards(dog):
    return {
        'exercise': random.randint(1, 5),
        'intelligence': random.randint(1, 100),
        'friendliness': random.randint(1, 10),
        'drool': random.randint(1, 10)
    }

# Combine the dogs into a dictionary with dog names as keys and card values
def combine_dogs(dogs):
    dogcards = {}
    for dog in dogs:
        dogcards[dog] = make_cards(dog)
    return dogcards

# Print the combined dogcards
print(combine_dogs(dogs))
