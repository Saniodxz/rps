import sys
from io import StringIO
from unittest.mock import patch
from rock_paper_scissors_game import play_game
from itertools import cycle


def run_game_with_mocked_inputs(inputs):
    output = StringIO()
    sys.stdout = output
    
    with patch('builtins.input', side_effect=inputs):
        play_game()
    
    sys.stdout = sys.__stdout__ 
    return output.getvalue()

def test_invalid_game_mode():
    user_inputs = [
        'invalid_mode',  
        'rps',           
        '1',             
        'rock'           
    ]
    output = run_game_with_mocked_inputs(user_inputs)
    
    if "Invalid choice, try again." in output:
        print("Test Passed: The game correctly handled an invalid game mode input for rps.")
    else:
        print("Test Failed: The game did not handle the invalid game mode input correctly for rps.")

    user_inputs = [
        'invalid_mode',  
        'rps',           
        '1',             
        'rock'           
    ]
    output = run_game_with_mocked_inputs(user_inputs)
    
    if "Invalid choice, try again." in output:
        print("Test Passed: The game correctly handled an invalid game mode input for rpsls.")
    else:
        print("Test Failed: The game did not handle the invalid game mode input correctly for rpsls")



def test_number_of_rounds_input():

    user_inputs_invalid = [
        'rps',       
        'two',       
        '2.5',       
        'a',         
        '3',         
        'rock',      
        'paper',     
        'scissors'   
    ]
    
    output = run_game_with_mocked_inputs(user_inputs_invalid)
    
    invalid_input_count = output.count("Invalid input, please enter a valid integer number of rounds.")
    
    # print(output)
    
    # The game prints "invalid input" 3 times before accepting the valid '3'
    if invalid_input_count == 3:
        print("Test Passed: The game handled invalid round inputs correctly.")
    else:
        print(f"Test Failed: Expected 3 invalid round inputs, but got {invalid_input_count}.")


def test_invalid_input_handling():

    user_inputs = [
        'rps',   
        '5',     
        'invalid_choice',  
        'rock',  
        'invalid',  
        'paper',  
        'scissors',  
        'rock',  
        'invalid_choice',  
        'paper'  
    ]
    
    output = run_game_with_mocked_inputs(user_inputs)
    
    # count prints
    invalid_input_count = output.count("Invalid choice, try again.")
    # print(output)
    
    if invalid_input_count == 3:
        print("Test Passed: The game handled invalid inputs correctly.")
    else:
        print(f"Test Failed: Expected 3 invalid inputs, but got {invalid_input_count}.")





def test_draw_conditions():

    with patch('random.choice', side_effect=cycle(['rock'])):
        user_inputs = [
            'rps',  
            '3',    
            'rock',  
            'rock', 
            'rock'  
        ]
        
        output = run_game_with_mocked_inputs(user_inputs)
        draw_count = output.count("Random Computer: It's a draw!")
        draw_count2 = output.count("Last Choice Computer: It's a draw!")
        # print(output)
        
        if draw_count == 3:
            print("Test Passed: The game correctly identified all draw conditions for random computer.")
        else:
            print(f"Test Failed: Expected 3 draws, but got {draw_count}.")

        if draw_count2 == 3:
            print("Test Passed: The game correctly identified all draw conditions for last move computer.")
        else:
            print(f"Test Failed: Expected 3 draws, but got {draw_count2}.")

def test_player_win_conditions():

    with patch('rock_paper_scissors_game.random_computer_choice', side_effect=cycle(['scissors', 'rock', 'paper'])):
        user_inputs = [
            'rps',  
            '3',    
            'rock',  
            'paper', 
            'scissors'
        ]
        
        output = run_game_with_mocked_inputs(user_inputs)

        player_win_count_random = output.count("Random Computer: You win!")
        # print(output)
        if player_win_count_random == 3:
            print("Test Passed: The game correctly identified all player win conditions.")
        else:
            print(f"Test Failed: Expected 3 wins from Random Computer but got {player_win_count_random}")

