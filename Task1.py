
num = int(input("Enter an integer: "))

def factorial(n):

    if n<2:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial of " + str(num) + " is " + str(factorial(num)))