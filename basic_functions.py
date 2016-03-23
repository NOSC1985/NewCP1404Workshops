



"""
CP1404 Workshop 04
Basic functions
demonstrating various parameters, returns and the use of a main function
"""
__author__ = 'Nicholas Stanton-Cook'


def main():
    lowest, highest = get_limits()
    print("lowest =", lowest, "highest =", highest)
    print_between(lowest, highest)


def get_limits():
    minimum = int(input("Enter the minimum: "))
    maximum = int(input("Enter the maximum: "))

    while maximum < minimum:
        print("maximum must be higher than or equal to minimum")
        minimum = int(input("Enter the new minimum: "))
        maximum = int(input("Enter the new maximum: "))
    return minimum, maximum


def print_between(start, end):
    for i in range(start, end+1):
        print(i, end=' ')

main()
