#PRIME OR NOT#

n = int(input("Enter a number: "))
if (n<=1):
    print("Not a prime number.")
else:
    for i in range(2,n):
        if(n%i==0):
            print("Not a prime number.")
            break
    else:
        print("Yes, it is a prime number.")


#OUTPUT
#Enter a number: 7
#Yes, it is a prime number.
#Enter a number: 8
#Not a prime number.