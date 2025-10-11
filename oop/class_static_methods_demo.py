class Calculator:
    """A calculator class demonstrating static and class methods."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Prints class attribute and returns the product."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
