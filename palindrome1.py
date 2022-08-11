n = int(input("enter number : "))
temp = n
sum = 0
while (n > 0):
    reminder = n % 10
    sum = sum * 10 + reminder
    n = n // 10
if(temp == sum):
    print("palimdrome")
else:
     print("not palidrome")