#!python3
from valuev2 import value

'''
In Blackjack, the dealer always must follow the same rules.

1. They will stand pat (not take new cards) if their score is over 16
2. They will automatically take a new card if their score is less than 17
'''

def dealer(deck):
  dealer = []
  t = deck.copy()
  score = 0
  ''' 
  inputs:
  list deck: contains a shuffled list of cards
  return:
  list of lists:
  list[0] : the dealer's hand
  list[1] : the dealer's count
  list[2] : the remaining deck
  
  function will keep drawing a card from the deck until they have a score > 16
  You may need to use the function in problem 2 to count the score
  it will then return a list
  '''

  draw = 0

  print(t)
  print(t[draw])
  dealer.append(t[draw])
  t.pop(draw)

  score = value(dealer)
  

  if score < 16:
    for i in range(len(t)):
      if score > 16:
        return [dealer, score, t]

      else:
          dealer.append(t[0])
          t.pop(0)
          score = value(dealer)
  

def main():
  deck = ['3C', '3S', '8S', '3D', 'AC', '9H', 'QC', 'TD', 'TH', '8H', '8D', '7C', 'TS', '7D', 'AD', 'QD', 'KC', '6H', 'JH', 'KH', 'QS', '6C', '4H', '7H', '5S', '2S', 'AS', 'AH', '5C', '2D', '2H', '6D', 'TC', '4C', 'JS', 'JC', 'KD', '2C', '4S', '3H', '5H', '7S', 'KS', '5D', 'QH', '6S', '8C', '9D', 'JD', '9S', '9C', '4D']
  run1 = dealer(deck)
  assert dealer(deck) == [['3C', '3S', '8S', '3D'], 17, run1[2] ]
  print(run1[2])
  run2 = dealer( run1[2] )
  assert dealer(run1[2]) == [['AC', '9H'], 20, run2[2]]

if __name__ == "__main__":
  main()
