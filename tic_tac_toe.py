#criação do jogo tic tac toe, mais conhecido como jogo da velha em modo console

import random


def display_board(board):

    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')

def player_input():

    marker = ' '
    while not marker == 'X' or marker =='O':
        marker = input('Player 1: Você quer ser X ou O ?').upper()

        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7]==mark and board[8]==mark and board[7]==mark) or
                 (board[4]==mark and board[5]==mark and board[6]==mark) or
                 (board[1]==mark and board[2]==mark and board[3]==mark) or
                 (board[1]==mark and board[5]==mark and board[9]==mark) or
                 (board[3]==mark and board[5]==mark and board[7]==mark) or
                 (board[2]==mark and board[5]==mark and board[8]==mark) or
                 (board[1]==mark and board[4]==mark and board[7]==mark) or
                 (board[3]==mark and board[6]==mark and board[9]==mark))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):

            return False

    return True

def player_choice(board):
    position = ' '

    while position is not '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position=int (input('Escolha sua jogada (1-9): '))

        return int(position)


def replay():
    return input('Quer jogar novamente? S/N: ').lower().startswith('s')

if __name__ == '__main__':
    print('Bem vindo ao jogo da velha!')

    while True:
        board = [' ']*10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' começa!')

        game_on = True

        while game_on:
            # jogardo 1
            if turn == 'Player 1':
                display_board(board)
                print('Vez do jogador 1')
                position = player_choice(board)
                place_marker(board, player1_marker, position)


            if win_check(board, player1_marker):
                display_board(board)
                print('Parabéns, Jogador 1!')
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print('Empate!')
                    break

                else:
                    turn = 'Player 2'

             # jogardo 2
            if turn == 'Player 2':
                    display_board(board)
                    print('Vez do jogador 2')
                    position = player_choice(board)
                    place_marker(board, player2_marker, position)


            if win_check(board, player2_marker):
                    display_board(board)
                    print('Parabéns, Jogador 2!')
                    game_on = False
            else:
                if full_board_check(board):
                     display_board(board)
                     print('Empate!')
                     break

                else:
                    turn = 'Player 1'



        if not replay():
             break