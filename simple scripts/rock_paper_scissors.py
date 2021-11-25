"""
A simple script for the popular game Rock, Paper, Scissors
"""
import random


def random_player_pick(li: list):
    """
    Picks 'Rock', 'Paper' or 'Scissors' for the random CPU player
    :param li: list of the valid actions ('Rock', 'Paper', 'Scissors')
    :type li: list
    :return: the selected action for the random CPU player
    :rtype: str
    """
    return random.choice(li)


def rocker_player_pick(li: list):
    """
    Picks 'Rock', 'Paper' or 'Scissors' for the Rocker CPU player
    Has a higher chance of picking 'Rock' than 'Paper' or 'Scissors'
    :param li: list of the valid actions ('Rock', 'Paper', 'Scissors')
    :type li: list
    :return: the selected action for the Rocker CPU player
    :rtype: str
    """
    return random.choices(population=li, weights=[50, 25, 25], k=1)[0]


def cutter_player_pick(li: list):
    """
    Picks 'Rock', 'Paper' or 'Scissors' for the Cutter CPU player
    Has a higher chance of picking 'Scissors' than 'Rock' or 'Paper'
    :param li: list of the valid actions ('Rock', 'Paper', 'Scissors')
    :type li: list
    :return: the selected action for the Cutter CPU player
    :rtype: str
    """
    return random.choices(population=li, weights=[25, 25, 50], k=1)[0]


def paperer_player_pick(li: list):
    """
    Picks 'Rock', 'Paper' or 'Scissors' for the Paperer CPU player
    Has a higher chance of picking 'Paper' than 'Rock' or 'Scissors'
    :param li: list of the valid actions ('Rock', 'Paper', 'Scissors')
    :type li: list
    :return: the selected action for the Paperer CPU player
    :rtype: str
    """
    return random.choices(population=li, weights=[25, 50, 25], k=1)[0]


def select_winner(player_action: str, cpu_action: str):
    """
    Based on the selected actions (choices), finds the winner of the game
    :param player_action: the player's choice
    :param cpu_action: the CPU player's choice
    :returns:
        - 0: if draw
        - 1: if the player wins
        - -1: if the CPU player wins
    :rtype: int
    """
    if player_action == cpu_action:
        return 0
    elif (player_action == 'Rock' and cpu_action == 'Scissors') or (player_action == 'Paper' and cpu_action == 'Rock')\
            or (player_action == 'Scissors' and cpu_action == 'Paper'):
        return 1
    else:
        return -1


if __name__ == '__main__':
    actions = ['Rock', 'Paper', 'Scissors']
    player_name = input('Enter your name: ')
    list_of_cpu_players = ['Random Player', 'Rocker', 'Cutter', 'Paperer']

    print(f'Welcome {player_name}!')
    while True:
        random_cpu = random.choice(list_of_cpu_players)
        print(f'You will be playing against {random_cpu}')
        while True:
            player_choice = input('Select \'Rock\', \'Paper\' or \'Scissors\': ')
            if player_choice == 'Rock' or player_choice == 'Paper' or player_choice == 'Scissors':
                break
            else:
                print('Invalid input')
                continue
        if random_cpu == 'Random Player':
            cpu_choice = random_player_pick(actions)
        elif random_cpu == 'Rocker':
            cpu_choice = rocker_player_pick(actions)
        elif random_cpu == 'Paper':
            cpu_choice = paperer_player_pick(actions)
        else:
            cpu_choice = cutter_player_pick(actions)

        result = select_winner(player_choice, cpu_choice)
        print('You chose: ' + player_choice)
        print(f'{random_cpu} chose: {cpu_choice}')
        if result == 0:
            print('It\'s a draw! Play again? (y/n)')
        elif result == 1:
            print('Congratulations! You win! Play again? (y/n)')
        else:
            print('CPU player wins! Play again? (y/n)')
        char = input()
        if char == 'y':
            continue
        else:
            print('Game over!')
            break
