def start():
    answer = "turtle".lower()
    guess = None
    tries = 3
    attempt = 0
    print("Welcome to 'Guess the Animal' game where you need to guess what animal I'm thinking of. You'll have 3 attemps to guess the animal, good luck.")

    while attempt < tries:
        guess = input("Enter guess: ").lower()
        attempt += 1
        if guess == answer:
            print("You got it! Well done mind reader.")
            break
        elif guess == "quit":
            print("Quitting game")
            break
        elif attempt == 3:
            print("You have used up all of your attemps! The animal is {answer}.")
            break
        else:
            print("Nope! It's a different animal and you now have", tries - attempt, "attempts left.")
    '''
    This function starts the guessing game loop logic. The function will poll and wait
    until the user inputs their guess and will exit once some conditions are met.
    '''

    # Create a string variable that contains the answer.

    return None # replace this line with your game loop logic.

start()