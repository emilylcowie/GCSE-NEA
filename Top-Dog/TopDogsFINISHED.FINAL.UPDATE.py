import random
import csv
import time
import sys


class FileHandler:
    @staticmethod
    def read_txt(file_path):
        with open(file_path, 'r') as file:
            return file.read().splitlines()

    @staticmethod
    def write_csv(file_path, header, data):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

    @staticmethod
    def read_csv(file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            return [row for row in csv_reader if row and row[0] != 'Dog']


class Card:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def __str__(self):
        stats_str = ', '.join([f"{key}: {value}" for key, value in self.stats.items()])
        return f"{self.name} ({stats_str})"

    def get_stat(self, category):
        return self.stats.get(category, 0)


class Deck:
    def __init__(self, cards=None):
        self.cards = cards or []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0) if self.cards else None

    def add(self, *new_cards):
        self.cards.extend(new_cards)

    def __len__(self):
        return len(self.cards)


class MakeCards:
    def __init__(self, file_handler):
        self.file_handler = file_handler

    def open_file(self, file_path):
        return self.file_handler.read_txt(file_path)

    def make_card(self, name):
        stats = {
            'exercise': random.randint(1, 5),
            'intelligence': random.randint(1, 100),
            'friendliness': random.randint(1, 10),
            'drool': random.randint(1, 10)
        }
        return Card(name, stats)

    def create_deck(self, file_path):
        dogs = self.open_file(file_path)
        return Deck([self.make_card(dog) for dog in dogs])

    def save_deck(self, deck, file_path):
        header = ['Dog', 'Exercise', 'Intelligence', 'Friendliness', 'Drool']
        data = [
            [card.name, card.stats['exercise'], card.stats['intelligence'], card.stats['friendliness'], card.stats['drool']]
            for card in deck.cards
        ]
        self.file_handler.write_csv(file_path, header, data)


class GameLogic:
    def compare_cards(self, category, player_card, computer_card):
        player_value = player_card.get_stat(category)
        computer_value = computer_card.get_stat(category)

        if player_value > computer_value:
            return 'player'
        elif player_value < computer_value:
            return 'computer'
        return 'tie'


class UserInterface:
    def __init__(self):
        self.file_handler = FileHandler()
        self.make_cards = MakeCards(self.file_handler)
        self.game_logic = GameLogic()

    def menu(self):
        while True:
            choice = self.character_print(''' 
    Welcome, here are your options, please select a number:
        1. Play game
        2. Quit 
    
''')

            if choice == '1':
                self.play()
            elif choice == '2':
                exit('Au revoir!')
            else:
                self.character_print('Invalid input, try again.')

    def intro(self):
        while True:
            try:
                num_cards = int(self.character_print(''' 
    How many cards do you want to be played? (Number must be >3, <31, and even)
You can also type 'exit' to quit.
'''))

                if num_cards <= 3 or num_cards >= 31 or num_cards % 2 != 0:
                    raise ValueError("Please enter a valid number")
                else:
                    break
            except ValueError as e:
                self.character_print(f"Error: {e}\n")
            except KeyboardInterrupt:
                self.character_print("\nExiting game... Goodbye!\n")
                exit()

        return num_cards

    def make_decks(self):
        number = self.intro()
        deck = self.make_cards.create_deck('Top-Dog/dogs.txt')
        deck.shuffle()

        player_deck = Deck(deck.cards[:number // 2])
        computer_deck = Deck(deck.cards[number // 2:number])

        return player_deck, computer_deck

    def play(self):
        player_deck, computer_deck = self.make_decks()
        categories = ['exercise', 'intelligence', 'friendliness', 'drool']

        while player_deck and computer_deck:
            player_card = player_deck.draw()
            computer_card = computer_deck.draw()

            self.character_print(f"\nYour card:\n{player_card}")

            while True:
                try:
                    category = self.character_print(
                        "\nChoose your category ((e)xercise, (i)ntelligence, (f)riendliness, (d)rool). Type 'exit' to quit: ").lower()
                    if category == 'exit':
                        self.character_print("\nExiting game... Goodbye!\n")
                        exit()
                    if category not in categories:
                        raise ValueError("Please enter a valid category")

                    result = self.game_logic.compare_cards(category, player_card, computer_card)

                    self.character_print(f"\nComputer's card:\n{computer_card}")
                    self.character_print(f"\nYour {category}: {player_card.get_stat(category)}")
                    self.character_print(f"Computer's {category}: {computer_card.get_stat(category)}")

                    if result == 'player':
                        self.character_print("You win this round!")
                        player_deck.add(player_card, computer_card)
                    elif result == 'computer':
                        self.character_print("Computer wins this round!")
                        computer_deck.add(player_card, computer_card)
                    else:
                        self.character_print("It's a tie! No cards are won.")
                        player_deck.add(player_card)
                        computer_deck.add(computer_card)

                    break
                except ValueError as e:
                    self.character_print(str(e))

            self.character_print(f"\nYou now have {len(player_deck)} card(s)")
            self.character_print(f"The computer now has {len(computer_deck)} card(s)")

        if len(player_deck) == 0:
            self.character_print("The computer wins!!!")
        elif len(computer_deck) == 0:
            self.character_print("You Win!!!!")

        if self.character_print("Return to menu? y/n\n").lower() == 'y':
            self.menu()
        else:
            self.character_print("\nExiting game... Goodbye!\n")
            exit()

    def character_print(self, info):
        try:
            for char in info:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.010)
            return input()
        except KeyboardInterrupt:
            self.character_print("\nExiting game... Goodbye!\n")
            exit()


run_game = UserInterface()
run_game.menu()
