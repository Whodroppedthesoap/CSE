import random

Word_bank = ["Snap back to reality oops there goes humanity", "Reality is sometimes a disappointment",
             "It was and it was beautiful", "Thanos Snap", "I'm sorry little one", "You should've gone for the head",
             "I knew you would still care", "What did it cost? , Everything", "Avenger Theme song",
             "see perfectly balanced as all things should be"]
guesses = 8
win_info = False
win_condition = False
BankWord = Word_bank[random.randint(0, len(Word_bank) - 1)]
letters_in_word = list(BankWord)
guessed_letter = []
hidden_word = []

while guesses > 0:
    output = []
    for letter in letters_in_word:
        if letter.lower() in guessed_letter:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))

    guess = input("Guess a letter: ").lower()
    guessed_letter.append(guess)

