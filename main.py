import os
import random
import time

board = [' ']*9
user_token = 'X'
comp_token = 'O'
available_places = [0,1,2,3,4,5,6,7,8]
def print_board():
    print(f'''
| {board[0]} | {board[1]} | {board[2]} |
| {board[3]} | {board[4]} | {board[5]} |
| {board[6]} | {board[7]} | {board[8]} |
    ''')

def start_game(user_name,turn):
    print(f'Hi ! {user_name} your sign is {user_token} ')
    print(f'You are going to play against Ana the Bot ')
    print('GOOD LUCK!')

    if turn == 0:
        print('Your turn is first')
    else:
        print('Ana is going to take the first turn')


def user_turn():
    pos = int(input('Enter the place where you want to add X(Places 0-8): '))
    while pos>9 or pos <1 or board[pos-1] !=' ':
        if pos>9:
            pos = int(input('Enter a smaller number: '))
        elif pos < 1:
            pos = int(input('Enter a larger number: '))
        else:
            pos = int(input('Place already filled. Enter another place: '))
    available_places.remove(pos-1)
    board[pos-1] = user_token

def computer_turn():
    pos = random.randint(available_places[0],available_places[-1])
    board[pos] = comp_token

def check_winner():
    if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X'or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X' or board[2]==board[4]==board[6]=='X':
        print('''
        User Wins Congratulations !''')
        return True
    elif board[0]==board[1]==board[2]=='O' or board[3]==board[4]==board[5]=='O' or board[6]==board[7]==board[8]=='O' or board[0]==board[3]==board[6]=='O'or board[1]==board[4]==board[7]=='O' or board[2]==board[5]==board[8]=='O' or board[0]==board[4]==board[8]=='O' or board[2]==board[4]==board[6]=='O':
        print('''
        YOU LOOSE !
        COMPUTER WON
        BETTER LUCK NEXT TIME''')
        return True
    else:
        return False

game_end = False
turn = random.randint(0,1)
user_name = input('Enter your name: ')
start_game(user_name,turn)
time.sleep(2)
while game_end == False:
    if turn == 0:
        user_turn()
        game_end = check_winner()
        turn = 1
    else:
        computer_turn()
        game_end = check_winner()
        turn = 0

    print('NEXT TURN')
    os.system('cls')
    time.sleep(1)
    print_board()

