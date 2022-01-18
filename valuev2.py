#!python3

def value(hand):
    total = 0
    ace = 0
    for i in range(len(hand)):
        if "2"  in hand[i]:
            total = total + 2
        elif "3"  in hand[i]:
            total = total + 3
        elif "4"  in hand[i]:
            total = total + 4
        elif "5"  in hand[i]:
            total = total + 5
        elif "6"  in hand[i]:
            total = total + 6
        elif "7"  in hand[i]:
            total = total + 7
        elif "8"  in hand[i]:
            total = total + 8
        elif "9"  in hand[i]:
            total = total + 9
        elif "T" in hand[i] or "K" in hand[i] or "Q" in hand[i] or "J" in hand[i]:
            total = total + 10
        elif "A" in hand[i]:
            ace = 1
    if ace == 1:
        if total + 10 > 21:
            total = total + 1
        else:
            total = total + 11
    return total