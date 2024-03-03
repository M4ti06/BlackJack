import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(which_player, number_of_cards):
    for card in range(number_of_cards):
        which_player.append(random.choice(cards))


def score(which_hand):
    if which_hand.count(11) >= 2:
        return (which_hand.count(11) -1)*(-10) + sum(which_hand)
    else:
        return sum(which_hand)


def over21(which_hand):
    if score(which_hand) > 21:
        return True
    else:
        return False


print(logo)

still_playing = True
while still_playing:
    players_hand = []
    computers_hand = []
    deal_card(players_hand, 2)
    deal_card(computers_hand, 2)
    still_drawing = True

    if score(players_hand) == 21:
        print("You Win! You are so lucky!")
        print(f"Yours cards are: {players_hand}")
        still_drawing = False
    if score(computers_hand) == 21:
        print("You Loose! Computer is lucky!")
        print(f"Computers cards are: {computers_hand}")
        still_drawing = False

    how_many_draws = 0
    while still_drawing:
        player_score = score(players_hand)
        computer_score = score(computers_hand)
        print(f"Yours cards are: {players_hand}, Your score is: {player_score}")
        if how_many_draws == 0:
            print(f"Computers card is: {computers_hand[0]}")
        else:
            print(f"Computers card is: {computers_hand}")
        if score(players_hand) == 21:
            print("You Win!")
            break
        how_many_draws += 1
        draw_another = input("Do You want to draw another card? Type 'y' or 'n': ")
        if draw_another == "y":
            deal_card(players_hand, 1)
            if over21(players_hand):
                print(f"You loose! Your cards are: {players_hand} and score {player_score}")
                still_drawing = False
        else:
            while score(computers_hand) < 17:
                deal_card(computers_hand,1)
                computer_score = score(computers_hand)
                print(f"Computers hand is {computers_hand} and score {computer_score}")
                if over21(computers_hand):
                    still_drawing = False
            if score(computers_hand) > 21:
                print("Computers badluck Yours win!")
            elif score(players_hand) > score(computers_hand):
                print(" You Win!")
            elif score(players_hand) == score(computers_hand):
                print("Its a draw!")
            else:
                print("You loose!")
            still_drawing = False
    another_round = input("Do You want another round? Type 'y' or 'n': ")
    if another_round == "n":
        print("Thank you for playing the game :-)")
        still_playing = False

