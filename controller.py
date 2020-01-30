import model
import view
import os

b_size = 3
ship_space_count = 1
board = model.Board(b_size, ship_space_count)
board2 = model.Board(b_size, ship_space_count)
list_ships = [model.Ship(1), model.Ship(5)]

print('Player 1 place ship')
for i in list_ships:
    order_dict = view.place_ship()
    while board.board_check(i, order_dict['X'], order_dict['Y'], order_dict['D'], b_size) != True:
        view.bad_input()
        order_dict = view.place_ship()
    board.place_ship(i, order_dict['X'], order_dict['Y'], order_dict['D'])

view.print_board_for_player(board)
os.system('clear')

print('Player 2 place ships')
for i in list_ships:
    order_dict = view.place_ship()
    while board2.board_check(i, order_dict['X'], order_dict['Y'], order_dict['D'], b_size) != True:
        view.bad_input()
        order_dict = view.place_ship()
    board2.place_ship(i, order_dict['X'], order_dict['Y'], order_dict['D'])
view.print_board_for_player(board2)
os.system('clear')

player_1_wins = None
while board.ship_space_count > 0 or board2.ship_space_count > 0:
    print('Player 1 turn')
    view.print_board_for_player(board)
    print('Enemy board')
    view.print_board_for_enemy(board2)
    order_dict = view.place_orders()
    while board2[order_dict['X']][order_dict['Y']].is_hit == True:
        view.bad_input()
        order_dict = view.place_orders()
    board2[order_dict['X']][order_dict['Y']].is_hit = True
    view.print_board_for_enemy(board2)
    os.system('clear')
    board2.ship_space_counter(ship_space_count)
    print(board2.board_tiles[0][0])
    print(board2.ship_space_count)
    if board2.ship_space_count == 0:
        player_1_wins = True
        break

    print('Player 2 turn')
    view.print_board_for_player(board2)
    print('Enemy board')
    view.print_board_for_enemy(board)
    order_dict = view.place_orders()
    while board[order_dict['X']][order_dict['Y']].is_hit == True:
        view.bad_input()
        order_dict = view.place_orders()
    board[order_dict['X']][order_dict['Y']].is_hit = True
    view.print_board_for_enemy(board)
    os.system('clear')
    board.ship_space_counter(ship_space_count)
    if board2.ship_space_count <= 0:
        if board.ship_space_count >= 0:
            player_1_wins = False
        break

if player_1_wins == True:
    print('Player 1 Wins!')
else:
    print("Player 2 Wins!")
    





