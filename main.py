import random

# from bullsandcows import bullsandcows
# game = bullsandcows()


def get_digits(num):
    return [int(i) for i in str(num)]


def no_duplicates(num):
    number = get_digits(num)
    if len(number) == len(set(number)):
        return True
    else:
        return False


def num_generator():
    while True:
        num = random.randint(1000, 9999)
        if no_duplicates(num):
            print(num)
            return num


def num_bull_cows(num, guess):
    bull_cow = [0, 0]
    secret_num = get_digits(num)
    guess_num = get_digits(guess)
    for index, digit in enumerate(guess_num):
        if digit == secret_num[index]: bull_cow[0] += 1
        elif digit in secret_num: bull_cow[1] += 1
    return bull_cow


def bullgame():
    separator = "=" * 55
    separator_1 = "-" * 55
    separator_2 = "*" * 3

    print(separator_1, "Hi there", separator_1, sep="\n")
    print(f"I've generated a random 4 digit number for you.", separator,
          sep="\n")
    print(f"LET'S PLAY A BULLS AND COWS GAME."
          .center(len(separator)), separator, sep="\n")

    game_num = num_generator()
    score_counter = 0

    while score_counter >= 0:
        print(separator_1)
        guess = input("Enter your guess: ")

        score_counter += 1

        if not guess.isdigit():
            print("The input you entered is not a number! Try again.")
            continue
        elif not no_duplicates(int(guess)):
            print("Number should not have repeated digits! Try again.")
            continue
        elif len(guess) != 4:
            print("Enter 4 digits only! Try again.")
            continue
        elif str(guess).startswith("0"):
            print("The input cannot begin with '0'! Try again.")
            continue

        bull_cow = num_bull_cows(game_num, guess)

        points_bull = "BULL" if bull_cow[0] == 1 else "BULLS"
        points_cow = "COW" if bull_cow[1] == 1 else "COWS"

        print(f"{separator_2} {bull_cow[0]} {points_bull} "
              f" {bull_cow[1]} {points_cow} {separator_2}")

        if bull_cow[0] == 4:
            print(separator, "YOU WON!".center(len(separator)),
                  separator, sep="\n")
            print(f"Correct, you've guessed the right number in"
                  f" {score_counter} guesses!", separator, sep="\n")
            break

    # mins, secs = game.get_time()
    # print(f"Total time spent: {mins} min & {secs} sec")

bullgame()






