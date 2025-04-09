## Nim Game (Human vs CPU)

Welcome to **Nim**, a classic strategy game where you play against the CPU in a battle of sticks! Try to be the last one to make a move—depending on the rules you choose.

---

###  Game Description

In this version of Nim:

- There are **4 rows** of sticks: `[1, 3, 5, 7]`.
- Players take turns removing **one or more sticks** from a single row.
- The player who **takes the last stick** either **wins or loses**, depending on your choice before the game starts.

---

### Features

- Random player goes first (you or CPU).
- CPU makes random valid moves.
- You decide if the last player to take a stick is the **winner or loser**.
- Option to play multiple rounds.
- Tracks your total **wins and losses**.
- Includes delays for better game pacing.

---

###  How to Run

1. Ensure you have Python installed (version 3+).
2. Save the code as `nim_game.py`.
3. Run the game in your terminal or command line:

```bash
python nim_game.py
```

---

###  How to Play

1. Enter your name.
2. Choose the rule for the last stick:
   - `w` – Whoever takes the last stick **wins**.
   - `l` – Whoever takes the last stick **loses**.
3. On your turn:
   - Choose a **row number (1-4)**.
   - Choose how many **sticks** to take from that row.
4. The CPU will make its move automatically.
5. The game ends when all sticks are taken.
6. Play again or exit.

---

###  Example Gameplay

```
Welcome to Nim!
Enter name: Alex
Do you want the player that picked the last stick to be winner (w) or loser (l)? Enter w or l: w
Game is starting... CPU will go first!

Current stick layout:
1.| 
2.|||
3.|||||
4.|||||||

CPU takes 2 sticks from row 4

Which row would you like to take sticks from? 3
How many sticks would you like to take? 2
Alex takes 2 sticks from row 3
...
Game Over!
Winner is Alex
You have won 1 time(s) and lost 0 time(s).
Would you like to play again? Enter y or n:

