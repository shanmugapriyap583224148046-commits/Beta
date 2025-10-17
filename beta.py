import math

def exponential(x):
    return math.exp(x)

x_value = float(input("Enter a value for x: "))
result = exponential(x_value)
print(f"e^{x_value} = {result}")