
"""
    PYTHON > DECORATOR: @STATICMETHOD

    The @staticmethod transforms a method into one that belongs to a class but does not receive any implicit first argument (like self for instances or cls for the class itself)

    >> WHAT IT DOES:
        - Prevent the method to access its class 'self.';
        - - The method cannot use its class attributes;
        - - The method cannot use its class other methods;

    >> REASON TO USE IT:
        - Nothing about security, but organization and readability (check example 2)!
"""

# Example 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def is_valid_price(price):
        """A utility function to check if a price is valid."""
        return price is not None and price > 0

# You can call it without creating a Product instance:
if Product.is_valid_price(19.99):
    print("Price is valid!")


# Example 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Without staticmethod - functions scattered everywhere
def calculate_tax(price, rate):
    return price * rate

def calculate_shipping(weight, distance):
    return weight * distance * 0.1

# With staticmethod - logically grouped
class OrderCalculator:
    @staticmethod
    def tax(price, rate):
        return price * rate
    
    @staticmethod
    def shipping(weight, distance):
        return weight * distance * 0.1
    
    @staticmethod
    def discount(price, percent):
        return price * (percent / 100)
