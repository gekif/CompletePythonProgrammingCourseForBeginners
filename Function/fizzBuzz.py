def fizzBuzz(input):

    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"

    if input % 3 == 0:
        return "Fizz"

    if input % 5 == 0:
        return "Buzz"

    return input

# Return Fizz
print(fizzBuzz(3))

# Return Buzz
print(fizzBuzz(5))

# Return FizzBuzz
print(fizzBuzz(15))

# Return None
print(fizzBuzz(7))