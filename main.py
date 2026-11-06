import random

# Function to determine the winner based on game rules
def determine_winner(comp_choice, user_choice):
    # If both choose the same, it's a tie
    if comp_choice == user_choice:
        return "Tie" 

    # Check all possible winning conditions for the user:
    # 's' (Stone) beats 'c' (Scissor) 
    # 'p' (Paper) beats 's' (Stone) 
    # 'c' (Scissor) beats 'p' (Paper) 
    elif (user_choice == 's' and comp_choice == 'c'):
        return "Win" 
    elif (user_choice == 'p' and comp_choice == 's'):
        return "Win"
    elif (user_choice == 'c' and comp_choice == 'p'):
        return "Win"  

    # If it's not a tie and the user didn't win, the computer wins
    else:
        return "Lose" 

# --- Main Game Loop ---
print("Welcome to Stone, Paper, Scissor!")
print("Enter 's' for Stone, 'p' for Paper, and 'c' for Scissor.")

# 1. Computer makes a random choice from the list
choices = ['s', 'p', 'c']
comp = random.choice(choices)

# 2. User makes a choice and convert it to lowercase for safety 
user = input("Your Turn: ").lower()

# Validate user input to ensure they entered a valid option
if user not in choices:
    print("Invalid choice! Please enter 's', 'p', or 'c'.")
else:
    # 3. Determine the result by comparing computer and user choices
    result = determine_winner(comp, user)

    # 4. Display what both players chose
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {comp}")

    # Display the final outcome based on the result
    if result == "Tie":
        print("Result: It's a Tie!")
    elif result == "Win":
        print("Result: You Win! ")
    else:
        print(f"Result: You Lose! ")
