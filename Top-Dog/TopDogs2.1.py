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

        return [(dog, self.make_cards(dog)) for dog in dogs]

    def save(self, toptrumps):
        with open('Top-Dog/TopTrumps.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ['Dog', 'Exercise', 'Intelligence', 'Friendliness', 'Drool'])
            for dog, stats in toptrumps:
                writer.writerow(
                    [dog, stats['exercise'], stats['intelligence'], stats['friendliness'], stats['drool']])

    def read_file(self):
        with open('Top-Dog/TopTrumps.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            cards = [row for row in csv_reader if row and row[0]
                     != 'Dog']
        return cards

    def run_class(self):
        dogs = self.open_file()  
        toptrumps = self.combine_dogs(dogs)  
        self.save(toptrumps) 


class UserInterface:

    def menu(self):
        while True:
            choice = int(input(''' 
    Welcome, here are your options, please select a number:
        1. Play game
        2. Quit \n\n'''))

            if choice == 1:
                self.play()
            elif choice == 2:
                exit('Au revoir!')
            else:
                print('Invalid input, try again.')

    def play(self):
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

        return num_cards

    def make_decks(self):

        number = self.play()

        game = Make_cards()

        cards = game.read_file()

        random.shuffle(cards)

        player_deck = cards[:number // 2]
        computer_deck = cards[number // 2:number]

        print(f"Player Deck: {player_deck}")
        print(f"Computer Deck: {computer_deck}")


run_game = UserInterface()
run_game.make_decks()
