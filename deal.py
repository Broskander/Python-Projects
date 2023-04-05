import math
import random


def deal_calc(numThrows):
    num = 0
    count = 0

    print("\nPrize".ljust(12), end='')
    print("Guess".ljust(12), end='')
    print("View".ljust(12), end='')
    print("New Guess")

    while (count < numThrows):
        door_list = [1, 2, 3]
        door_to_prize = random.randint(1, 3)
        contestent_guess = random.randint(1, 3)
        temp = 1
        if (temp == door_to_prize) or (temp == contestent_guess):
            temp = 2
            if (temp == door_to_prize) or (temp == contestent_guess):
                temp = 3
        door_list.remove(temp)
        door_list.remove(contestent_guess)
        newGuess = int(door_list[0])

        print(f"{door_to_prize}".ljust(14), end='')
        print(f"{contestent_guess}".ljust(11), end='')
        print(f"{temp}".ljust(15), end='')
        print(f"{newGuess}")

        if (newGuess == door_to_prize):
            num = num + 1
        count = count + 1

    return num


def main():
    numThrows = int(input("Enter number of times you want to play: "))
    num = deal_calc(numThrows)
    win = (float(num) / float(numThrows))
    lose = (1.0 - win)
    print("\nProbability of winning if you switch =", round(win, 3))
    print("Probability of winning if you do not switch =", round(lose, 3))


main()
