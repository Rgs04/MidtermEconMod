#Q1
import string

class TextProcessor:
    @staticmethod
    def find_words(filename):
        """
        Prints all the three-letter words in the file that start with 'b' or 'B'.
        """
        with open(filename, 'r') as f:
            for line in f:
                for p in string.punctuation:
                    line = line.replace(p, " ")
                for word in line.split():
                    if len(word) == 3 and word[0] in "Bb":
                        print(word)

#Q3
pip install numpy

import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(4, 4), index=[1, 2, 3, 4], columns=['a', 'b', 'c', 'd'])
print(df)

# Choose a row label and column name
row_label = 3
col_label = 'b'

#index
element_index = df[col_label][row_label]
print(f"1) Using df['{col_label}'][{row_label}]: {element_index}")

#loc
element_loc = df.loc[row_label, col_label]
print(f"2) Using df.loc[{row_label}, '{col_label}']: {element_loc}")

#iloc
element_iloc = df.iloc[2, 1]
print(f"3) Using df.iloc[2, 1]: {element_iloc}")

#Q5
import requests
import pandas as pd
import matplotlib.pyplot as plt

ticker = "GOOG"
url = f"https://raw.githubusercontent.com/itb-ie/midterm_data/refs/heads/main/{ticker}.csv"
with open("company.csv", "w") as f:
    f.write(requests.get(url).text)

df = pd.read_csv("company.csv", index_col="Date")
df.index = pd.to_datetime(df.index)

#Q5.1
n_rows = df.shape[0]
cols = list(df.columns)
closing_apr11 = df.loc["2025-04-11", "Close"]

print(f"Number of rows: {n_rows}")
print(f"Column names: {cols}")
print(f"Closing on 2025-04-11: {closing_apr11}")

#Q5.2
plt.figure(figsize=(20, 10))
plt.plot(df.index, df["Close"], linestyle="-", marker="o", ms=4)
plt.title(f"{ticker} Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close")
plt.grid(True)
plt.show()


#Q6
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = x**2 + 4*x + 10
min_y = y.min()
print(f"The minimum value of y is {min_y}")

#Q7
import numpy as np

a = np.arange(0, 12)
a = a.reshape(3, 4)
a = a + (a + 1)**2
print(a)

#Q8
class Card(object):
  RANKS = ["2","3",...,"A"]
  SUITS = ["♣","♦","♥","♠"]

  def __init__(self, suit, rank):
    # regular method: initializer
    if rank not in self.RANKS:
      raise ValueError("Invalid Rank")

    if suit not in self.SUITS:
      raise ValueError("Invalid Suit")

    self._suit = suit
    self._rank = rank

  def __str__(self):
    # magic method: called when you do str(card) or print(card)
    return f"{self._rank}{self._suit}"

  def __eq__(self, other):
    # magic method: called for card1 == card2
    return self.rank == other.rank

  def __gt__(self, other):
    # magic method: called for card1 > card2
    return (Card.RANKS.index(self.rank) >
        Card.RANKS.index(other.rank))
  @property

  def suit(self):
    return self._suit
  @property

  def rank(self):
    return self._rank

class Deck:

  def __init__(self):
    # regular method: builds the 52-card deck
    self._deck = [Card(s, r)
           for s in Card.SUITS
           for r in Card.RANKS]

  def shuffle(self):
    # regular method: shuffles in place
    random.shuffle(self._deck)

  def deal(self):
    # regular method: pops and returns the “top” card
    return self._deck.pop(0)

  def __str__(self):
    # magic method: called when you print(deck)
    return str(self._deck)

#Q9
num_iterations = 10000

import matplotlib.pyplot as plt
import random
from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    @property
    def number_matches(self):
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        return self.number_matches == 2

    @property
    def is_trips(self):
        return self.number_matches == 6

    @property
    def is_full_house(self):
        # Full House = three of a kind + a pair
        return self.is_trips and self.is_pair

full_house_count = 0
x_vals = []
y_vals = []

for i in range(num_iterations):
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_full_house:
        full_house_count += 1
    x_vals.append(i + 1)
    y_vals.append(full_house_count / (i + 1) * 100)


plt.figure(figsize=(20, 10))
plt.plot(x_vals, y_vals)
plt.xlabel("Number of draws")
plt.ylabel("Probability of Full House (%)")
plt.title("Running Probability of Drawing a Full House")
plt.grid(True)
plt.show()

final_prob = full_house_count / num_iterations * 100
print(f"Final probability of a Full House: {final_prob:.4f}%")