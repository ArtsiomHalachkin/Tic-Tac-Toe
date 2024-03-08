import random
import time

board = [
    ["|", "|", "|"],
    ["|", "|", "|"],
    ["|", "|", "|"]
]
state = False
winPlr1 = False
winPlr2 = False
Player1Char = ""
Player2Char = ""
invalid_choices = [9]

def set_default():
    state = False
    winPlr1 = False
    winPlr2 = False
    Player2Char = ""
    Player1Char = ""
    invalid_choices = []
def step_machine_choice():
    print("Player2 move..")
    time.sleep(3)
    choice = [random.randint(0, 2) for i in range(2)]
    invalid_choices.append(choice[0])
    invalid_choices.append(choice[1])
    return choice

def choice_side():
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
    choice = [int(i) for i in input("Enter step: ").split(",")]
    if (choice[0] in invalid_choices) or (choice[1] in invalid_choices):
        print("invalid input")
    else:
        invalid_choices.append(choice[0])
        invalid_choices.append(choice[1])
        return choice

def input_handling(input_choice, char):
    board[input_choice[0]][input_choice[1]] = char

def check_win():
    plr1 = 0
    plr2 = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == Player1Char:
                plr1 = plr1 + 1
                if plr1 == 3:
                    winPlr1 = True
                    state = True
            else:
                if board[i][j] == Player2Char:
                    plr2 = plr2 + 1
                    if plr2 == 3:
                        winPlr1 = True
                        state = True




def play():
    choice_side()
    while not state:
        print_Board(board)
        input_handling(step_input_choice(), Player1Char)
        input_handling(step_machine_choice(), Player2Char)
        check_win()



if __name__ == '__main__':
    set_default()
    play()








