"""Setting up Deck and Dealing cards out.

Available Functions
deal_hand(dict,list,int)
    goes through dictionary of cards and
find_available_card(dict)
    goes thru deck and finds the first with owner pile
set_up_deck()
    create a deck of cards
    returns a dictionary of each cards and the owner
print_hand(dict,list)
    Takes a dictionary of a deck and list of players
    and prints out each hand.
"""


def deal_hand(deck_of_cards, players, number_of_cards):
    """Function to deal out a desk of 52 cards."""
    # for key, value in deck.iteritems():
    for ctr in range(0, number_of_cards):
        for player in players:
            card_to_assign = find_available_card(deck_of_cards)
            deck_of_cards.update({card_to_assign: player})


def find_available_card(deck_of_cards):
    """Find the card that isn't owned by pile and set new owner."""
    for card, owner in deck_of_cards.items():
        if owner == 'pile':
            return card


def print_hand(deck_of_cards, players):
    """Function to print out who owns which card."""
    for player in players:
        print("%s has the following cards:" % player)
        for card, owner in deck_of_cards.items():
            if owner == player:
                print(card)


def set_up_deck():
    """Function to create a deck of cards."""
    card_numbers = (
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
    deck_of_cards = dict()

    for card_num in card_numbers:
        for suit in suits:
            # print(card_num + "_of_" + suit)
            my_key = card_num + "_of_" + suit
            deck_of_cards[my_key] = 'pile'

    return deck_of_cards


if __name__ == '__main__':
    my_deck = set_up_deck()
    print(my_deck)
    print()

    list_of_players = ['david', 'matt', 'paul', 'jeff']
    deal_hand(my_deck, list_of_players, 7)
    print(my_deck)
    print()

    print_hand(my_deck, list_of_players)
