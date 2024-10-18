from decimal import Decimal
from typing import Callable
# Import arithmetic operations from a module named calculator.operations
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    # Constructor method with type hints for parameters and the return type
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        # Store the operation as a callable that takes two Decimals and returns a Decimal
      
        self.operation = operation
    
    # Static method to create a new instance of Calculation
    @staticmethod    
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        # Return a new Calculation object initialized with the provided arguments
        return Calculation(a, b, operation)

    # Method to perform the calculation stored in this object
    def perform(self) -> Decimal:
        "Perform the stored calculation and return the result."
        # Returns result of a and b
        return self.operation(self.a, self.b)

    # Special method to provide a string representation of the Calculation instance
    def __repr__(self):
        "Return a simplified string representation of the calculation."
        # This method makes it easier to understand what the Calculation object represents when printed or logged
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"