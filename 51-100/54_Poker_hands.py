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


def is_one_pairs(cards: list):
    couter, current, max_counter = 0, cards[0], 0

    for card in cards:
        if card == current:
            couter += 1
        else:
            current = card
            if couter > max_counter:
                max_counter = couter
            couter = 1
    if max_counter > couter:
        return max_counter == 2
    else:
        return couter == 2


def one_pairs(cards: list):
    if is_one_pairs(cards):
        couter, current, max_counter, n = 0, cards[0], 0, 0

        for card in cards:
            if card == current:
                couter += 1
            else:
                if couter > max_counter:
                    max_counter = couter
                    n = current.get_number()
                current = card
                couter = 1
        if max_counter > couter:
            return n
        else:
            return cards[4].get_number()


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


def straight_flush(cards: list):
    if is_straight_flush(cards):
        return cards[3].get_number()


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


def four_of_a_kind(cards: list):
    if is_four_of_a_kind(cards):
        return cards[3].get_number()


def is_full_house(cards: list):
    repeat, indexs = 0, []

    for i in range(0, len(cards)):
        if cards[i].get_number() == 13:
            repeat += 1
            indexs.append(cards[i])
    for x in indexs:
        cards.remove(x)

    if repeat == 3 and is_one_pairs(cards):
        return True
    return False


def full_house(cards: list):
    repeat, indexs = 0, []
    for i in range(0, len(cards)):
        if cards[i].get_number() == 13:
            repeat += 1
            indexs.append(cards[i])
    for x in indexs:
        cards.remove(x)

    return one_pairs(cards)


def is_flush(cards: list):
    start_suit = cards[0].suit

    for card in cards:
        if card.suit != start_suit:
            return False
    return True


def is_straight(cards: list):
    start_number, start_suit = cards[0].get_number(), cards[0].suit
    for card in cards:
        if card.get_number() == start_number:
            start_number += 1
            continue
        else:
            return False
    return True


def straight(cards: list):
    if is_straight_flush(cards):
        return cards[0].get_number()


def is_three_of_a_kind(cards: list):
    couter, current, max_counter = 0, cards[0], 0

    for card in cards:
        if card == current:
            couter += 1
        else:
            current = card
            if couter > max_counter:
                max_counter = couter
            couter = 1
    if max_counter > couter:
        return max_counter == 3
    else:
        return couter == 3


def three_of_a_kind(cards: list):
    couter, current, max_counter, n = 0, cards[0], 0, 0

    for card in cards:
        if card == current:
            couter += 1
        else:
            if couter > max_counter:
                max_counter = couter
                n = current.get_number()
            current = card
            couter = 1
    if max_counter > couter:
        return n
    else:
        return cards[4].get_number()


def is_two_pairs(cards: list):
    couter, current, max_counter, repeat = 0, cards[0], 0, 0

    for card in cards:
        if card == current:
            couter += 1
        else:
            current = card
            if couter == 2:
                repeat += 1
            couter = 1
    if couter == 2:
        repeat += 1
    return repeat == 2


def two_pairs(cards: list):
    pass


def high_card(cards: list):
    max_card = Card('2', 'H')
    for card in cards:
        if card > max_card:
            max_card = card

    return max_card


hands = []
f = open('p054_poker.txt')
for line in f.readlines():
    hands.append(line.split('\n')[0].split(' '))

for hand in hands:
    player1 = []
    player2 = []
    for i in range(0, 5):
        player1.append(hand[i])
    for i in range(5, 10):
        player2.append(hand[i])
