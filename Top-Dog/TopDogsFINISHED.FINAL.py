import random
import csv
import time
import sys


class MakeCards:

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
            cards = [row for row in csv_reader if row and row[0] != 'Dog']
        return cards

    def run_class(self):
        dogs = self.open_file()
        toptrumps = self.combine_dogs(dogs)
        self.save(toptrumps)


class UserInterface:

    def menu(self):
        while True:
            choice = int(self.character_print(''' 
    Welcome, here are your options, please select a number:
        1. Play game
        2. Quit 
    \n\n'''))

            if choice == 1:
                self.play()
            elif choice == 2:
                exit('Au revoir!')
            else:
                self.character_print('Invalid input, try again.')

    def intro(self):
        while True:
            try:
                num_cards = int(self.character_print(''' 
    How many cards do you want to be played? (Number must be >3, <31, and even)\n'''))

                if num_cards <= 3 or num_cards >= 31 or num_cards % 2 != 0:
                    raise ValueError("Please enter a valid number")
                else:
                    break
            except ValueError as e:
                self.character_print(f"Error: {e}\n")

        return num_cards

    def make_decks(self):
        number = self.intro()
        game = MakeCards()
        cards = game.read_file()
        random.shuffle(cards)

        player_deck = cards[:number // 2]
        computer_deck = cards[number // 2:number]

        return player_deck, computer_deck

    def play(self):
        player_deck, computer_deck = self.make_decks()
        categories = ['exercise', 'intelligence', 'friendliness', 'drool']

        while True:
            try:
                player_card = player_deck.pop(0)
                computer_card = computer_deck.pop(0)
            except IndexError:
                if len(computer_deck) == 0:
                    self.character_print("You Win!!!!")
                elif len(player_deck) == 0:
                    self.character_print("The computer wins!!!")
                if str(self.character_print("Return to menu? y/n\n")) == 'y':
                    self.menu()
                else:
                    exit("Au Revoir")

            self.character_print(f"\nYour card:\n{player_card}")

            while True:
                try:
                    category = self.character_print(
                        "\nChoose your category (exercise, intelligence, friendliness, drool): ").lower()
                    if category not in categories:
                        raise ValueError("Please enter a valid category")
                    else:
                        self.compare(category, player_card, computer_card,
                                     player_deck, computer_deck, categories)
                        break
                except ValueError as e:
                    self.character_print(e)

    def compare(self, category, player_card, computer_card, player_deck, computer_deck, categories):
        category_index = categories.index(category) + 1

        player_value = int(player_card[category_index])
        computer_value = int(computer_card[category_index])

        self.character_print(f"\nYour card:\n{player_card}")
        self.character_print(f"\nComputer's card:\n{computer_card}")

        self.character_print(f"\nComparing category '{category}'...")

        self.character_print(f"Your card's {category}: {player_value}")
        self.character_print(f"Computer's card's {category}: {computer_value}")

        if player_value > computer_value:
            self.character_print("You win this round!")
            player_deck.append(player_card)
            player_deck.append(computer_card)
        elif player_value < computer_value:
            self.character_print("Computer wins this round!")
            computer_deck.append(player_card)
            computer_deck.append(computer_card)
            category = self.computer_choice(categories)
            self.compare(category, player_card, computer_card,
                         player_deck, computer_deck, categories)
            return
        else:
            self.character_print("It's a tie! No cards are won.")
            player_deck.append(player_card)
            computer_deck.append(computer_card)

        print(f"\nYou now have {len(player_deck)} card(s)")
        print(f"The computer now has {len(computer_deck)} card(s)")

        if not player_deck:
            self.character_print("Game Over! You lose.")
        elif not computer_deck:
            self.character_print("Game Over! You win.")

    def computer_choice(self, categories):
        return random.choice(categories)

    def character_print(self, info):
        for char in info:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.010)
        return input()


run_game = UserInterface()
run_game.menu()
