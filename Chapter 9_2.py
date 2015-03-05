#Chapter 9_2.py
#By: Karlos Calvillo
#3/5/15
#in collaboration with Tom Morrissey and Karl Pearson

import random

RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
SUITS = ["c", "d", "h", "s"]

player1=0
player2=0

player1Name=input("Enter name: ")
player2Name=input("Enter name: ")

while player1 <10 and player2 <10:
    player1RankIndex=random.randrange(len(RANKS))
    player1Rank=RANKS[player1RankIndex]
    player1Suit=random.choice(SUITS)
    player1Card=player1Rank+player1Suit

    player2RankIndex=random.randrange(len(RANKS))
    player2Rank=RANKS[player2RankIndex]
    player2Suit=random.choice(SUITS)
    player2Card=player2Rank+player2Suit
    print(player1Name, ":", player1Card)
    print(player2Name, ":", player2Card)
    if player1RankIndex > player2RankIndex:
        print(player1Name, "has won this round and gained one point.")
        player1 += 1
    elif player2RankIndex > player1RankIndex:
        print(player2Name, "has won this round and gained one point.")
        player2 += 1
    else:
        print("Oh no, its a tie. Nobody wins a point.")
    print(player1Name, ":", player1)
    print(player2Name, ":", player2)
    input("press enter for the next round")
if player1 >9:
    print(player1Name, "has won this game and is much better than you")

else:
    print(player2Name, "has won this game and is much better than you")

