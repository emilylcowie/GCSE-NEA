def open_doors():
    count_open = 0
    for door_key in doors:
        if doors[door_key] == "Open":
            count_open += 1
    print(count_open)

def change_values(door_key):
    if doors[door_key] == "Open":
        doors[door_key] = "Closed"
    else:
        doors[door_key] = "Open"

# main program
doors = {}
for i in range(100):
    doors[f'door_{i}'] = "Closed"

for i in range(1, 101): 
    for door_key in tuple(doors)[::i+1]:
        change_values(doors[door_key])

open_doors() 