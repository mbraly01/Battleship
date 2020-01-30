import model
import time

time_sleep = 5
def print_board_for_player(board):
    for i in range(0, len(board)):
        string = ''
        for j in range(0, len(board)):
            if board[i][j].is_ship == True:
                if board[i][j].is_hit == True:
                    string += '|&|'
                else:
                    string += '|+|'
            elif board[i][j].is_hit == True:
                string += '|#|'
            else:
                string += '|_|'
        print(string)
    
    time.sleep(time_sleep)

def print_board_for_enemy(board):
    for i in range(0, len(board)):
        string = ''
        for j in range(0, len(board)):
            if board[i][j].is_ship == True:
                if board[i][j].is_hit == True:
                    string += '|&|'
                else:
                    string += '|_|'
            elif board[i][j].is_hit == True:
                string += '|#|'
            else:
                string += '|_|'
        print(string)
    time.sleep(time_sleep)

def bad_input():
    print('Your input is bad')
    return

def place_ship():
    order_dict = {}
    order_dict['X'] = int(input('X coordinate '))
    order_dict['Y'] = int(input('Y coordinate '))
    order_dict['D'] = (input('Direction \n H for Horizontal, V for vertical')).upper()
    return order_dict


def place_orders():
    order_dict = {}
    order_dict['X'] = int(input('X coordinate '))
    order_dict['Y'] = int(input('Y coordinate '))
    return order_dict


