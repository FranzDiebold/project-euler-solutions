"""
Poker game classes.
"""
# pylint: disable=protected-access

from functools import total_ordering
from typing import Iterable, Optional, Dict, Tuple, List, Set
from collections import defaultdict


@total_ordering
class PokerCard:
    """Class for handling poker cards."""

    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = 'Ten'
    JACK = 'Jack'
    QUEEN = 'Queen'
    KING = 'King'
    ACE = 'Ace'

    CLUBS = 'Clubs'
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'

    def __init__(self, poker_card_str: str) -> None:
        """Initialize poker card with string representation."""
        self.value = self._get_value(poker_card_str)
        self.suit = self._get_suit(poker_card_str)

    @property
    def _value(self) -> int:
        """Integer value for comparison purposes."""
        return self._get_int_value_for_value(self.value)

    @classmethod
    def _get_int_value_for_value(cls, value: str) -> int:
        """Get the integer value for a given card value."""
        value_string_to_int_map = {
            cls.TWO: 2,
            cls.THREE: 3,
            cls.FOUR: 4,
            cls.FIVE: 5,
            cls.SIX: 6,
            cls.SEVEN: 7,
            cls.EIGHT: 8,
            cls.NINE: 9,
            cls.TEN: 10,
            cls.JACK: 11,
            cls.QUEEN: 12,
            cls.KING: 13,
            cls.ACE: 14,
        }
        return value_string_to_int_map[value]

    def _get_value(self, poker_card_str: str) -> str:
        """Get card value from string."""
        string_to_value_map = {
            '2': self.TWO,
            '3': self.THREE,
            '4': self.FOUR,
            '5': self.FIVE,
            '6': self.SIX,
            '7': self.SEVEN,
            '8': self.EIGHT,
            '9': self.NINE,
            'T': self.TEN,
            'J': self.JACK,
            'Q': self.QUEEN,
            'K': self.KING,
            'A': self.ACE,
        }
        return string_to_value_map[poker_card_str[0]]

    def _get_suit(self, poker_card_str: str) -> str:
        """Get card suit from string."""
        string_to_suit_map = {
            'C': self.CLUBS,
            'H': self.HEARTS,
            'D': self.DIAMONDS,
            'S': self.SPADES,
        }
        return string_to_suit_map[poker_card_str[1]]

    def __lt__(self, other) -> bool:
        """Compare two poker cards regarding their value, if one is less than the other."""
        return self._value < other._value

    def __eq__(self, other) -> bool:
        """Compare two poker cards regarding their value for equality."""
        return self._value == other._value


