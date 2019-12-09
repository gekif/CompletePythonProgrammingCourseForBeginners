# [2, 3, 4, 5]

# [] -> List: can add collection, mutable

# () -> Tuples: cannot modified collection, immutable


def multiply(*numbers):

    total = 1

    for number in numbers:

        # Using augmented assignment
        total *= number

    return total


print(multiply(2, 3, 4, 5))