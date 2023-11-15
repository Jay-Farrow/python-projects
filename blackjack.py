# Task: Write a program that simulates the game of blackjack.

# Rules of Blackjack/21:
# Beat the dealer's hand without going over 21. If you get 21 points exactly on the deal, that is called a 'blackjack'
# Blackjack card values 'J', 'K', 'Q', 10 have a value of 10. 'A' has a value of 1 or 11. The rest of the card values are as they should be. 
# A face card combined with an 'A' is a blackjack(value of 21). 

import random
import os
from art import blackjack

# This clear() function clears the screen following the restart of the game and other choices implemented in the main code of the game.
def clear():
    '''Clears the terminal screen when called.'''
    os.system('cls')

# Created a dictionary called hands to store the 'player' and 'dealer' card hands. 
hands = {
    'player' : [],
    'dealer': [],
}

# Created a list called cards for the set of 52 playing cards.
cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


# Determine the values of both the player hand and dealer hand. Create a function to determine the hand values.
# player_hand_function determines the value of the player hand.
def player_hand_value(player_hand):
    '''Determines the value of the player's cards.'''
    player_hand_value = 0
    for value in player_hand:
        if value == 'J' or value == 'Q' or value == 'K':
            value = 10
        elif value == 'A':
            if player_hand_value <= 10:
                value = 11
            elif player_hand_value >= 11:
                value = 1
        player_hand_value += value
    return player_hand_value

# dealer_hand_function determines the value of the dealer hand. 
def dealer_hand_value(dealer_hand):
    '''Determines the value of the dealer's cards.'''
    dealer_hand_value = 0
    for value in dealer_hand:
        if value == 'J' or value == 'Q' or value == 'K':
            value = 10
        elif value == 'A':
            if dealer_hand_value <= 10:
                value = 11
            elif dealer_hand_value >= 11:
                value = 1
        dealer_hand_value += value
    return dealer_hand_value

# Determine who wins, the player or the dealer. Create a function to determine who wins the game.
def winner(player_hand_value, dealer_hand_value):
    '''Determines the winner of the blackjack game.'''
    if player_hand_value > 21:
        message = 'Bust! You are over 21.'
    elif dealer_hand_value > 21:
        message = 'Dealer busted! You win.'
    elif player_hand_value == 21:
        message = 'Blackjack! You Win.'
    elif dealer_hand_value == 21:
        message = 'Dealer has Blackjack! You lose.'
    elif dealer_hand_value < 17:
        message = 'Dealer is below 16.'
    elif player_hand_value > dealer_hand_value:
        message = 'You win!'
    elif player_hand_value < dealer_hand_value:
        message = 'Dealer wins!'
    elif player_hand_value == dealer_hand_value:
        message = 'Push.'
    return message




#Main BlackJack Game
game_state = True
while game_state:
    print("\nDo you want to play BlackJack? Type yes or no. ")        # Start the game
    player_input = input().lower()
    if player_input == 'yes':
        player_hand = hands['player']
        dealer_hand = hands['dealer']
        player_hand = [random.choice(cards), random.choice(cards)]  # Deal the first set of cards to the player and the dealer. 
        dealer_hand = [random.choice(cards), random.choice(cards)]
        player_choice = True
        while player_choice:
            clear()
            print(blackjack)
            player_value = player_hand_value(player_hand=player_hand)            # Call the player_hand_value function to determine the players card set value.
            dealer_value = dealer_hand_value(dealer_hand=dealer_hand)            # Call the dealer_hand_value function to determine the dealers card set value.
            print(f"Player hand: {player_hand}, Your current hand value: {player_value}.")   # Display the player's cards and the first dealer card.
            print(f"Dealer hand: {dealer_hand[0]}")
            who_wins = winner(player_hand_value=player_value, dealer_hand_value=dealer_value)  # Call the winner function to determine the winner of the game. 
            if who_wins == 'Blackjack! You Win.':
                print(who_wins)
                player_choice = False
                break
            elif who_wins == 'Dealer has Blackjack! You lose.':         # Determine if either the player or dealer gets 21 on the first deal of cards. 
                print(who_wins)
                player_choice = False
                break
            elif who_wins == 'Bust! You are over 21.':
                print(f"{who_wins}, Dealer had: {dealer_value}.")
                player_choice = False
                break
            player_choice_input = input("\nDo you want to hit or stand? ").lower()
            if player_choice_input == 'hit':
                player_hand.append(random.choice(cards))
            elif player_choice_input == 'stand':
                while who_wins == 'Dealer is below 16.':
                    dealer_hand.append(random.choice(cards))
                    dealer_value = dealer_hand_value(dealer_hand=dealer_hand)
                    print(f"Dealer Hand: {dealer_hand}, Current dealer hand value: {dealer_value}.")
                    who_wins = winner(player_hand_value=player_value, dealer_hand_value=dealer_value)
                print(who_wins)
                player_choice = False
    elif player_input == 'no':
        print("\nExited Game")
        game_state = False