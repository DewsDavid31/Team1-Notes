class Player:
    variable = ""

class Deck:
    cards = 10

class Hand:
    variable = ""
class Dealer:
    varible = ""

def has_player():
    assert Player() != None, "Player doesn't exist"
    return Player() != None
def has_deck():
    assert Deck() != None, "Deck Doesn't exist"
    return Deck() != None
def has_hand():
    assert Hand() != None, "Hand Doesn't exist"
    return Hand() != None
def has_dealer():
    assert Dealer() != None, "Dealer cannot be found"
    
def deck_has_cards(deck):
    assert deck.cards > 0, "No cards found in deck"


def main():

    deck1 = Deck()
    deck_has_cards(deck1)

if __name__ == "__main__":
    # execute only if run as a script
    main()
