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
        stats_str = ', '.join(
            [f"{key}: {value}" for key, value in self.stats.items()])
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
            [card.name, card.stats['exercise'], card.stats['intelligence'],
                card.stats['friendliness'], card.stats['drool']]
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

''', require_input=True)

            if choice == '1':
                self.play()
            elif choice == '2':
                exit('Au revoir!')
            else:
                self.character_print(
                    'Invalid input, try again.', require_input=False)

    def intro(self):
        while True:
            try:
                user_input = self.character_print('''
    How many cards do you want to be played? (Number must be >3, <31, and even)
    You can also type 'exit' to quit.
    ''', require_input=True).strip().lower()

                if user_input == 'exit':
                    self.character_print(
                        "\nExiting game... Goodbye!\n", require_input=False)
                    exit()

                num_cards = int(user_input)
                if 3 < num_cards < 31 and num_cards % 2 == 0:
                    break
                else:
                    self.character_print(
                        "Please enter a valid number (even, >3, <31)", require_input=True)
            except ValueError:
                self.character_print(
                    "Invalid input. Please enter a number or type 'exit'.", require_input=True)
            except KeyboardInterrupt:
                self.character_print(
                    "\nExiting game... Goodbye!\n", require_input=False)
                exit()

        return num_cards

    def make_decks(self):
        number = self.intro()
        deck = self.make_cards.create_deck('Top-Dog/dogs.txt')
        deck.shuffle()

        player_deck = Deck(deck.cards[:number // 2])
        computer_deck = Deck(deck.cards[number // 2:number])

        return player_deck, computer_deck

    import random

    def play(self):
        def get_player_category():
            category_input = self.character_print(
                "\nChoose your category ((e)xercise, (i)ntelligence, (f)riendliness, (d)rool). Type 'exit' to quit: ",
                require_input=True
            ).lower()

            if category_input == 'exit':
                self.character_print(
                    "\nExiting game... Goodbye!\n", require_input=False)
                exit()

            category_map = {'e': 'exercise', 'i': 'intelligence',
                            'f': 'friendliness', 'd': 'drool'}
            if category_input not in category_map:
                raise ValueError("Invalid category")

            return category_map[category_input]

        def computer_choice():
            return random.choice(['exercise', 'intelligence', 'friendliness', 'drool'])

        def process_round(player_card, computer_card, category):
            result = self.game_logic.compare_cards(
                category, player_card, computer_card)
            self.character_print(f"\nComputer's card:\n{
                                 computer_card}", require_input=False)
            self.character_print(f"\nYour {category}: {
                                 player_card.get_stat(category)}", require_input=False)
            self.character_print(f"Computer's {category}: {
                                 computer_card.get_stat(category)}", require_input=False)

            if result == 'player':
                self.character_print(
                    "You win this round!", require_input=False)
                return 'player', player_card, computer_card
            elif result == 'computer':
                self.character_print(
                    "Computer wins this round!", require_input=False)
                return 'computer', player_card, computer_card
            else:
                self.character_print(
                    "It's a tie! No cards are won.", require_input=False)
                return 'tie', player_card, computer_card

        player_deck, computer_deck = self.make_decks()
        categories = ['exercise', 'intelligence', 'friendliness', 'drool']

        while player_deck and computer_deck:
            player_card = player_deck.draw()
            computer_card = computer_deck.draw()
            self.character_print(
                f"\nYour card:\n{player_card}\n", require_input=False)

            try:
                category = get_player_category()
                round_result, player_card, computer_card = process_round(
                    player_card, computer_card, category)

                if round_result == 'player':
                    player_deck.add(player_card, computer_card)
                elif round_result == 'computer':
                    computer_deck.add(player_card, computer_card)
                else:
                    player_deck.add(player_card)
                    computer_deck.add(computer_card)

            except ValueError as e:
                self.character_print(str(e), require_input=False)

            self.character_print(f"\nYou now have {len(
                player_deck)} card(s)", require_input=False)
            self.character_print(f"The computer now has {len(
                computer_deck)} card(s)", require_input=False)

            if len(player_deck) == 0:
                self.character_print(
                    "The computer wins!!!", require_input=False)
            elif len(computer_deck) == 0:
                self.character_print("You Win!!!!", require_input=False)

            if round_result == 'computer':
                computer_selected_category = computer_choice()
                self.character_print(f"\nComputer chooses: {
                                     computer_selected_category}\n", require_input=False)
                result = self.game_logic.compare_cards(
                    computer_selected_category, player_card, computer_card)
                self.character_print(f"\nYour {computer_selected_category}: {
                                     player_card.get_stat(computer_selected_category)}", require_input=False)
                self.character_print(f"Computer's {computer_selected_category}: {
                                     computer_card.get_stat(computer_selected_category)}", require_input=False)

                if result == 'player':
                    self.character_print(
                        "You win this round!", require_input=False)
                    player_deck.add(player_card, computer_card)
                elif result == 'computer':
                    self.character_print(
                        "Computer wins this round!", require_input=False)
                    computer_deck.add(player_card, computer_card)
                else:
                    self.character_print(
                        "It's a tie! No cards are won.", require_input=False)
                    player_deck.add(player_card)
                    computer_deck.add(computer_card)

        if len(player_deck) == 0:
            self.character_print("The computer wins!!!", require_input=False)
        elif len(computer_deck) == 0:
            self.character_print("You Win!!!!", require_input=False)

        if self.character_print("Return to menu? y/n\n", require_input=True).lower() == 'y':
            self.menu()
        else:
            self.character_print(
                "\nExiting game... Goodbye!\n", require_input=False)
            exit()

    def character_print(self, info, require_input):
        try:
            for char in info:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.010)
            if not require_input:
                sys.stdout.write("   \x1B[3mEnter to continue\x1B[0m\n")
                sys.stdout.flush()
                input()
            else:
                return input()
        except KeyboardInterrupt:
            print("\nExiting game... Goodbye!\n")
            exit()


run_game = UserInterface()
run_game.menu()
