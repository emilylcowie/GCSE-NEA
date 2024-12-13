import random
import csv

class Make_cards:

    def open_file(self):
        with open('Top-Dog/dogs.txt', 'r') as file:
            dogs = file.read().splitlines()
        return dogs

    def make_cards(self, dog):
        return {
            'exercise': random.randint(1, 5),
            'intelligence': random.randint(1, 100),
            'friendliness': random.randint(1, 10),
            'drool': random.randint(1, 10)
        }

    def combine_dogs(self, dogs):
        dogcards = {}
        for dog in dogs:
            dogcards[dog] = self.make_cards(dog)
        return dogcards

    def save(self, toptrumps):
        with open('Top-Dog/TopTrumps.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Dog', 'Exercise', 'Intelligence', 'Friendliness', 'Drool'])
            for dog, stats in toptrumps.items():
                writer.writerow([dog, stats['exercise'], stats['intelligence'], stats['friendliness'], stats['drool']])

    def read_file(self):
        with open('Top-Dog/TopTrumps.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)

    def run_class(self):
        dogs = self.open_file()  
        toptrumps = self.combine_dogs(dogs)
        self.save(toptrumps)  


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
    while True:
        try:
            num_cards = int(input(''' 
How many cards do you want to be played?
(Number must be >3, <31 and an even number)\n'''))

            if num_cards <= 3 or num_cards >= 31 or num_cards % 2 != 0:
                raise ValueError("Please enter a valid number")
            else:
                break
        except ValueError as e:
            print(f"Error: {e}\n")

    game = Make_cards()
    game.read_file() 

game = Make_cards()
game.run_class()