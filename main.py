import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(which_player, number_of_cards):
    """
    Deal the random card from the deck. U can choose number of cards dealed and for which player.
    """
    for card in range(number_of_cards):
        which_player.append(random.choice(cards))


def calculate_score(which_hand):
    """
    calculates the score. If it is blackjack from start returns zero.
    """
    if 11 in which_hand and 10 in which_hand and len(which_hand) == 2:
        return 0
    if 11 in which_hand and sum(which_hand) > 21:
        which_hand.remove(11)
        which_hand.append(1)
    return sum(which_hand)


def compare(users_score, computers_score):
    """
    Logic about scores. Returns strings with communicates
    """
    if users_score > 21 or computers_score > 21:
        return "You went over. You lose 😤"
    if users_score == computers_score:
        return "its a Draw!"
    elif users_score > computers_score:
        return "You Win!"
    elif users_score < computers_score:
        return "You Loose!"
    elif users_score > 21:
        return "You have too much score!"
    elif computers_score > 21:
        return "Computer has too much score!"
    elif computers_score == 0:
        return "You loose Computer has Blackjack!"
    elif users_score == 21:
        return "You have Blackjack! You Win!"


def play_game():
    print(logo)

    players_hand = []
    computers_hand = []
    deal_card(players_hand,2)
    deal_card(computers_hand,2)

    game_is_over = False
    while not game_is_over:

        user_score = calculate_score(players_hand)
        computer_score = calculate_score(computers_hand)
        print(f"Your cards are: {players_hand}, current score: {user_score}")
        print(f"Computers first card is: {computers_hand[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_over = True
        else:
            drawing_card = input("Do you want to draw another card? Type 'y' or 'n': ")
            if drawing_card == "y":
                deal_card(players_hand,1)
            else:
                game_is_over = True
    while computer_score != 0 and computer_score < 17:
        deal_card(computers_hand,1)
        computer_score = calculate_score(computers_hand)
    print(f"Your final hand is: {players_hand} and final score: {user_score}.")
    print(f"Computers final hand is: {computers_hand} and final score: {computer_score}.")
    print(compare(user_score,computer_score))


while input("Do You want to play Game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
