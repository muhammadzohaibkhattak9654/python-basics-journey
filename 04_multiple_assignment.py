"""
Topic: Multiple Assignment
Python lets you assign several variables at once in two main ways:
1. Different values to different variables in one line.
2. The same value to several variables in one line.
"""

# Different values, different variables
o, c, b = "orange", "cherry", "banana"
print(o, c, b)

# Same value, multiple variables
o = c = b = "orange"
print(o, c, b)
