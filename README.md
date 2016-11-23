# Markov-Text-Generator-Dynamic-Feedlength

My take on a Markov-Chain based text generator. 
Storage.py is used for the behind the scenes hashmaps which store word counts and handle probabilities
Chain.py contains the Chain class
  The Chain object takes in a feedlength(explained) and a text file
  The Chain object then calculates the probability of every single world appearing based on the last few words (feedlength)
  Longer feedlengths will cause the chain to generate text that is more natural but also closer to the source,
  while shorter feedlengths will create more original text that will have substantially more grammatical errors.
Chain.py also contains the MultiChain class
  A Multichain object stores four Chain objects with feedlengths of 5,4,3 and 2
  It first tries to generate a word from the the largest feedlength chain, but drops to the next lowest chain if it doesn't have sufficient diversity
  At the moment, "sufficient" diversity is defined as having at least 2 viable options but I plan on finding a better algorithm down the the road
