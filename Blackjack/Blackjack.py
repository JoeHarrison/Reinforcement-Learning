import random
import numpy as np

def new_deck():
    return [i for i in range(2,15)]*4

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = 'J'
        if card == 12:
            card = 'Q'
        if card == 13:
            card = 'K'
        if card == 14:
            card = 'A'
        hand.append(card)

    return hand

def total(hand):
    total = 0

    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            total += 10
        elif card == 'A':
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card

    return total

def hit(hand,deck):
    card = deck.pop()
    if card == 11:
        card = 'J'
    if card == 12:
        card = 'Q'
    if card == 13:
        card = 'K'
    if card == 14:
        card = 'A'
    hand.append(card)
    return hand

def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print("Player Blackjack")
        return 1
    elif total(dealer_hand) == 21:
        print("Dealer Blackjack")
        return -1
    elif total(player_hand) > 21:
        print("Player Bust")
        return -1
    elif total(dealer_hand) > 21:
        print("Dealer Bust")
        return 1
    elif total(player_hand) < total(dealer_hand):
        print("Dealer Higher Score")
        return -1
    elif total(player_hand) > total(dealer_hand):
        print("Player Higher Score")
        return 1

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print("Player Blackjack")
        return 1
    elif total(dealer_hand) == 21:
        print("Dealer Blackjack")
        return -1
    else:
        return 0

def game():
    deck = new_deck()
    dealer_hand = deal(deck)
    print(dealer_hand)
    player_hand = deal(deck)
    print(player_hand)

    win = 0

    win = blackjack(dealer_hand, player_hand)

    if win==0:
        choice = np.random.randint(1)

        if choice:
            hit(player_hand)
            while total(dealer_hand) < 17:
                hit(dealer_hand,deck)
            win = score(dealer_hand, player_hand)
        else:
            while total(dealer_hand) < 17:
                hit(dealer_hand,deck)
            win = score(dealer_hand, player_hand)

    return win

print(game())