def test_computer_win_conditions():

    with patch('rock_paper_scissors_game.random_computer_choice', side_effect=cycle(['rock', 'paper', 'scissors'])):
        user_inputs = [
            'rps',  
            '3',   
            'scissors',  
            'rock',  
            'paper'  
        ]
        
        output = run_game_with_mocked_inputs(user_inputs)
        computer_win_count = output.count("Random Computer: You lose!")
        # print(output)
        
        if computer_win_count == 3:
            print("Test Passed: The game correctly identified all random computer win conditions.")
        else:
            print(f"Test Failed: Expected 3 computer wins, but got {computer_win_count}.")

def test_last_choice_computer_win_conditions():

    user_inputs = [
            'rps',     
            '3',        
            'rock',     
            'scissors', 
            'paper'     
        ]
        
    output = run_game_with_mocked_inputs(user_inputs)
        

    last_choice_computer_win_count = output.count("Last Choice Computer: You lose!")
    last_choice_computer_draw_count = output.count("Last Choice Computer: It's a draw!")
    # print(output)
        
    if last_choice_computer_win_count == 2 and last_choice_computer_draw_count == 1:
            print("Test Passed: The game correctly identified all Last Choice Computer win conditions.")
    else:
            print(f"Test Failed: Expected 2 Last Choice Computer wins and 1 draw, but got {last_choice_computer_win_count} and {last_choice_computer_draw_count}")

def test_rps_and_rpsls_modes():

    user_inputs_rps = ['rps', '1', 'rock']
    user_inputs_rpsls = ['rpsls', '1', 'spock']
    
    # test RPS mode
    rps_output = run_game_with_mocked_inputs(user_inputs_rps)
    
    # test RPSLS mode
    rpsls_output = run_game_with_mocked_inputs(user_inputs_rpsls)
    
    # print the results
    print("RPS Mode Output:\n", rps_output)
    print("RPSLS Mode Output:\n", rpsls_output)
    
    if "--- Round 1" in rps_output and "--- Round 1" in rpsls_output:
        print("Test Passed: Both 'rps' and 'rpsls' modes are functioning correctly.")
    else:
        print("Test Failed: One or both modes are not functioning correctly.")


def test_rpsls_rules_agasint_random():
    with patch('rock_paper_scissors_game.random_computer_choice', side_effect=cycle(['spock', 'scissors', 'rock', 'lizard', 'spock'])):
        user_inputs = [
            'rpsls',  
            '5',     
            'rock',  
            'scissors',
            'rock',   
            'scissors', 
            'paper'   
        ]
        
        output = run_game_with_mocked_inputs(user_inputs)

        player_win_count_random = output.count("Random Computer: You win!")
        player_loss_count_random = output.count("Random Computer: You lose!")
        draw_count_random = output.count("Random Computer: It's a draw!")
        # print(output)
        
        if player_win_count_random == 2 and player_loss_count_random == 1 and draw_count_random == 2:
            print("Test Passed: The game correctly identified all win, loss, and draw conditions for Random Computer in RPSLS mode.")
        else:
            print(f"Test Failed: Expected 2 wins, 1 loss, and 2 draws for Random Computer but got {player_win_count_random} wins, {player_loss_count_random} losses, and {draw_count_random} draws.")

        if "You won against the Random Computer!" in output or "You lost against the Random Computer." in output:
            print("Test Passed: The game correctly calculated the overall winner against the Random Computer.")
        else:
            print("Test Failed: The game did not calculate the overall winner correctly against the Random Computer.")


