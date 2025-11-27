"""
This example shows pipe operator usage in python
This pipe operator is implemented in langchain modules


The __or__ method in Python is a magic method (also called a dunder method) that allows you to define custom behavior for the bitwise OR operator (|) when used with instances of your class. This is particularly useful when you want to make your objects behave in a specific way during operations involving |.

Here’s a breakdown of how it works:

Key Points
Definition: The __or__ method is called when the | operator is used between two objects.
Fallback: If __or__ is not implemented, Python will attempt to call the __ror__ method on the right-hand operand.
Purpose: It’s commonly used for custom objects to define logical or bitwise operations.
"""

class Pipe:
    def __init__(self, func):
        self.func = func
    
    def __or__(self, other):
        return Pipe(lambda x: other.func(self.func(x)))
    
    def __ror__(self, other):
        return self.func(other)
    
    def __call__(self, x):
        return self.func(x)

@Pipe
def double(x):
    return 2*x
@Pipe
def square(x):
    return x ** 2


x = 10 | double | square # equivalent to square(double(10))

print(x)