# program to calculate square root, log and sine using math module

import math

num = float(input("Enter a number: "))

sq_root = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

print("Square root of", num, "is", sq_root)
print("Natural log of", num, "is", log_val)
print("Sine of", num, "is", sine_val)
