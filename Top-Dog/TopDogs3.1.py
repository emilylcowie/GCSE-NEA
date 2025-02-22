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

    def intro(self):
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
        number = self.intro()
        game = Make_cards()
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
                    print("You Win!!!!")
                elif len(player_deck) == 0:
                    print("The computer wins!!!")
                if str(input("Return to menu? y/n\n")) == 'y':
                    self.menu()
                else:
                    exit("Au Revoir")

            print("\nYour card:")
            print(player_card)

            

            while True:
                try:
                    category = input("\nChoose your category (exercise, intelligence, friendliness, drool): ").lower()
                    if category not in categories:
                        raise ValueError("Please enter a valid category")
                    else:
                        self.compare(category, player_card, computer_card, player_deck, computer_deck, categories)
                        break
                except ValueError as e:
                    print(e)

    def compare(self, category, player_card, computer_card, player_deck, computer_deck, categories):
        print("\nComputer's card:")
        print(computer_card)
    
        print(f"\nComparing category '{category}'...")

        player_value = player_card[categories.index(category)+1]
        computer_value = computer_card[categories.index(category)+1]

        print(f"Your card's {category}: {player_value}")
        print(f"Computer's card's {category}: {computer_value}")

        if player_value > computer_value:
            print("You win this round!")
            player_deck.append(player_card)
            player_deck.append(computer_card)
        elif player_value < computer_value:
            print("Computer wins this round!")
            computer_deck.append(player_card)
            computer_deck.append(computer_card)
        else:
            print("It's a tie! No cards are won.")
            player_deck.append(player_card)
            computer_deck.append(computer_card)

        if not player_deck:
            print("Game Over! You lose.")
        elif not computer_deck:
            print("Game Over! You win.")

run_game = UserInterface()
run_game.menu()