import random
import time
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
print("Welcome to Blackjack!\n")
time.sleep(1)
print("You will be given two cards, ranging from A to K. You can ask for more cards later. Your goal is to get as close to 21 points as possible.")
time.sleep(4)
print("If you exceed 21 points, that is a 'bust'. If you bust, your opponent wins (unless they bust as well).")
time.sleep(4)
print("Have fun!")
time.sleep(1)

playerMoney = 100
player1Money = 100
player2Money = 100
playAgain = "yes"
while playAgain == "yes":
    version = input("Would you like to play against the computer or against another person? Enter 1 for the computer and 0 for another player. ")
    if version == "1":
        # Player V.S. Computer
        time.sleep(1)
        playerCards = []
        playerPoints = 0
        playerCards.append(random.choice(cards))
        playerCards.append(random.choice(cards))
        print("This is the player's turn")
        time.sleep(1.5)
        print("Your starting cards: ", playerCards)
        for i in playerCards:
            if i == "A":
                playerPoints += 1
            elif i == "J":
                playerPoints += 11
            elif i == "Q":
                playerPoints += 12
            elif i == "K":
                playerPoints += 13
            else:
                playerPoints += int(i)
        time.sleep(1)
        print("Your points: ", playerPoints)
        bet = input("You have " + str(playerMoney) + " coins. How much would you like to bet? ")
        playerMoney -= int(bet)
        hitStand = "hit"
        while hitStand == "hit" and playerPoints < 21:
            hitStand = input("Would you like to hit or stand? ")
            if hitStand == "hit":
                newCard = random.choice(cards)
                playerCards.append(newCard)
                time.sleep(1)
                print("You drew a(n) ", newCard)
                playerPoints = 0
                for i in playerCards:
                    if i == "A":
                        playerPoints += 1
                    elif i == "J":
                        playerPoints += 11
                    elif i == "Q":
                        playerPoints += 12
                    elif i == "K":
                        playerPoints += 13
                    else:
                        playerPoints += int(i)
                print(playerPoints)
                if playerPoints > 21:
                    print("You bust!")

        # Computer's Turn
        computerCards = []
        computerPoints = 0
        print("This is the computer's turn")
        time.sleep(1)
        computerCards.append(random.choice(cards))
        computerCards.append(random.choice(cards))
        for i in computerCards:
            if i == "A":
                computerPoints += 1
            elif i == "J":
                computerPoints += 11
            elif i == "Q":
                computerPoints += 12
            elif i == "K":
                computerPoints += 13
            else:
                computerPoints += int(i)
        print(computerCards)
        time.sleep(1)
        print(computerPoints)
        time.sleep(1)
        stand = False
        while stand == False and computerPoints < 16:
            computerHit = random.randint(1,100)
            if computerHit <= 90:
                computerCards.append(random.choice(cards))
                time.sleep(1)
                print("The computer chose to hit")
                time.sleep(1)
                print(computerCards)
                computerPoints = 0
                for i in computerCards:
                    if i == "A":
                        computerPoints += 1
                    elif i == "J":
                        computerPoints += 11
                    elif i == "Q":
                        computerPoints += 12
                    elif i == "K":
                        computerPoints += 13
                    else:
                        computerPoints += int(i)
                time.sleep(0.5)
                print(computerPoints)

            else:
                stand = True
                time.sleep(1)
                print("The computer chose to stand")
                time.sleep(1)
        while stand == False and 16 < computerPoints < 21:
            computerHit = random.randint(1,100)
            if computerHit > 90:
                computerCards.append(random.choice(cards))
                time.sleep(1)
                print("The computer chose to hit")
                time.sleep(0.5)
                print(computerCards)
                computerPoints = 0
                for i in computerCards:
                    if i == "A":
                        computerPoints += 1
                    elif i == "J":
                        computerPoints += 11
                    elif i == "Q":
                        computerPoints += 12
                    elif i == "K":
                        computerPoints += 13
                    else:
                        computerPoints += int(i)
                print(computerPoints)
            else:
                stand = True
                time.sleep(1)
                print("The computer chose to stand")
                time.sleep(1)
        print("Both players have finished their turns. It is now time to decide the winner.")
        time.sleep(1)
        if computerPoints <= 21 and playerPoints <= 21:
            if computerPoints > playerPoints:
                print("The computer won!")
                print("You now have ", playerMoney, "coins!")
            else:
                print("You won!")
                time.sleep(0.5)
                playerMoney += 2 * int(bet)
                print("You now have ", playerMoney, " coins!")
        elif computerPoints > 21 and playerPoints > 21:
            if computerPoints < playerPoints:
                print("The computer won!")
                print("You now have ", playerMoney, "coins!")
            else:
                print("You won!")
                playerMoney += 2 * int(bet)
                print("You now have", playerMoney, "coins!")
        elif computerPoints > 21 and playerPoints <= 21:
            print("You won!")
            playerMoney += 2 * int(bet)
            print("You now have", playerMoney, "coins!")
        else:
            print("The computer won!")
        if playerPoints == computerPoints:
            print("It's a draw!")
            playerMoney += int(bet)
            time.sleep(1)
            print("You now have ", playerMoney, "coins!")

    # Player V.S. Player
    elif version == "0":
        print("This is the 2-Player Version")
        time.sleep(1.5)
        print("Choose which person is Player 1 and which is Player 2.")

        # Player 1's Turn
        player1Cards = []
        player1Points = 0
        player1Cards.append(random.choice(cards))
        player1Cards.append(random.choice(cards))
        time.sleep(2)
        print("This is Player 1's turn")
        time.sleep(1.5)
        print("Your starting cards: ", player1Cards)
        for i in player1Cards:
            if i == "A":
                player1Points += 1
            elif i == "J":
                player1Points += 11
            elif i == "Q":
                player1Points += 12
            elif i == "K":
                player1Points += 13
            else:
                player1Points += int(i)
        time.sleep(1)
        print("Your points: ", player1Points)
        time.sleep(1)
        bet1 = input("You have " + str(player1Money) + " coins. How much would you like to bet? ")
        player1Money -= int(bet1)
        hitStand = "hit"
        while hitStand == "hit" and player1Points < 21:
            hitStand = input("Would you like to hit or stand? ")
            if hitStand == "hit":
                newCard = random.choice(cards)
                player1Cards.append(newCard)
                time.sleep(1)
                print("You drew a(n) ", newCard)
                player1Points = 0
                for i in player1Cards:
                    if i == "A":
                        player1Points += 1
                    elif i == "J":
                        player1Points += 11
                    elif i == "Q":
                        player1Points += 12
                    elif i == "K":
                        player1Points += 13
                    else:
                        player1Points += int(i)
                print(player1Points)
                if player1Points > 21:
                    print("You bust!")

        # Player 2's Turn
        player2Cards = []
        player2Points = 0
        player2Cards.append(random.choice(cards))
        player2Cards.append(random.choice(cards))
        time.sleep(2)
        print("This is Player 2's turn")
        time.sleep(1.5)
        print("Your starting cards: ", player2Cards)
        for i in player2Cards:
            if i == "A":
                player2Points += 1
            elif i == "J":
                player2Points += 11
            elif i == "Q":
                player2Points += 12
            elif i == "K":
                player2Points += 13
            else:
                player2Points += int(i)
        print("Your points: ", player2Points)
        bet2 = input("You have " + str(player2Money) + " coins. How much would you like to bet? ")
        player2Money -= int(bet2)
        hitStand = "hit"
        while hitStand == "hit" and player2Points < 21:
            hitStand = input("Would you like to hit or stand? ")
            if hitStand == "hit":
                newCard = random.choice(cards)
                player2Cards.append(newCard)
                time.sleep(1)
                print("You drew a(n) ", newCard)
                player2Points = 0
                for i in player2Cards:
                    if i == "A":
                        player2Points += 1
                    elif i == "J":
                        player2Points += 11
                    elif i == "Q":
                        player2Points += 12
                    elif i == "K":
                        player2Points += 13
                    else:
                        player2Points += int(i)
                print(player2Points)
                if player2Points > 21:
                    print("You bust!")
        print("Both players have finished their turns. It is now time to decide the winner.")
        if player1Points <= 21 and player2Points <= 21:
            if player1Points > player2Points:
                print("Player 1 won!")
            else:
                print("Player 2 won!")
        elif player1Points > 21 and player2Points > 21:
            if player1Points < player2Points:
                print("Player 1 won!")
            else:
                print("Player 2 won!")
        elif player1Points > 21 and player2Points <= 21:
            print("Player 2 won!")
        else:
            print("Player 1 won!")
        if player1Points == player2Points:
            print("It's a draw!")
            player1Money += int(bet1)
            time.sleep(1)
            print("Player 1 has ", player1Money, "coins!")
            player2Money += int(bet2)
            time.sleep(1)
            print("Player 2 has ", player2Money, "coins!")

    else:
        print("Please enter either 1 or 0 to play.")
    playAgain = input("Would you like to play again (yes/no)?")
print("Thanks for playing!")