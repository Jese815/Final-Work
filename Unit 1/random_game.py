import random

names_AI = ['fred', 'javi', 'thomas', 'ken', 'jessie']

def get_player_choice():
    print("Choose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        try:
            choice = int(input("Enter a number: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a number.")

def get_ai_choice():
    return random.choice([1, 2, 3])

def determine_winner(player, ai):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    print(f"You chose: {choices[player]}")
    print(f"AI chose: {choices[ai]}")

    if player == ai:
        return "It's a tie!"
    elif (player == 1 and ai == 3) or (player == 2 and ai == 1) or (player == 3 and ai == 2):
        return "You Win!"
    else:
        return "You Lose!"

def play_game():
    player_name = input("Enter your name: ")
    ai_name = random.choice(names_AI)
    print(f"Your opponent is {ai_name}")

    while True:
        print('''Menu:
         1) Play game
         2) Exit''')

        user_choice = input("Select a number: ")

        if user_choice == '1':
            player_choice = get_player_choice()
            ai_choice = get_ai_choice()

            result = determine_winner(player_choice, ai_choice)
            print(f"Result: {result}")
        elif user_choice == '2':
            print("Goodbye!")
            break
        else:
            print("Enter a valid number (1 or 2).")

if __name__ == "__main__":
    play_game()
