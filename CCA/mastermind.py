import random


def generate_sequence(colors, length=4):
    return [random.choice(colors) for _ in range(length)]


def compare_sequences(correct, guess):
    correct_position = sum(1 for c, g in zip(correct, guess) if c == g)
    correct_color_wrong_position = (
        sum(min(correct.count(color), guess.count(color)) for color in set(guess))
        - correct_position
    )
    return correct_position, correct_color_wrong_position

def play_mastermind():

    colors = ["red", "blue", "green", "yellow", "pink", "orange", "purple", "white"]

    correct_sequence = generate_sequence(colors)
    attempts = 0

    print("Welcome to Mastermind!")
    print("Available colors:", ", ".join(colors))
    print("Try to guess the correct sequence of 4 colors.")
    print("Enter your guesses separated by spaces (e.g., 'red blue green yellow').")

    while True:
        guess = input("Enter your guess: ").lower().split()

       
        if len(guess) != 4 or not all(color in colors for color in guess):
            print("Invalid input. Please enter exactly 4 colors from the list.")
            continue

        
        attempts += 1

        
        correct_position, correct_color_wrong_position = compare_sequences(
            correct_sequence, guess
        )

        
        print(f"Correct color in the correct place: {correct_position}")
        print(f"Correct color but in the wrong place: {correct_color_wrong_position}")

 
        if correct_position == 4:
            print(f"Congratulations! You guessed the correct sequence in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_mastermind()