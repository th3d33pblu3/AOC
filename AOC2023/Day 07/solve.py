from collections import Counter
from functools import cmp_to_key

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def isFiveOfAKind(hand: str) -> bool:
    cc = Counter(hand)
    return 5 in cc.values()

def isFourOfAKind(hand: str) -> bool:
    cc = Counter(hand)
    return 4 in cc.values()

def isFullhouse(hand: str) -> bool:
    cc = Counter(hand)
    return 3 in cc.values() and 2 in cc.values()

def isThreeOfAKind(hand: str) -> bool:
    cc = Counter(hand)
    return 3 in cc.values()

def isTwoPair(hand: str) -> bool:
    cc = Counter(hand)
    ccc = Counter(cc.values())
    return ccc[2] == 2

def isPair(hand: str) -> bool:
    cc = Counter(hand)
    return 2 in cc.values()

values = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
def sortSameHand(handBid1: tuple[str, int], handBid2: tuple[str, int]) -> int:
    hand1 = handBid1[0]
    hand2 = handBid2[0]
    for i in range(5):
        if hand1[i] != hand2[i]:
            return values[hand1[i]] - values[hand2[i]]
    return 0

def solve_part_1():
    kinds = {5: [], 4: [], 32: [], 3: [], 22: [], 2: [], 1: []}
    num_hands = 0
    for line in read_input_file_data().splitlines():
        hand, bid = line.split()
        num_hands += 1
        if isFiveOfAKind(hand):
            kinds[5].append((hand, int(bid)))
        elif isFourOfAKind(hand):
            kinds[4].append((hand, int(bid)))
        elif isFullhouse(hand):
            kinds[32].append((hand, int(bid)))
        elif isThreeOfAKind(hand):
            kinds[3].append((hand, int(bid)))
        elif isTwoPair(hand):
            kinds[22].append((hand, int(bid)))
        elif isPair(hand):
            kinds[2].append((hand, int(bid)))
        else:
            kinds[1].append((hand, int(bid)))
    
    winnings = 0
    for hand_type in [5, 4, 32, 3, 22, 2, 1]:
        ls = sorted(kinds[hand_type], key=cmp_to_key(sortSameHand), reverse=True)
        for hand, bid in ls:
            winnings += bid * num_hands
            num_hands -= 1
    
    return winnings

JOKER = 'J'

def isJokerFiveOfAKind(hand: str) -> bool:
    # Max 5 Jokers
    cc = Counter(hand)
    joker_count = cc.pop(JOKER, 0)
    return joker_count == 5 or 5 - joker_count in cc.values()

def isJokerFourOfAKind(hand: str) -> bool:
    # Max 3 Jokers
    cc = Counter(hand)
    joker_count = cc.pop(JOKER, 0)
    return joker_count == 3 or 4 - joker_count in cc.values()

def isJokerFullhouse(hand: str) -> bool:
    # Max 1 Joker
    cc = Counter(hand)
    joker_count = cc.pop(JOKER, 0)
    if joker_count == 1:
        ccc = Counter(cc.values())
        return ccc[2] == 2
    return 3 in cc.values() and 2 in cc.values()

def isJokerThreeOfAKind(hand: str) -> bool:
    # Max 2 Jokers
    cc = Counter(hand)
    joker_count = cc.pop(JOKER, 0)
    return 3 - joker_count in cc.values()

def isJokerTwoPair(hand: str) -> bool:
    # Max 0 Jokers
    cc = Counter(hand)
    ccc = Counter(cc.values())
    return ccc[2] == 2

def isJokerPair(hand: str) -> bool:
    cc = Counter(hand)
    joker_count = cc.pop(JOKER, 0)
    return 2 - joker_count in cc.values()

jokerValues = {'A':14, 'K':13, 'Q':12, 'J':1, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
def sortJokerSameHand(handBid1: tuple[str, int], handBid2: tuple[str, int]) -> int:
    hand1 = handBid1[0]
    hand2 = handBid2[0]
    for i in range(5):
        if hand1[i] != hand2[i]:
            return jokerValues[hand1[i]] - jokerValues[hand2[i]]
    return 0

def solve_part_2():
    kinds = {5: [], 4: [], 32: [], 3: [], 22: [], 2: [], 1: []}
    num_hands = 0
    for line in read_input_file_data().splitlines():
        hand, bid = line.split()
        num_hands += 1
        if isJokerFiveOfAKind(hand):
            kinds[5].append((hand, int(bid)))
        elif isJokerFourOfAKind(hand):
            kinds[4].append((hand, int(bid)))
        elif isJokerFullhouse(hand):
            kinds[32].append((hand, int(bid)))
        elif isJokerThreeOfAKind(hand):
            kinds[3].append((hand, int(bid)))
        elif isJokerTwoPair(hand):
            kinds[22].append((hand, int(bid)))
        elif isJokerPair(hand):
            kinds[2].append((hand, int(bid)))
        else:
            kinds[1].append((hand, int(bid)))
    
    winnings = 0
    for hand_type in [5, 4, 32, 3, 22, 2, 1]:
        ls = sorted(kinds[hand_type], key=cmp_to_key(sortJokerSameHand), reverse=True)
        for hand, bid in ls:
            winnings += bid * num_hands
            num_hands -= 1
    
    return winnings
    
print(solve_part_2())
