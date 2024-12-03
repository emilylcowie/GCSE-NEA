import random

with open('Top-Dog/dogs.txt', 'r') as file:
    dogs = file.read()
    print(dogs)

dogcards = {}
for i in dogs:
    dogcards.update({"dog": i,
                     'exercise' : random.randint(1,5),
                     'intelligence' : random.randint(1,100),
                     'friendliness' : random.randint(1,10),
                     'drool' : random.randint(1,10)})
print(dogcards)