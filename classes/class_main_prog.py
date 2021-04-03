from classes import SpecialOperation

a = 2
b = "5,3"

# Creating object for the class SpecialOperation with 2 parameters
spl_opr = SpecialOperation(a, b)

# Calling method inside SpecialOperation
print(spl_opr.concatnumber())

print(spl_opr.split("5,"))