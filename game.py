from os import system, name

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
            print(str(board[i][j]), end=" ")
        print()
    print()


def move_down():
    pass


def move_up():
    pass


def move_right():
    pass


def move_left():
    pass


def check_game_over():
    pass


def check_win():
    pass


def check_free_space():
    pass


def main():
    clear()
    while True:
        show_board()
        print(f"\n\t\t\tScore : {score}")
        print("\n\t\t\tDown : d , Up : u , right : r , left : l")
        choice = input("\n\t\t\tEnter your choice : ")
        clear()

        if choice.lower() == "d":
            move_down()
        elif choice.lower() == "u":
            move_up()
        elif choice.lower() == "r":
            move_right()
        elif choice.lower() == "l":
            move_left()
        else:
            print("\n\t\t\tWrong input! Try again!\n")

        check_win()
        check_game_over()


if __name__ == "__main__":
    main()