# program to calculate factorial using a function

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
