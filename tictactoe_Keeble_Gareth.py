import random
field = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
]
turns = 0

user = True  # true means X's turn


def get_computer_turn():
    unused_square = 0

    while True:
        square = random.randint(1, 9)
        if not is_used_square(square):
            unused_square = square
            break

    return unused_square




def print_field(field):
    for row in field:
        for slot in row:
            print(f"{slot} ", end="")
        print()


print("You have been challenged to a game of tic tac toe!")


def quit_game(user_input):
    if user_input == "flee":
        print("You bravely run away")
        return True
    else: return False


def check_input(user_input):
    if not is_number(user_input): return False
    user_input = int(user_input)
    if not bounds(user_input): return False

    return True


def is_number(user_input):
    if not user_input.isnumeric():
        print("This is not an acceptable number")
        return False
    else: return True


def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of the range of acceptable inputs")
        return False
    else: return True


def is_used_square(square):
    co_ords = coordinates(square)

    return is_taken(co_ords, field)



def is_taken(co_ords, field):
    row = co_ords[0]
    col = co_ords[1]
    if field[row][col] !="*":
        print("This spot has already been claimed!")
        return True
    else: return False


def coordinates(user_input):
    user_input = (user_input - 1) # user input has to be 0-8 for this function to work, but user enters 1-9
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return row, col


def add_to_field(co_ords, field, active_user):
    row = co_ords[0]
    col = co_ords[1]
    field[row][col] = active_user


def current_user(user):
    if user: return "X"
    else: return "O"


def victory(user, field):
    if check_row(user, field): return True
    if check_column(user, field): return True
    if check_diag(user, field): return True


def check_row(user, field):
    for row in field:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False


def check_column(user, field):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if field[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False


def check_diag(user, field):
    #  top left to the bottom right spaces
    if field[0][0] == user and field[1][1] == user and field[2][2] == user: return True
    #  top right to bottom left
    elif field[0][2] == user and field[1][1] == user and field[2][0] == user: return True
    else: return False


while turns < 9:
    active_user = current_user(user)
    print_field(field)
    if user:
        user_input = input("Enter the space you'd like to claim, 1-9 or enter \"flee\" to flee like a coward: ")
        if not check_input(user_input):
            print("Please try a different input")
            continue
    else:
        user_input = get_computer_turn()
        print("The computer has chosen: ", user_input)

    if quit_game(user_input):
        break

    user_input = int(user_input)
    co_ords = coordinates(user_input)
    # makes the inputs line up with the array
    if is_taken(co_ords, field):
        print("Please try another space.")
        continue
    add_to_field(co_ords, field, active_user)
    if victory(active_user, field):
        print_field(field)
        print(f"{active_user} is victorious!")

        break
    turns += 1
    if turns == 9:
        print("Tie game")
    user = not user
