__author__ = 'yann'


class Card(object):
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __lt__(self, other):
        return self.get_number() < other.get_number()

    def __gt__(self, other):
        return self.get_number() > other.get_number()

    def __eq__(self, other):
        return self.get_number() == other.get_number()

    def get_number(self):
        if self.number.isdigit():
            return int(self.number)
        elif self.number == 'J':
            return 11
        elif self.number == 'Q':
            return 12
        elif self.number == 'K':
            return 13
        elif self.number == 'A':
            return 14

    @staticmethod
    def sort_key(obj):
        return obj.get_number()


# default assume cards is sorted
def is_royal_flush(cards: list):
    start_number, start_suit = 10, cards[0].suit
    for card in cards:
        if card.get_number() == start_number and card.suit == start_suit:
            start_number += 1
            continue
        else:
            return False

    return True


def is_straight_flush(cards: list):
    return not is_royal_flush(cards)

    start_number, start_suit = cards[0].get_number(), cards[0].suit
    for card in cards:
        if card.get_number() == start_number and card.suit == start_suit:
            start_number += 1
            continue
        else:
            return False
    return True


def is_four_of_a_kind(cards: list):
    start_number, count, max_count = cards[0].get_number(), 0, 0

    for card in cards:
        if card.get_number() == start_number:
            count += 1
        else:
            if count > max_count:
                max_count = count

            start_number = card.get_number()
            count = 1

    return max_count == 4


print(is_four_of_a_kind([Card('10', 'H'), Card('10', 'H'), Card('10', 'H'), Card('10', 'H'), Card('A', 'H')]))


def is_full_house(cards: list):
    pass


def is_flush(cards: list):
    pass


def is_straight(cards: list):
    pass


def is_three_of_a_kind(cards: list):
    pass


def is_two_pairs(cards: list):
    pass


def is_one_pairs(cards: list):
    pass


def high_card(cards: list):
    max_card = Card('2', 'H')
    for card in cards:
        if card > max_card:
            max_card = card

    return max_card
