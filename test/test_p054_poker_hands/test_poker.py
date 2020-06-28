"""
Poker game classes.
"""

import pytest


@pytest.mark.parametrize('test_input_poker_card_string,expected_result_value,expected_result_suit', [
    ('2D', '2', 'Diamonds'),
    ('4D', '4', 'Diamonds'),
    ('6S', '6', 'Spades'),
    ('9H', '9', 'Hearts'),
    ('TC', 'Ten', 'Clubs'),
    ('QC', 'Queen', 'Clubs'),
    ('JC', 'Jack', 'Clubs'),
    ('QH', 'Queen', 'Hearts'),
    ('KD', 'King', 'Diamonds'),
    ('AS', 'Ace', 'Spades'),
])
def test_poker_card_value_and_suit(test_input_poker_card_string, expected_result_value, expected_result_suit):
    # arrange
    from src.p054_poker_hands.poker import PokerCard

    # act
    test_poker_card = PokerCard(test_input_poker_card_string)

    # assert
    assert test_poker_card.value == expected_result_value
    assert test_poker_card.suit == expected_result_suit


@pytest.mark.parametrize('test_input_poker_card_1_string,test_input_poker_card_2_string,expected_result', [
    ('2D', '4D', True),
    ('4D', '2D', False),
    ('2D', '2H', False),
    ('4D', 'TC', True),
    ('QH', 'JS', False),
    ('KS', 'AD', True),
    ('3C', 'KH', True),
    ('JH', 'JD', False),
])
def test_poker_card_ordering_lt(test_input_poker_card_1_string, test_input_poker_card_2_string, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerCard

    # act
    test_poker_card_1 = PokerCard(test_input_poker_card_1_string)
    test_poker_card_2 = PokerCard(test_input_poker_card_2_string)

    # assert
    assert (test_poker_card_1 < test_poker_card_2) == expected_result


@pytest.mark.parametrize('test_input_poker_card_1_string,test_input_poker_card_2_string,expected_result', [
    ('2D', '4D', False),
    ('4D', '2D', True),
    ('2D', '2H', False),
    ('4D', 'TC', False),
    ('QH', 'JS', True),
    ('KS', 'AD', False),
    ('3C', 'KH', False),
    ('JH', 'JD', False),
])
def test_poker_card_ordering_gt(test_input_poker_card_1_string, test_input_poker_card_2_string, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerCard

    # act
    test_poker_card_1 = PokerCard(test_input_poker_card_1_string)
    test_poker_card_2 = PokerCard(test_input_poker_card_2_string)

    # assert
    assert (test_poker_card_1 > test_poker_card_2) == expected_result


@pytest.mark.parametrize('test_input_poker_card_1_string,test_input_poker_card_2_string,expected_result', [
    ('2D', '4D', False),
    ('4D', '2D', False),
    ('2D', '2H', True),
    ('4D', 'TC', False),
    ('QH', 'JS', False),
    ('KS', 'AD', False),
    ('3C', 'KH', False),
    ('JH', 'JD', True),
])
def test_poker_card_ordering_eq(test_input_poker_card_1_string, test_input_poker_card_2_string, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerCard

    # act
    test_poker_card_1 = PokerCard(test_input_poker_card_1_string)
    test_poker_card_2 = PokerCard(test_input_poker_card_2_string)

    # assert
    assert (test_poker_card_1 == test_poker_card_2) == expected_result


def test_poker_hand_initialization_success():
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    # act
    actual_result = PokerHand(['4D', '2D', 'AH', 'QC', 'QD'])

    # assert
    expected_result = [
        {
            'value': '2',
            'suit': 'Diamonds',
        },
        {
            'value': '4',
            'suit': 'Diamonds',
        },
        {
            'value': 'Queen',
            'suit': 'Clubs',
        },
        {
            'value': 'Queen',
            'suit': 'Diamonds',
        },
        {
            'value': 'Ace',
            'suit': 'Hearts',
        },
    ]
    for actual_poker_card, expected_poker_card in zip(actual_result.cards, expected_result):
        assert actual_poker_card.value == expected_poker_card['value']
        assert actual_poker_card.suit == expected_poker_card['suit']


def test_poker_hand_initialization_fail():
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    # act and assert
    with pytest.raises(ValueError):
        actual_result = PokerHand(['4D', '2D', 'AH', 'QC'])


@pytest.mark.parametrize('test_input_poker_hand_1_card_strings,test_input_poker_hand_2_card_strings,expected_result', [
    (['5H', '5C', '6S', '7S', 'KD'], ['2C', '3S', '8S', '8D', 'TD'], True),
    (['5D', '8C', '9S', 'JS', 'AC'], ['2C', '5C', '7D', '8S', 'QH'], False),
    (['2D', '9C', 'AS', 'AH', 'AC'], ['3D', '6D', '7D', 'TD', 'QD'], True),
    (['4D', '6S', '9H', 'QH', 'QC'], ['3D', '6D', '7H', 'QD', 'QS'], False),
    (['2H', '2D', '4C', '4D', '4S'], ['3C', '3D', '3S', '9S', '9D'], False),
])
def test_poker_hand_ordering_lt(test_input_poker_hand_1_card_strings, test_input_poker_hand_2_card_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    # act
    test_poker_hand_1 = PokerHand(test_input_poker_hand_1_card_strings)
    test_poker_hand_2 = PokerHand(test_input_poker_hand_2_card_strings)

    # assert
    assert (test_poker_hand_1 < test_poker_hand_2) == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['TH', 'JH', 'QH', 'KH', 'AH'], {'Hearts'}),
    (['AD', 'JD', 'KD', 'QD', 'TD'], {'Diamonds'}),
    (['TH', 'JH', 'QD', 'KH', 'AH'], {'Hearts', 'Diamonds'}),
    (['4D', '2D', 'AH', 'QC', 'QS'], {'Diamonds', 'Hearts', 'Clubs', 'Spades'}),
    (['3S', '5S', 'AS', 'JS', 'TS'], {'Spades'}),
])
def test_poker_hand_get_suit_set(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand._get_suit_set()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['TH', 'JH', 'QH', 'KH', 'AH'], 'Ten'),
    (['AD', 'JD', 'KD', 'QD', 'TD'], 'Ten'),
    (['TH', 'JH', 'QD', 'KH', 'AH'], 'Ten'),
    (['2H', '3H', '4H', '5H', '6H'], '2'),
    (['4D', '2D', 'AH', 'QC', 'QS'], None),
    (['3S', '5S', 'AS', 'JS', 'TS'], None),
])
def test_poker_hand_get_consecutive_values_start(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand._get_consecutive_values_start()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['TH', 'JH', 'QH', 'KH', 'AH'], { 1: ['Ace', 'King', 'Queen', 'Jack', 'Ten'] }),
    (['AD', 'JD', 'KD', 'QD', 'TD'], { 1: ['Ace', 'King', 'Queen', 'Jack', 'Ten'] }),
    (['TH', 'JH', 'QD', 'KH', 'AH'], { 1: ['Ace', 'King', 'Queen', 'Jack', 'Ten'] }),
    (['2H', '3H', '4H', '5H', '6H'], { 1: ['6', '5', '4', '3', '2'] }),
    (['QC', 'QH', 'QD', '3H', 'QS'], { 4: ['Queen'], 1: ['3'] }),
    (['QC', 'QH', 'QD', '3H', '3S'], { 3: ['Queen'], 2: ['3'] }),
    (['QC', 'KH', 'QD', '3H', 'QS'], { 3: ['Queen'], 1: ['King', '3'] }),
    (['QD', 'KC', 'QH', 'KH', 'AH'], { 2: ['King', 'Queen'], 1: ['Ace'] }),
    (['4D', '2D', 'AH', '2C', 'QD'], { 2: ['2'], 1: ['Ace', 'Queen', '4'] }),
    (['3S', '5S', 'AS', 'JS', 'TS'], { 1: ['Ace', 'Jack', 'Ten', '5', '3'] }),
])
def test_poker_hand_get_same_value_cards_map(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand._get_same_value_cards_map()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['TH', 'JH', 'QH', 'KH', 'AH'], True),
    (['AD', 'JD', 'KD', 'QD', 'TD'], True),
    (['TH', 'JH', 'QD', 'KH', 'AH'], False),
    (['TH', 'JH', 'QH', 'QC', 'AH'], False),
    (['2H', '3H', '4H', '5H', '6H'], False),
    (['9H', 'TH', 'JH', 'QH', 'KH'], False),
    (['4D', '2D', 'AH', 'QC', 'QD'], False),
    (['3S', '5S', 'AS', 'JS', 'TS'], False),
])
def test_poker_hand_is_royal_flush(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.is_royal_flush()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['TH', 'JH', 'QH', 'KH', 'AH'], 'Ten'),
    (['AD', 'JD', 'KD', 'QD', 'TD'], 'Ten'),
    (['TH', 'JH', 'QD', 'KH', 'AH'], None),
    (['TH', 'JH', 'QH', 'QC', 'AH'], None),
    (['2H', '3H', '4H', '5H', '6H'], '2'),
    (['9H', 'TH', 'JH', 'QH', 'KH'], '9'),
    (['4D', '2D', 'AH', 'QC', 'QD'], None),
    (['3S', '5S', 'AS', 'JS', 'TS'], None),
])
def test_poker_hand_is_straight_flush(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.is_straight_flush()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['QC', 'QH', 'QD', '3H', 'QS'], 'Queen'),
    (['QC', 'QH', 'QD', '3H', '3S'], None),
    (['QC', 'KH', 'QD', '3H', 'QS'], None),
    (['QD', 'KC', 'QH', 'KH', 'AH'], None),
    (['4D', '2D', 'AH', '2C', 'QD'], None),
    (['3S', '5S', 'AS', 'JS', 'TS'], None),
])
def test_poker_hand_is_four_of_a_kind(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.is_four_of_a_kind()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['QC', 'QH', 'QD', '3H', 'QS'], None),
    (['QC', 'QH', 'QD', '3H', '3S'], ('Queen', '3')),
    (['QC', 'KH', 'QD', '3H', 'QS'], None),
    (['QD', 'KC', 'QH', 'KH', 'AH'], None),
    (['4D', '2D', 'AH', '2C', 'QD'], None),
    (['3S', '5S', 'AS', 'JS', 'TS'], None),
])
def test_poker_hand_is_full_house(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.is_full_house()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['TH', 'JH', 'QH', 'KH', 'AH'], ('Ace', 'King', 'Queen', 'Jack', 'Ten')),
    (['AD', 'JD', 'KD', 'QD', 'TD'], ('Ace', 'King', 'Queen', 'Jack', 'Ten')),
    (['TH', 'JH', 'QD', 'KH', 'AH'], None),
    (['TH', 'JH', 'QH', 'QC', 'AH'], None),
    (['2H', '3H', '4H', '5H', '6H'], ('6', '5', '4', '3', '2')),
    (['9H', 'TH', 'JH', 'QH', 'KH'], ('King', 'Queen', 'Jack', 'Ten', '9')),
    (['4D', '2D', 'AH', 'QC', 'QD'], None),
    (['3S', '5S', 'AS', 'JS', 'TS'], ('Ace', 'Jack', 'Ten', '5', '3')),
])
def test_poker_hand_is_flush(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.is_flush()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['TH', 'JH', 'QH', 'KH', 'AH'], 'Ten'),
    (['AD', 'JD', 'KD', 'QD', 'TD'], 'Ten'),
    (['TH', 'JH', 'QD', 'KH', 'AH'], 'Ten'),
    (['TH', 'JH', 'QH', 'QC', 'AH'], None),
    (['2H', '3H', '4H', '5H', '6H'], '2'),
    (['9H', 'TH', 'JH', 'QH', 'KH'], '9'),
    (['4D', '2D', 'AH', 'QC', 'QD'], None),
    (['3S', '5S', 'AS', 'JS', 'TS'], None),
])
def test_poker_hand_is_straight(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.is_straight()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['QC', 'QH', 'QD', '3H', 'QS'], None),
    (['QC', 'QH', 'QD', '3H', '3S'], 'Queen'),
    (['QC', 'KH', 'QD', '3H', 'QS'], 'Queen'),
    (['QD', 'KC', 'QH', 'KH', 'AH'], None),
    (['4D', '2D', 'AH', '2C', 'QD'], None),
    (['3S', '5S', 'AS', 'JS', 'TS'], None),
])
def test_poker_hand_is_three_of_a_kind(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.is_three_of_a_kind()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['QC', 'QH', 'QD', '3H', 'QS'], None),
    (['QC', 'QH', 'QD', '3H', '3S'], None),
    (['QC', 'KH', 'QD', '3H', 'QS'], None),
    (['QD', 'KC', 'QH', 'KH', 'AH'], ('King', 'Queen')),
    (['4D', '2D', 'AH', '2C', 'QD'], None),
    (['3S', '5S', 'AS', 'JS', 'TS'], None),
])
def test_poker_hand_is_two_pairs(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.is_two_pairs()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['QC', 'QH', 'QD', '3H', 'QS'], None),
    (['QC', 'QH', 'QD', '3H', '3S'], '3'),
    (['QC', 'KH', 'QD', '3H', 'QS'], None),
    (['QD', 'KC', 'QH', 'KH', 'AH'], None),
    (['4D', '2D', 'AH', '2C', 'QD'], '2'),
    (['3S', '5S', 'AS', 'JS', 'TS'], None),
])
def test_poker_hand_is_one_pair(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.is_one_pair()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['QC', 'QH', 'QD', '3H', 'QS'], ['3']),
    (['QC', 'QH', 'QD', '3H', '3S'], []),
    (['QC', 'KH', 'QD', '3H', 'QS'], ['King', '3']),
    (['QD', 'KC', 'QH', 'KH', 'AH'], ['Ace']),
    (['4D', '2D', 'AH', '2C', 'QD'], ['Ace', 'Queen', '4']),
    (['3S', '5S', 'AS', 'JS', 'TS'], ['Ace', 'Jack', 'Ten', '5', '3']),
])
def test_poker_hand_get_ordered_single_cards(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.get_ordered_single_cards()

    # assert
    assert actual_result == expected_result


@pytest.mark.parametrize('test_input_cards_strings,expected_result', [
    (['QC', 'QH', 'QD', '3H', 'QS'], ('Queen', 'Queen', 'Queen', 'Queen', '3')),
    (['QC', 'QH', 'QD', '3H', '3S'], ('Queen', 'Queen', 'Queen', '3', '3')),
    (['QC', 'KH', 'QD', '3H', 'QS'], ('King', 'Queen', 'Queen', 'Queen', '3')),
    (['QD', 'KC', 'QH', 'KH', 'AH'], ('Ace', 'King', 'King', 'Queen', 'Queen')),
    (['4D', '2D', 'AH', '2C', 'QD'], ('Ace', 'Queen', '4', '2', '2')),
    (['3S', '5S', 'AS', 'JS', 'TS'], ('Ace', 'Jack', 'Ten', '5', '3')),
])
def test_poker_hand_get_reverse_card_values(test_input_cards_strings, expected_result):
    # arrange
    from src.p054_poker_hands.poker import PokerHand

    poker_hand = PokerHand(test_input_cards_strings)

    # act
    actual_result = poker_hand.get_reverse_card_values()

    # assert
    assert actual_result == expected_result
