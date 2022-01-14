#!python3

"""
Create a list of cards
the cards should be denoted with a number or A, J, Q, K, T (for ace, jack, queen, king or ten)
as well as a suit
"""

def createDeck():
  ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['C','D','H','S']
  deck = []
  rankspot = 0
  suitspot = 0
  for i in range(52):
    deck.append(ranks[rankspot] + suits[suitspot])
    rankspot = rankspot + 1
    suitspot = suitspot + 1
    if rankspot == 13:
      rankspot = 0    
    if suitspot == 4:
      suitspot = 0
  
  return deck
  
  '''
  use the two lists to create a new list "deck" 
  return the deck list to your calling function
  '''

def main():
  deck = createDeck()
  assert "JH" in deck 
  assert "AC" in deck 
  assert "TD" in deck 
  assert len(deck) == 52
  
if __name__ == "__main__":
  main()
