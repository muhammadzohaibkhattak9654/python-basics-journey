"""
Topic: Type Conversion
You can convert a value from one type to another using str(), int(), and float().
This is useful when, for example, you read a number as text and need to do math on it.
"""

x = str(3)      # converts integer 3 to the string "3"
y = int(45)     # creates an integer 45
z = float(9)    # creates a float 9.0

print(x, y, z)
print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'float'>
