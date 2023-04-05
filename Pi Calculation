import math
import random

def calculate_pi(num):

    def pos():
        xPos = random.uniform(-1.0, 1.0)
        yPos = random.uniform(-1.0, 1.0)
        return xPos, yPos

    def outer(x, y):
        return ((x ** 2) + (y ** 2) == 1)

    def inner(x, y):
        return (math.sqrt((x ** 2) + (y ** 2)) < 1)

    def div(num1, num2):
        return (num2 / num1) * 4

    def difference(pi):
        difference = pi - math.pi

        if (difference > 0):
            return ('+', difference)

        else:
            return (' ', difference)

    def calculate(t):
        dart = 0
        innerCircle = 0

        for i in range(t):
            x, y = pos()

            if outer(x, y) or inner(x, y):
                innerCircle += 1
                dart += 1

            else:
                dart += 1

        return (dart, innerCircle)

    (total, inside) = calculate(num)
    pi = div(total, inside)
    variance = difference(pi)

    return (pi, variance)


def main():
    print('Computation of PI using Random Numbers\n')
    list = [100, 1000, 10000, 100000, 1000000, 10000000]

    for darts in (list):
        pi, variance = calculate_pi(darts)
        finish = pi
        diff = ''.join( [str(i) for i in variance] )

        print('{:<10} {:<10} {:<10} {:<10} {:<10} {:<7}'.format('Num = ', darts, 'Calculated PI = ', f'{finish:.6f}', 'Difference = ', diff[:9], ))

    print("\nDifference = Calculated PI - math.pi")


main()
