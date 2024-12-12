import random

class Make_cards:

    def open_file():
        with open('Top-Dog/dogs.txt', 'r') as file:
            dogs = file.read().splitlines()
        return dogs

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
            dogcards[dog] = Make_cards.make_cards(dog)
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

    def run_class():
        dogs = Make_cards.open_file
        toptrumps = Make_cards.combine_dogs(dogs)
        Make_cards.save(toptrumps)

Make_cards.run_class

def menu():
    while True:
        choice = int(input('''
    Welcome, here are your options, please select a number:
        1. Play game
        2. Quit \n\n'''))

        if choice == 1:
            play()
        elif choice == 2:
            exit('Au revoir!')
        else:
            print('Invalid input, try again.')

def play():
    num_cards = int(input('''
    How many cards do you want to be played?
    (Number must be >3, <31 and an even nummber)'''))
    dogs = str(Make_cards.run_class)
    for i in dogs:
        print(i)

menu()