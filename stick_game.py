import random
import time

# Define the print_move function
def print_move(current_player, row, stick_quantity):
    if stick_quantity == 1:
        print(f"{current_player} takes {stick_quantity} stick from row {row}")
    else:
        print(f"{current_player} takes {stick_quantity} sticks from row {row}")

print("Welcome to Nim!")
user = input("Enter name: ")
wins = 0
losses = 0

# Game loop
running_game = True
while running_game:
    decision = input("Do you want the player that picked the last stick to be winner (w) or loser (l)? Enter w or l: ").lower()
    sticks = [1, 3, 5, 7]
    player = [user, "CPU"]
    current_player = random.choice(player)
    print(f"Game is starting... {current_player} will go first!")

    # Game round
    while sum(sticks) > 0:
        # Display current stick configuration
        print("\nCurrent stick layout:")
        for row, stick in enumerate(sticks, start=1):
            width = len(sticks) - row
            space = ''
            print(str(row) + '.' + space.center(width) + '|' * stick)

        # User's turn
        if current_player == user:
            while True:
                try:
                    row = int(input("Which row would you like to take sticks from? "))
                    stick_quantity = int(input("How many sticks would you like to take? "))
                    if row in range(1, len(sticks) + 1) and stick_quantity in range(1, sticks[row - 1] + 1):
                        break
                    else:
                        print("Invalid row or stick number.")
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            print_move(current_player, row, stick_quantity)
            sticks[row - 1] -= stick_quantity
            current_player = "CPU"

        # CPU's turn
        else:
            while True:
                row = random.randint(1, len(sticks))
                if sticks[row - 1] == 0:
                    continue  # Skip empty rows
                stick_quantity = random.randint(1, sticks[row - 1])
                if stick_quantity > 0:
                    break

            time.sleep(2)
            print_move(current_player, row, stick_quantity)
            sticks[row - 1] -= stick_quantity
            current_player = user

    # End of game
    print("\nGame Over!")

    if decision == 'w':
        # Last player who played is the winner
        if current_player == "CPU":
            print(f"Winner is {user}")
            wins += 1
        else:
            print("Winner is CPU")
            losses += 1
    else:
        # Last player who played is the loser
        if current_player == "CPU":
            print("Winner is CPU")
            losses += 1
        else:
            print(f"Winner is {user}")
            wins += 1

    response = input("\nWould you like to play again? Enter y or n: ").lower()
    print(f"You have won {wins} time(s) and lost {losses} time(s).")

    if response != 'y':
        running_game = False

