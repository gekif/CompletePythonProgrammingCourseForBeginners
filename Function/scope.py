# def greet():


# Global variable
message = "a"


def greet(name):

    # Local variable inherit from global variable
    global message

    message = "b"


# def sendEmail(name):
#     message = "b"

# print(message)

# print(name)

greet("Mosh")

print(message)