import random
import time
board = [
    ["|", "|", "|"],
    ["|", "|", "|"],
    ["|", "|", "|"]
]
state = False
Player1Char = " "
Player2Char = " "

def step_machine_choice():
    print("\nPlayer2 move..")
    time.sleep(1)
    choice = [random.randint(0, 2) for i in range(2)]
    while board[choice[0]][choice[1]] == Player1Char:
        choice = [random.randint(0, 2) for i in range(2)]
    return choice

def choice_side():
    global Player1Char
    global Player2Char
    inpt = input("Ahoj, vyber si [0] nebo [+]: ")
    Player1Char = inpt
    if inpt == "0":
        Player2Char = "+"
    else:
        Player2Char = "0"
def print_Board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def step_input_choice():
    choice = [int(i) for i in input("Enter: ").split(",")]
    while board[choice[0]][choice[1]] == Player2Char:
        choice = [int(i) for i in input("je obsazeno napiste jeste: ").split(",")]
    return choice

def input_handling(input_choice, char):
    global board
    board[input_choice[0]][input_choice[1]] = char

def check_for_plr1_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == Player1Char:
            return True
        elif board[i][0] == board[i][1] == board[i][2] == Player1Char:
            return True
        elif board[0][0] == board[1][1] == board[2][2] == Player1Char:
            return True
        elif board[2][2] == board[1][1] == board[0][0] == Player1Char:
            return True
        else:
            return False
def check_for_plr2_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == Player2Char:
            return True
        elif board[i][0] == board[i][1] == board[i][2] == Player2Char:
            return True
        elif board[0][0] == board[1][1] == board[2][2] == Player2Char:
            return True
        elif board[2][2] == board[1][1] == board[0][0] == Player2Char:
            return True
        else:
            return False

def play():
    choice_side()
    while not state:
        print_Board(board)
        input_handling(step_input_choice(), Player1Char)
        input_handling(step_machine_choice(), Player2Char)
        if check_for_plr1_win():
            print(f"\n{Player1Char} VYHRAL!")
        elif check_for_plr2_win():
            print(f"\n{Player2Char} VYHRAL!")
        elif check_for_plr1_win() and check_for_plr2_win:
            print("\nREMIZA!!!")
        else:
            continue

if __name__ == '__main__':
    play()








