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
invalid_choices = []

def step_machine_choice():
    global invalid_choices
    print("\nPlayer2 move..")
    time.sleep(2)
    choice = [random.randint(0, 2) for i in range(2)]
    while choice in invalid_choices:
        choice = [random.randint(0, 2) for i in range(2)]

    invalid_choices.append(choice)
    return choice

def choice_side():
    global Player1Char
    global Player2Char
    inpt = input("Hello please choice sid [0] or [+]: ")
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
    global invalid_choices
    choice = [int(i) for i in input("Enter step: ").split(",")]
    if choice in invalid_choices:
        print("\ninvalid input")
    else:
        invalid_choices.append(choice)
        return choice

def input_handling(input_choice, char):
    global board
    board[input_choice[0]][input_choice[1]] = char

def check_win():
    global state
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '|':
            state = True
            win_message(board[i][1])
        elif board[i][0] == board[i][1] == board[i][2] != '|':
            state = True
            win_message(board[i][1])
        elif board[0][0] == board[1][1] == board[2][2] != '|':
            state = True
            win_message(board[1][1])
        elif board[0][0] == board[1][1] == board[2][2] != '|':
            state = True
            win_message(board[1][1])

def win_message(winChar):
    print(f"\n{winChar} vyhrál!\n")


def play():
    choice_side()
    while not state:
        print_Board(board)
        input_handling(step_input_choice(), Player1Char)
        input_handling(step_machine_choice(), Player2Char)
        check_win()


if __name__ == '__main__':
    play()








