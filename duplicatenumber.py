list1 = [2, 3, 7, 3, 6, 2, 8, 8]

index = 1
while index < len(list1):
    if list1[index] in list1[: index]:
        list1.pop(index)
    else:
        index += 1

print(list1)