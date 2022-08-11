def sum(n,temp):
    if(n==0):
        return temp
    temp = (temp * 10) + (n % 10)

    return sum(n//10, temp)

n = 12121
temp = sum(n,0)
if(temp==n):
    print("palidrome")
else:
    print("not palindrome")