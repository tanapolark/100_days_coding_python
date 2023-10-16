import random

def user_input_limit(prompt, max_length):
    while True:
        user_input = input(prompt)
        if len(user_input) <= max_length:
            return user_input
        else:
            print(f"Input exceeds the maximum length of {max_length} characters. Try again.")

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

running = True

while running:
    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
           'coyote crow deer dog donkey duck eagle ferret fox frog goat '
           'goose hawk lion lizard llama mole monkey moose mouse mule newt '
           'otter owl panda parrot pigeon python rabbit ram rat raven '
           'rhino salmon seal shark sheep skunk sloth snake spider '
           'stork swan tiger toad trout turkey turtle weasel whale wolf '
           'wombat zebra ').split()

    pics = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="]

    word_chosen = random.choice(words)
    num_of_alphabets = len(word_chosen)
    print("Hangman")
    user_alphabets = []
    counter = 0

    while counter < 6:
        print(pics[counter])
        print(display_word(word_chosen, user_alphabets))
        if '_' not in display_word(word_chosen, user_alphabets):
            print(f"Congratulations! You've guessed the word: {word_chosen}")
            break
        user_input = user_input_limit("Choose a letter: ", 1)
        user_alphabets.append(user_input)
        if user_input not in word_chosen:
            counter += 1

    if counter == 6:
        print(f"Sorry, you're out of attempts. The word was: {word_chosen}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        running = False
