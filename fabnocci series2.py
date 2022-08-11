
num = int(input("enter number:"))
n1 = 0
n2 = 1
count = 0

if num <= 0:
   print("Please enter a positive integer")

elif num == 1:
   print("Fibonacci sequence ",num,"", end=" ")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < num:
       print(n1 , end=" ")
       nextterm = n1 + n2
       n1 = n2
       n2 = nextterm
       count += 1