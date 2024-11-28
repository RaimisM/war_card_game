War - A Children’s Card Game
This project implements the classic children’s card game War using the Object-Oriented Programming (OOP) paradigm. 


1. Set up:
    a) Create a function to initialize a deck of cards (52 cards: 13 ranks × 4 suits).
    b) Write a shuffle function to randomize the deck.
    c) Split the deck into two equal piles for Player 1 and Player 2.

2. Gameplay:
    a) Implement a loop for the turn structure:
    b) Each player draws the top card from their stack.
    c) Compare the values of the two drawn cards.
    d) Add both cards to the winner's pile (bottom of their deck).

3. Tiebreake solution:
    Check if drawn cards are of equal value:
        a) Place three additional cards face-down.
        b) Draw a fourth card to compare values.
        c) Repeat this process if the tiebreaker cards are also tied.
        d) Add all cards in play to the winner's pile.

4. Find winner:
    a) Check if one player’s stack is empty (loses the game).
    b) Implement a check for total card ownership to declare a winner.
    c) Write congratulation message