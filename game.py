import random

room = 1

def monster():
    rand = random.randrange(1, 100)
    
    if rand <= 30:
        print("A vampire is here to suck your blood!")
    elif rand <= 50:
        print("A mummy crawls out of his coffin to attack you!")
    else:
        print()
        
    
    
    

while True:
    if room == 1:
        print("You are in room 1. You can go 'n' or 'e'.")
        choice = input()
        if choice == 'e':
            room = 2
        elif choice == 'n':
            room = 4
        else:
            print("wob")
            
    if room == 2:
        print("You are in room 2. You can go 'w' or 'n'.")
        monster()
        choice = input()
        if choice == 'w':
            room = 1
        elif choice == 'n':
            room = 3
        else:
            print("wob")
            
    if room == 3:
        print("You are in room 3. You can go 'w' or 's'.")
        choice = input()
        if choice == 'w':
            room = 4
        elif choice == 's':
            room = 2
            
    if room == 4:
        print("You are in room 4. You can go 'w' or 's' or even 'e'.")
        choice = input()
        if choice == 'w':
            room = 5
        elif choice == 's':
            room = 1
        elif choice == 'e':
            room = 3
            
    if room == 5:
        print("You are in room 5. You can go 'e'.")
        monster()
        choice = input()
        if choice == 'e':
            room = 4


