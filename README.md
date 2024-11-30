# War - A Children’s Card Game

This project implements the classic children’s card game **War** using the Object-Oriented Programming (OOP) paradigm.

---

## Features

- Fully object-oriented implementation for clarity and scalability.
- Simulates the gameplay mechanics, including card drawing, tiebreaker handling, and winner determination.
- Randomized deck shuffling for dynamic gameplay.

---

## How It Works

### 1. Setup
- **Deck Initialization**: A deck of 52 cards is created (13 ranks × 4 suits).
- **Shuffle**: The deck is shuffled to ensure random card order.
- **Card Distribution**: The deck is split into two equal piles for Player 1 and Player 2.

---

### 2. Gameplay
- Each turn follows this sequence:
  1. Both players draw the top card from their stack.
  2. The values of the two cards are compared.
  3. The winner of the turn adds both cards to the bottom of their deck.

---

### 3. Tiebreaker Rules
If the drawn cards have the same value:
1. Each player places three additional cards face-down.
2. A fourth card is drawn by both players to determine the winner.
3. If the fourth cards are also tied, repeat the process until a winner is determined.
4. The winner collects all cards in play and adds them to their pile.

---

### 4. Determining the Winner
- A player loses when their stack is empty.
- A check is performed to ensure total card ownership to declare a winner.
- The game ends with a congratulatory message for the winner.

---


