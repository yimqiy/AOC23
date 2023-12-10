def get_hand_strength(handbet):
    # Sort the hand by card labels
    hand = handbet[0].copy()
    
    v = hand[0]*1e-2+hand[1]*1e-4+hand[2]*1e-6+hand[3]*1e-8+hand[4]*1e-10
    
    if 1 in hand:
        #print(hand)
        hand.remove(1)
        return get_hand_joker_strength(hand,v)
    hand.sort()
    # Check for Five of a kind
    if len(set(hand)) == 1:
        return 8+v, hand[0]

    # Check for Four of a kind
    for card in set(hand):
        if hand.count(card) == 4:
            return 7+v, card

    # Check for Full house
    for card in set(hand):
        if hand.count(card) == 3:
            pair_value = [x for x in set(hand) if x != card][0]
            if hand.count(pair_value) == 2:
                return 6+v, card, pair_value

    # Check for Three of a kind
    for card in set(hand):
        if hand.count(card) == 3:
            other_cards = [x for x in set(hand) if x != card]
            return 5+v, card, max(other_cards), min(other_cards)

    # Check for Two pair
    pairs = [card for card in set(hand) if hand.count(card) == 2]
    if len(pairs) == 2:
        other_card = [card for card in set(hand) if card not in pairs][0]
        return 4+v, max(pairs), min(pairs), other_card

    # Check for One pair
    for card in set(hand):
        if hand.count(card) == 2:
            other_cards = sorted([x for x in set(hand) if x != card], reverse=True)
            return 3+v, card, other_cards

    # High card
    return 2+v, sorted(hand, reverse=True)

def get_hand_joker_strength(hand,v):
    print(hand)
    if 1 in hand:
        hand.remove(1)
        return get_hand_joker_strength(hand,v)
    hand.sort()
    # Check for Five of a kind
    if len(set(hand)) < 2:
        return 8+v, []

    # Check for Four of a kind
    for card in set(hand):
        if hand.count(card) == len(hand)-1:
            return 7+v, card

    # Check for Full house
    #j1122, j1112, jj112, jj122
    if len(set(hand))==2:
        return 6+v, hand[0]

    #lowest possible for jj
    #123jj
    #1234j
    #1233j
    # Check for Three of a kind
    # Check for Two pair
    if len(set(hand)) < 4:
        return 5+v, hand[0]

    # Check for One pair
    return 3+v, sorted(hand, reverse=True)


def order_hands(hands):
    return sorted(hands, key=get_hand_strength, reverse=True)

def str2ordered_hand(card_string):
    # Define the mapping of card labels to their corresponding values
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    # Convert each character in the card string to its corresponding value
    ordered_list = [card_values[card] for card in card_string]

    return ordered_list

folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'
l=[]
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        parts = line.split()
        l.append((parts[0],int(parts[1])))
# Example usage
hands=[]
#l = ["33332","2AAAA","77888","77788","TTT98", "23432", "A23A4", "23456", "AAAAA", "AA8AA", "23332", ]
for a in l:
    hands.append((str2ordered_hand(a[0]),a[1]))
ordered_hands = order_hands(hands)
maxp = len(ordered_hands)
N=0
for i,g in enumerate(ordered_hands):
    print(maxp-i,g)
    N+=(maxp-i)*g[1]
print(N)