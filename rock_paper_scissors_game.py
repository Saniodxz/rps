import random

# Rock Paper Scissors rules
rps_rules = {
    'rock': ['scissors'],
    'paper': ['rock'],
    'scissors': ['paper']
}

# Rock Paper Scissors Lizard Spock rules
rpsls_rules = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock']
}

#modes
def print_options(game_mode):
    if game_mode == 'rps':
        print("Options: rock, paper, scissors")
    else:
        print("Options: rock, paper, scissors, lizard, spock")

def get_user_choice(game_mode):
    while True:
        print_options(game_mode)
        choice = input("Your choice: ").lower()
        if game_mode == 'rps' and choice in rps_rules.keys():
            return choice
        elif game_mode == 'rpsls' and choice in rpsls_rules.keys():
            return choice
        else:
            print("Invalid choice, try again.")

# Random computer
def random_computer_choice(game_mode):
    if game_mode == 'rps':
        return random.choice(list(rps_rules.keys()))
    else:
        return random.choice(list(rpsls_rules.keys()))

# Last Choice computer
def last_choice_computer(last_human_choice):
    if last_human_choice:
        return last_human_choice
    else:
        return 'rock'


def determine_winner(player_choice, computer_choice, game_mode):
    rules = rps_rules
    if game_mode == 'rps':
        rules = rps_rules
    else:
        rules = rpsls_rules
    
    if player_choice == computer_choice:
        return 'draw'
    elif computer_choice in rules[player_choice]:
        return 'player'
    else:
        return 'computer'


def play_game():
    print("Welcome to Rock Paper Scissors (or the Big Bang version)!")
    
    # Choose game mode
    while True:
        game_mode = input("Choose your game mode: 'rps' for Rock Paper Scissors or 'rpsls' for Rock Paper Scissors Lizard Spock: ").lower()
        if game_mode in ['rps', 'rpsls']:
            break
        else:
            print("Invalid choice, try again.")
    
    # Ask for number of rounds with input validation
    while True:
        rounds_input = input("Best out of how many rounds? ")
        # Check if input is a valid integer
        if rounds_input.isdigit():
            rounds = int(rounds_input)
            break
        else:
            print("Invalid input, please enter a valid integer number of rounds.")

    # counters for both Random ccomputer and Last Choice computer
    player_wins_random = 0
    computer_wins_random = 0
    draws_random = 0
    player_wins_last = 0
    computer_wins_last = 0
    draws_last = 0
    last_human_choice = None

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        
        user_choice = get_user_choice(game_mode)
        computer_choice_random = random_computer_choice(game_mode)
        computer_choice_last = last_choice_computer(last_human_choice)
        
        print(f"Your choice: {user_choice}")
        print(f"Random Computer choice: {computer_choice_random}")
        print(f"Last Choice Computer choice: {computer_choice_last}")
 
        result_random = determine_winner(user_choice, computer_choice_random, game_mode)
        if result_random == 'draw':
            print("Random Computer: It's a draw!")
            draws_random += 1
        elif result_random == 'player':
            print("Random Computer: You win!")
            player_wins_random += 1
        else:
            print("Random Computer: You lose!")
            computer_wins_random += 1

        result_last = determine_winner(user_choice, computer_choice_last, game_mode)
        if result_last == 'draw':
            print("Last Choice Computer: It's a draw!")
            draws_last += 1
        elif result_last == 'player':
            print("Last Choice Computer: You win!")
            player_wins_last += 1
        else:
            print("Last Choice Computer: You lose!")
            computer_wins_last += 1
        
        last_human_choice = user_choice
    
    #overall winner
    print("\n--- Game Over: Random Computer ---")
    if player_wins_random > computer_wins_random:
        print(f"You won against the Random Computer! You: {player_wins_random} | Random Computer: {computer_wins_random} | Draws: {draws_random}")
    elif computer_wins_random > player_wins_random:
        print(f"You lost against the Random Computer. You: {player_wins_random} | Random Computer: {computer_wins_random} | Draws: {draws_random}")
    else:
        print(f"It's a draw against the Random Computer! You: {player_wins_random} | Random Computer: {computer_wins_random} | Draws: {draws_random}")

    print("\n--- Game Over: Last Choice Computer ---")
    if player_wins_last > computer_wins_last:
        print(f"You won against the Last Choice Computer! You: {player_wins_last} | Last Choice Computer: {computer_wins_last} | Draws: {draws_last}")
    elif computer_wins_last > player_wins_last:
        print(f"You lost against the Last Choice Computer. You: {player_wins_last} | Last Choice Computer: {computer_wins_last} | Draws: {draws_last}")
    else:
        print(f"It's a draw against the Last Choice Computer! You: {player_wins_last} | Last Choice Computer: {computer_wins_last} | Draws: {draws_last}")

    print("\nThanks for playing!")

if __name__ == "__main__":
    play_game()
