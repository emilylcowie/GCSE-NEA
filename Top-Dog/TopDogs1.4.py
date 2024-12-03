import random

with open('Top-Dog/dogs.txt', 'r') as file:
    dogs = file.read().splitlines()

def make_cards(dog):
    return {
        'exercise': random.randint(1, 5),
        'intelligence': random.randint(1, 100),
        'friendliness': random.randint(1, 10),
        'drool': random.randint(1, 10)
    }

def combine_dogs(dogs):
    dogcards = {}
    for dog in dogs:
        dogcards[dog] = make_cards(dog)
    return dogcards

def save(toptrumps):
    with open('Top-Dog/TopTrumps.txt', "w") as file:
        for dog, stats in toptrumps.items():
            file.write(f"{dog}:\n")
            for stat, value in stats.items():
                file.write(f"  {stat}: {value}\n")
            file.write("\n")

def read_file():
    with open('Top-Dog/TopTrumps.txt', "r") as file:
        file_content = file.read()
    print(file_content)

save(combine_dogs(dogs))
read_file()

