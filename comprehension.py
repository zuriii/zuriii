# nested for loop

matrix = []

for i in range(5):
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)

print(matrix, end=" ")

# nested list comprehension


matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

# set comprehensions

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newSet = {element * 3 for element in myList if element % 2 == 0}
print("The existing list is:")
print(myList)
print("The Newly Created set is:")
print(newSet)

# dictionary
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num * num
print(square_dict)

# dictionary comprehension
# dictionary = {key: value for vars in iterable}
square_dict = {num: num * num for num in range(1, 11)}
print(square_dict)

# Comprehension with If-clause:
# [ expr(item) for item in iterable if predicate(item) ]
num = [i for i in range(30) if i >= 2 if i <= 25 if i % 4 == 0 if i % 8 == 0]
print(num)

# multiple comprehension
values = [(x, y) for x in range(5) for y in range(3)]

values = []
for x in range(5):
    for y in range(3):
        values.append((x, y))


# *args and **kwargs in Python
def myfun(*argv):
    for arg in argv:
        print(arg)


myfun('hello', 'I', 'am', 'here')


def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myfun('hello', 'I', 'am', 'here')


def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='I', mid='am', last='here')


def function_name(a, b, c, d):
    print(a, b, c, d)


function_name("a", "b", "c", "d")


def hyperVolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v += length
    return v


print(hyperVolume(1, 2, 3, 4, 5))

# iterative and next

vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)  # return as an iterator object
print(next(vowels_iter))


