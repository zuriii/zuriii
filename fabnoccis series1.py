def fabnocciseries(n):
   if n <= 1:
       return n
   else:
       return(fabnocciseries(n-1) + fabnocciseries(n-2))

num = 8

if num <= 0:
   print("enter a positive number")
else:
   print("Fibonacci series:")
   for i in range(num):
       print(fabnocciseries(i))
