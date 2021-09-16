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


def move_down_and_right(direction):
    move_down_or_right(direction)
    add_elements_down_or_right(direction)
    move_down_or_right(direction)


def move_down_or_right(direction):
    i = 2
    while i >= 0:
        j = 0
        while j < 4:
            temp_i = i
            if direction == "down":
                while temp_i < 3 and check_free_space(temp_i+1, j):
                    board[temp_i + 1][j] = board[temp_i][j]
                    board[temp_i][j] = 0
                    temp_i += 1
            elif direction == "right":
                while temp_i < 3 and check_free_space(j, temp_i+1):
                    board[j][temp_i+1] = board[j][temp_i]
                    board[j][temp_i] = 0
                    temp_i += 1
            j += 1
        i -= 1


def add_elements_down_or_right(direction):
    global score
    i = 2
    while i >= 0:
        j = 0
        while j < 4:
            if direction == "down":
                if board[i][j] == board[i+1][j]:
                    board[i+1][j] += board[i][j]
                    board[i][j] = 0
                    score += board[i+1][j]
            elif direction == "right":
                if board[j][i] == board[j][i+1]:
                    board[j][i+1] += board[j][i]
                    board[j][i] = 0
                    score += board[j][i+1]
            j += 1
        i -= 1


def move_up_and_left(direction):
    move_up_or_left(direction)
    add_elements_up_or_left(direction)
    move_up_or_left(direction)


def move_up_or_left(direction):
    i = 1
    while i < 4:
        j = 0
        while j < 4:
            temp_i = i
            if direction == "up":
                while temp_i > 0 and check_free_space(temp_i-1, j):
                    board[temp_i - 1][j] = board[temp_i][j]
                    board[temp_i][j] = 0
                    temp_i -= 1
            if direction == "left":
                while temp_i > 0 and check_free_space(j, temp_i-1):
                    board[j][temp_i - 1] = board[j][temp_i]
                    board[j][temp_i] = 0
                    temp_i -= 1
            j += 1
        i += 1


def add_elements_up_or_left(direction):
    global score
    i = 1
    while i < 4:
        j = 0
        while j < 4:
            if direction == "up":
                if board[i][j] == board[i-1][j]:
                    board[i-1][j] += board[i][j]
                    board[i][j] = 0
                    score += board[i-1][j]
            if direction == "left":
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
            if board[i][j] == 16:
                return True
    return False


def check_free_space(i, j):
    return board[i][j] == 0


def check_high_score():
    if not score in high_scores:
        if score > high_scores[0]:
            high_scores[2] = high_scores[1]
            high_scores[1] = high_scores[0]
            high_scores[0] = score
        elif score > high_scores[1]:
            high_scores[2] = high_scores[1]
            high_scores[1] = score
        elif score > high_scores[2]:
            high_scores[2] = score


def initialize_game():
    global score
    score = 0
    for i in range(4):
        for j in range(4):
            board[i][j] = 0


def main():
    initialize_game()
    clear()
    add_random_element()
    while True:
        print(f"\n\t\t\tHigh scores :   1. {high_scores[0]}\n\t\t\t\t\t" + \
                f"2. {high_scores[1]}\n\t\t\t\t\t3. {high_scores[2]}\n")
        show_board()
        print(f"\n\t\t\tScore : {score}")
        print("\n\t\t\tDown : s , Up : w , right : d , left : a , Quit : q")
        choice = input("\n\t\t\tEnter your choice : ").lower()
        clear()
        
        if choice == "s":
            move_down_and_right("down")
        elif choice == "w":
            move_up_and_left("up")
        elif choice == "d":
            move_down_and_right("right")
        elif choice == "a":
            move_up_and_left("left")
        elif choice == "q":
            exit()
        else:
            print("\n\t\t\tWrong input! Try again!\n")

        if check_win():
            show_board()
            print("\n\t\t\tYou won!")
            print(f"\n\t\t\tScore : {score}")
            check_high_score()
            while True:
                choice = input("\n\t\t\tDo you want to continue? (y/n) ").lower()
                if choice == 'y':
                    main()
                elif choice == 'n':
                    exit()
                else:
                    print("\n\t\t\tWrong input! Try again!\n")
        
        if check_game_over():
            print("\n\t\t\tYou lost!")
            exit()
        else:
            add_random_element()


if __name__ == "__main__":
    main()