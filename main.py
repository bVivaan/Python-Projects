import random, time
deck = ["🔥1", "🔥2", "🔥3", "🔥4", "🔥5", "💧1", "💧2", "💧3", "💧4", "💧5", "🌱1", "🌱2", "🌱3", "🌱4", "🌱5"]
print("Welcome to the Game!")
time.sleep(1)
print("Play your element cards against the computer's to win battles. Fire beats nature, nature beats water, and water beats fire.")
time.sleep(3.5)
print("In order to win a game, you need to win at least one turn with all three elements (fire, water, AND nature).")
time.sleep(3.5)
print("Have Fun!")
time.sleep(0.75)
playAgain = "yes"
# Loops every game
while playAgain == "yes":
    playerDeck = []
    computerDeck = []
    playerPoints = {"f": 0, "w": 0, "n": 0}
    computerPoints = {"f": 0, "w": 0, "n": 0}
    for i in range(4):
        playerDeck.append(random.choice(deck))
    for i in range(4):
        computerDeck.append(random.choice(deck))
    # Loops every turn
    while (playerPoints["f"] < 1 or playerPoints["w"] < 1 or playerPoints["n"] < 1) and (computerPoints["f"] < 1 or computerPoints["w"] < 1 or computerPoints["n"] < 1):
        print("Your deck: ", playerDeck)
        cardPlayed = input("Which card would you like to play? Enter 'f' for fire, 'w' for water, and 'n' for nature. For example, to play 🔥3, you would type 'f3' ")
        element = cardPlayed[0]
        number = cardPlayed[1]
        if element == "f":
            cardPlayed = "🔥" + str(number)
        elif element == "w":
            cardPlayed = "💧" + str(number)
        elif element == "n":
            cardPlayed = "🌱" + str(number)
        if cardPlayed in playerDeck:
            playerDeck.remove(cardPlayed)

        else:
            cardPlayed = input("Please enter a card that is in your deck.")

        computerCardPlayed = random.choice(computerDeck)
        computerElement = computerCardPlayed[0]
        if computerElement == "🔥":
            computerElement = "f"
        elif computerElement == "💧":
            computerElement = "w"
        elif computerElement == "🌱":
            computerElement = "n"
        computerNumber = computerCardPlayed[1]
        print("The computer played ", computerCardPlayed, "\n")
        time.sleep(1)

        if computerElement == element:
            if computerNumber > number:
                print("The computer won!")
                computerPoints[computerElement] += 1
            elif computerNumber < number:
                print("You won!")
                playerPoints[element] += 1
            else:
                print("It's a draw!")
        else:
            if computerElement == "f" and element == "w":
                print("You won!")
                playerPoints[element] += 1
            elif computerElement == "n" and element == "f":
                print("You won!")
                playerPoints[element] += 1
            elif computerElement == "w" and element == "n":
                print("You won!")
                playerPoints[element] += 1
            elif computerElement == "f" and element == "n":
                print("The computer won!")
                computerPoints[computerElement] += 1
            elif computerElement == "w" and element == "f":
                print("The computer won!")
                computerPoints[computerElement] += 1
            elif computerElement == "n" and element == "w":
                print("The computer won!")
                computerPoints[computerElement] += 1

        newCard = random.choice(deck)
        time.sleep(1)
        print("You drew a", newCard)
        playerDeck.append(newCard)
        time.sleep(2)
        print("Your points: ", playerPoints)
        print("Computer's points: ", computerPoints)
        time.sleep(2)

    if (playerPoints["f"] >= 1 and playerPoints["w"] >= 1 and playerPoints["n"] >= 1) and (computerPoints["f"] < 1 or computerPoints["w"] < 1 or computerPoints["n"] < 1):
        print("You won the game!")
    elif (playerPoints["f"] < 1 or playerPoints["w"] < 1 or playerPoints["n"] < 1) and (computerPoints["f"] >= 1 or computerPoints["w"] >= 1 or computerPoints["n"] >= 1):
            print("The computer won the game!")
    playAgain = input("Would you like to play again? ")
if playAgain == "no":
    print("Thanks for playing!")