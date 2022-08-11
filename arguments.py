x = (1, 2, 3, 4, 5)


def argumentFunction(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


argumentFunction(*x)


# local-functions
# nested functions

def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()


if __name__ == '__main__':
    outerFunction('hello')

# closure


def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction


if __name__ == '__main__':
    myFunction = outerFunction('hello1')
    print(myFunction)
    myFunction()


#decorator

def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")
        returned_value = func(*args, **kwargs)
        print("after Execution")

        return returned_value

    return inner1


@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2
print("Sum =", sum_two_numbers(a, b))