@total_ordering
class PokerHand:
    """Class for handling poker hands, consisting of `NUMBER_OF_CARDS` `PokerCard`s."""

    NUMBER_OF_CARDS = 5

    def __init__(self, cards_strings: Iterable[str]) -> None:
        """Initialize poker hand with five poker cards encoded as strings."""
        cards = [PokerCard(card_string) for card_string in cards_strings]
        if len(cards) != self.NUMBER_OF_CARDS:
            raise ValueError(
                f'You need to initialize the poker hand with {self.NUMBER_OF_CARDS} poker cards!'
            )
        self.cards = sorted(cards, key=lambda card: card._value)

    @property
    def _value(self) -> str:
        """
        Get the value of a poker hand as a string for comparison purposes.
        The strings are of constant length, so you may perform a lexicographical comparison.
        """
        hand_value = ''

        poker_hand_properties = [
            (self.is_royal_flush, 1),
            (self.is_straight_flush, 1),
            (self.is_four_of_a_kind, 1),
            (self.is_full_house, 2),
            (self.is_flush, self.NUMBER_OF_CARDS),
            (self.is_straight, 1),
            (self.is_three_of_a_kind, 1),
            (self.is_two_pairs, 2),
            (self.is_one_pair, 1),
            (self.get_reverse_card_values, self.NUMBER_OF_CARDS),
        ]
        for property_function, num_places in poker_hand_properties:
            property_value = property_function()
            if property_value is True:
                property_places = '1'
            elif isinstance(property_value, tuple):
                property_places = ''.join(
                    [f'{PokerCard._get_int_value_for_value(pv):x}' for pv in property_value]
                )
            elif isinstance(property_value, str):
                property_places = f'{PokerCard._get_int_value_for_value(property_value):x}'
            else:
                property_places = num_places * '0'

            hand_value += property_places

        return hand_value

    def __lt__(self, other) -> bool:
        """Compare two poker hands if one is worse than the other."""
        return self._value < other._value

    def __eq__(self, other) -> bool:
        """Check if two poker hands are equal."""
        return self._value == other._value

    def _get_suit_set(self) -> Set[str]:
        """Get the set of suits in the poker hand."""
        return set(card.suit for card in self.cards)

    def _get_consecutive_values_start(self) -> Optional[str]:
        """
        Check if the poker hand consists of consecutive values only.
        Return the lowest value or `None` if it does not consist of consecutive values only.
        """
        for idx in range(len(self.cards) - 1):
            if self.cards[idx]._value + 1 != self.cards[idx + 1]._value:
                return None
        return self.cards[0].value

    def _get_same_value_cards_map(self) -> Dict[int, List[str]]:
        """
        Get all sets of same cards as map `{ <n of a kind> : [value1, value2] }`.
        The values list is ordered by value descending.
        Examples:
        - One pair: { 2: ['Ten'] }
        - Two pairs: { 2: ['Queen', '6'] }
        - Three of a kind: { 3: ['Jack'] }
        - Four of a kind: { 4: ['King'] }
        - Three of a kind and a pair (Full House): { 2: ['Ace'], 3: ['8'] }
        """
        reverse_cards_map = defaultdict(int)
        for card in self.cards:
            reverse_cards_map[card.value] += 1

        same_value_cards_map = defaultdict(list)
        for card_value, count in reverse_cards_map.items():
            same_value_cards_map[count].append(card_value)

        for count in same_value_cards_map.keys():
            same_value_cards_map[count] = sorted(
                same_value_cards_map[count],
                key=PokerCard._get_int_value_for_value,
                reverse=True
            )

        return same_value_cards_map

    def is_royal_flush(self) -> bool:
        """Check for Royal Flush: Ten, Jack, Queen, King, Ace, in same suit."""
        return self.is_straight_flush() == PokerCard.TEN

    def is_straight_flush(self) -> Optional[str]:
        """
        Check for Straight Flush: All cards are consecutive values of same suit.
        Return the lowest value of straight flush, or `None` else.
        """
        if len(self._get_suit_set()) == 1:
            return self._get_consecutive_values_start()
        return None

    def is_four_of_a_kind(self) -> Optional[str]:
        """
        Check for Four of a Kind: Four cards of the same value.
        Return the value of these four cards, or `None` else.
        """
        return self._get_same_value_cards_map().get(4, [None])[0]

    def is_full_house(self) -> Optional[Tuple[str, str]]:
        """
        Check for Full House: Three of a kind and a pair.
        Return the tuple `(<value of three of a kind>, <value of pair>)`, or `None` else.
        """
        same_value_cards_map = self._get_same_value_cards_map()
        if 3 in same_value_cards_map and 2 in same_value_cards_map:
            return (same_value_cards_map[3][0], same_value_cards_map[2][0])
        return None

    def is_flush(self) -> Optional[Tuple[str, ...]]:
        """
        Check for Flush: All cards of the same suit.
        Return the card values ordered by value descending, or `None` else.
        """
        if len(self._get_suit_set()) == 1:
            return self.get_reverse_card_values()
        return None

    def is_straight(self) -> Optional[str]:
        """Check for Straight: All cards are consecutive values."""
        return self._get_consecutive_values_start()

    def is_three_of_a_kind(self) -> Optional[str]:
        """
        Check for Three of a Kind: Three cards of the same value.
        Return the value of these three cards, or `None` else.
        """
        return self._get_same_value_cards_map().get(3, [None])[0]

    def is_two_pairs(self) -> Optional[Tuple[str, str]]:
        """
        Check for Two Pairs: Two different pairs.
        Return the set `{ <value of first pair>, <value of second pair> }`, or `None` else.
        """
        same_value_cards_map = self._get_same_value_cards_map()
        if len(same_value_cards_map.get(2, [])) == 2:
            return tuple(same_value_cards_map[2])
        return None

    def is_one_pair(self) -> Optional[str]:
        """
        Check for One Pair: Two cards of the same value.
        Return the value of the pair, or `None` else.
        """
        same_value_cards_map = self._get_same_value_cards_map()
        if len(same_value_cards_map.get(2, [])) == 1:
            return same_value_cards_map[2][0]
        return None

    def get_ordered_single_cards(self) -> List[str]:
        """Get all single cards of the poker hand ordered by value descending."""
        return self._get_same_value_cards_map().get(1, [])

    def get_reverse_card_values(self) -> Tuple[str, ...]:
        """Get the poker hand card values ordered by value descending."""
        return tuple(card.value for card in self.cards[::-1])