def test_rpsls_rules_agasint_last():

    user_inputs = [
            'rpsls',
            '5',   
            'paper', 
            'rock',    
            'scissors',
            'rock',   
            'spock'    
        ]
        
    output = run_game_with_mocked_inputs(user_inputs)
    player_win_count_last = output.count("Last Choice Computer: You win!")
    player_loss_count_last = output.count("Last Choice Computer: You lose!")
    draw_count_last = output.count("Last Choice Computer: It's a draw!")
    # print(output)
    

    if player_win_count_last == 3 and player_loss_count_last == 2 and draw_count_last == 0:
            print("Test Passed: The game correctly identified all win, loss, and draw conditions for Last Choice Computer in RPSLS mode.")
    else:
            print(f"Test Failed: Expected 2 wins, 3 losses, and 0 draws for Last Choice Computer but got {player_win_count_last} wins, {player_loss_count_last} losses, and {draw_count_last} draws.")


    if "You won against the Last Choice Computer!" in output or "You lost against the Last Choice Computer." in output:
            print("Test Passed: The game correctly calculated the overall winner against the Last Choice Computer.")
    else:
            print("Test Failed: The game did not calculate the overall winner correctly against the Last Choice Computer.")


def test_overall_winner():

    with patch('rock_paper_scissors_game.random_computer_choice', side_effect=cycle(['scissors', 'paper', 'scissors'])):
        user_inputs = [
            'rps',     
            '3',        
            'rock',    
            'scissors',  
            'paper'      
        ]
        
        output = run_game_with_mocked_inputs(user_inputs)
        # print(output)
        
        if "You won against the Random Computer!" in output:
            print("Test Passed: The game correctly identified the overall player as the winner in odd rounds.")
        else:
            print("Test Failed: The game did not correctly identify the overall winner in odd rounds.")
    with patch('rock_paper_scissors_game.random_computer_choice', side_effect=cycle(['scissors', 'paper','paper', 'scissors'])):
        user_inputs = [
            'rps',    
            '4',       
            'rock',    
            'scissors', 
            'scissors', 
            'paper'     
        ]
        
        output = run_game_with_mocked_inputs(user_inputs)
        # print(output)
        
        if "You won against the Random Computer!" in output:
            print("Test Passed: The game correctly identified the overall player as the winner in even rounds.")
        else:
            print("Test Failed: The game did not correctly identify the overall winner in even rounds.")
    with patch('rock_paper_scissors_game.random_computer_choice', side_effect=cycle(['scissors', 'paper', 'scissors','scissors'])):
        user_inputs = [
            'rps',   
            '4',     
            'rock',     
            'scissors', 
            'paper',     
            'paper'     
        ]
        
        output = run_game_with_mocked_inputs(user_inputs)
        # print(output)
        
        if "It's a draw against the Random Computer!" in output:
            print("Test Passed: The game correctly identified the draw  in even rounds.")
        else:
            print("Test Failed: The game did not correctly identify the draw in even rounds.")
    with patch('rock_paper_scissors_game.random_computer_choice', side_effect=cycle(['scissors'])):
        user_inputs = [
            'rps',      
            '1',        
            'rock',      
        ]
        
        output = run_game_with_mocked_inputs(user_inputs)
        # print(output)
        
        if "You won against the Random Computer!" in output:
            print("Test Passed: The game correctly identified the overall player as the winner in one round.")
        else:
            print("Test Failed: The game did not correctly identify the overall winner in one round.")

    with patch('rock_paper_scissors_game.random_computer_choice', side_effect=cycle(['rock'])):
        user_inputs = [
            'rps',      
            '1',         
            'rock',      
        ]
        
        output = run_game_with_mocked_inputs(user_inputs)
        # print(output)
        
        if "It's a draw against the Random Computer!" in output:
            print("Test Passed: The game correctly identified the draw")
        else:
            print("Test Failed: The game did not correctly identify the draw.")



if __name__ == "__main__":
    test_invalid_game_mode()
    test_invalid_input_handling()
    test_number_of_rounds_input()
    test_draw_conditions()
    test_player_win_conditions()
    test_computer_win_conditions()
    test_last_choice_computer_win_conditions()
    test_rps_and_rpsls_modes()
    test_overall_winner()
    test_invalid_game_mode()
    test_rpsls_rules_agasint_random()
    test_rpsls_rules_agasint_last()