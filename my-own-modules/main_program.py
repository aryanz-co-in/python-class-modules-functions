# Importing custom module to perform math operations.

# Importing all the methods inside the module.
# Using this method we need to use the module name as reference to call every methods inside.
import math_operations

# Importing only the method inside module. Using this approach we can directly call the method.
from number_concat import concat_int


x = 100
y = 2

print(f"Addition using own module: {math_operations.add(x, y)}")

print(f"Subtraction using own module: {math_operations.sub(x, y)}")

print(f"Multiplication using own module: {math_operations.mul(x, y)}")

print(f"Division using own module: {math_operations.div(x, y)} ")


print(f"Concat {concat_int(x, y)}")
