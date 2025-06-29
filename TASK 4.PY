def start_game():
    print("🌲 Welcome to 'The Lost Forest' Adventure!")
    print("You're an explorer lost in an enchanted forest. You must find your way out.")
    print("Your choices will determine your fate.\n")
    first_choice()

def first_choice():
    print("You reach a fork in the path.")
    print("1. Take the LEFT path.")
    print("2. Take the RIGHT path.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid input. Try again.")
        first_choice()

def left_path():
    print("\nYou chose the left path and find a mysterious river.")
    print("1. Try to SWIM across.")
    print("2. Follow the river downstream.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\n💀 Oh no! The current is too strong. You drown. GAME OVER.")
    elif choice == "2":
        print("\n🏞️ You follow the river and find a village. You're safe! YOU WIN!")
    else:
        print("Invalid input. Try again.")
        left_path()

def right_path():
    print("\nYou chose the right path and encounter a talking owl.")
    print("1. Listen to the owl’s advice.")
    print("2. Ignore the owl and move on.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\n🦉 The owl tells you a safe route out. You escape the forest. YOU WIN!")
    elif choice == "2":
        print("\n🌪️ You get lost deeper in the forest and vanish forever. GAME OVER.")
    else:
        print("Invalid input. Try again.")
        right_path()

# Start the game
start_game()
