from os import system, name
from random import randint


board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
score = 0
high_scores = [0, 0, 0]


def clear():
    if name == 'nt':
        _ = system('cls')  
    else:
        _ = system('clear')


def show_board():
    print()
    for i in range(4):
        print("\t\t\t\t\t", end="")
        for j in range(4):
            print("{0:6d}".format(board[i][j]), end=" ")
        print("\n")
    print()


def move_down():
    i = 2
    while i >= 0:
        j = 0
        while j < 4:
            temp_i = i
            while temp_i < 3 and check_free_space(temp_i+1, j):
                board[temp_i + 1][j] = board[temp_i][j]
                board[temp_i][j] = 0
                temp_i += 1
            j += 1
        i -= 1
    add_elements_down()
    i = 2
    while i >= 0:
        j = 0
        while j < 4:
            temp_i = i
            while temp_i < 3 and check_free_space(temp_i+1, j):
                board[temp_i + 1][j] = board[temp_i][j]
                board[temp_i][j] = 0
                temp_i += 1
            j += 1
        i -= 1


def add_elements_down():
    global score
    i = 2
    while i >= 0:
        j = 0
        while j < 4:
            if board[i][j] == board[i+1][j]:
                board[i+1][j] += board[i][j]
                board[i][j] = 0
                score += board[i+1][j]
            j += 1
        i -= 1


def move_up():
    i = 1
    while i < 4:
        j = 0
        while j < 4:
            temp_i = i
            while temp_i > 0 and check_free_space(temp_i-1, j):
                board[temp_i - 1][j] = board[temp_i][j]
                board[temp_i][j] = 0
                temp_i -= 1
            j += 1
        i += 1
    add_elements_up()
    i = 1
    while i < 4:
        j = 0
        while j < 4:
            temp_i = i
            while temp_i > 0 and check_free_space(temp_i-1, j):
                board[temp_i - 1][j] = board[temp_i][j]
                board[temp_i][j] = 0
                temp_i -= 1
            j += 1
        i += 1
    

def add_elements_up():
    global score
    i = 1
    while i < 4:
        j = 0
        while j < 4:
            if board[i][j] == board[i-1][j]:
                board[i-1][j] += board[i][j]
                board[i][j] = 0
                score += board[i-1][j]
            j += 1
        i += 1


def move_right():
    i = 2
    while i >= 0:
        j = 0
        while j < 4:
            temp_i = i
            while temp_i < 3 and check_free_space(j, temp_i+1):
                board[j][temp_i+1] = board[j][temp_i]
                board[j][temp_i] = 0
                temp_i += 1
            j += 1
        i -= 1
    add_elements_right()
    i = 2
    while i >= 0:
        j = 0
        while j < 4:
            temp_i = i
            while temp_i < 3 and check_free_space(j, temp_i+1):
                board[j][temp_i+1] = board[j][temp_i]
                board[j][temp_i] = 0
                temp_i += 1
            j += 1
        i -= 1


def add_elements_right():
    global score
    i = 2
    while i >= 0:
        j = 0
        while j < 4:
            if board[j][i] == board[j][i+1]:
                board[j][i+1] += board[j][i]
                board[j][i] = 0
                score += board[j][i+1]
            j += 1
        i -= 1


def move_left():
    i = 1
    while i < 4:
        j = 0
        while j < 4:
            temp_i = i
            while temp_i > 0 and check_free_space(j, temp_i-1):
                board[j][temp_i - 1] = board[j][temp_i]
                board[j][temp_i] = 0
                temp_i -= 1
            j += 1
        i += 1
    add_elements_left()
    i = 1
    while i < 4:
        j = 0
        while j < 4:
            temp_i = i
            while temp_i > 0 and check_free_space(j, temp_i-1):
                board[j][temp_i - 1] = board[j][temp_i]
                board[j][temp_i] = 0
                temp_i -= 1
            j += 1
        i += 1
    

def add_elements_left():
    global score
    i = 1
    while i < 4:
        j = 0
        while j < 4:
            if board[j][i] == board[j][i-1]:
                board[j][i-1] += board[j][i]
                board[j][i] = 0
                score += board[j][i-1]
            j += 1
        i += 1


def check_game_over():
    for i in range(4):
        for j in range(4):
            if check_free_space(i, j):
                return False
    
    return True


def add_random_element():
    while True:
        i = randint(0, 3)
        j = randint(0, 3)
        if check_free_space(i, j):
            board[i][j] = 2
            break
    

def check_win():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                return True
    
    return False


def check_free_space(i, j):
    return board[i][j] == 0


def main():
    clear()
    add_random_element()
    while True:
        show_board()
        print(f"\n\t\t\tScore : {score}")
        print("\n\t\t\tDown : s , Up : w , right : d , left : a")
        choice = input("\n\t\t\tEnter your choice : ").lower()
        clear()

        if choice == "s":
            move_down()
        elif choice == "w":
            move_up()
        elif choice == "d":
            move_right()
        elif choice == "a":
            move_left()
        else:
            print("\n\t\t\tWrong input! Try again!\n")

        add_random_element()
        if check_win():
            print("\n\t\t\tYou won!")
        if check_game_over():
            print("\n\t\t\tYou lost!")
            exit()


if __name__ == "__main__":
    main()