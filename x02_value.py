#!python3

def value(hand):
  '''
  input:
  list hand: hand is a list of strings that contains the cards in the hand
  eg: ['AH','3D','4S']
  
  return:
  int the total value of the hand
  may return a list if the hand contains an Ace
  eg:
  '''
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
    acel = []
    total = total + 1
    acet = total + 10
    acel.append(total)
    acel.append(acet)
    return acel
  else:
    return total


def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__name__":
  main()