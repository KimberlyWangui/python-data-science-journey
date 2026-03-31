from currency_converter import convert_currency, get_exchange_rate, exchange_rates

amount = 100
from_currency = 'USD'
to_currency = 'EUR'

converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
exchange_rate = get_exchange_rate(from_currency, to_currency, exchange_rates)

print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
print(f"The exchange rate from {from_currency} to {to_currency} is {exchange_rate}")


from mathtools import add, subtract, multiply, divide, power, modulus, area_of_rectangle, area_of_circle, area_of_triangle, perimeter_of_rectangle, circumference_of_circle, perimeter_of_triangle, is_prime, fibonacci

# Example usage of arithmetic functions
a = 10
b = 5
print(f"Addition: {a} + {b} = {add(a, b)}")
print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
print(f"Division: {a} / {b} = {divide(a, b)}")
print(f"Power: {a} ** {b} = {power(a, b)}")
print(f"Modulus: {a} % {b} = {modulus(a, b)}")

# Example usage of geometry functions
base = 5
height = 10
print(f"Area of triangle: {area_of_triangle(base, height)}")

length = 4
width = 6
print(f"Area of rectangle: {area_of_rectangle(length, width)}")

radius = 3
print(f"Area of circle: {area_of_circle(radius)}")
print(f"Perimeter of rectangle: {perimeter_of_rectangle(length, width)}")
print(f"Circumference of circle: {circumference_of_circle(radius)}")

side1 = 3
side2 = 4
side3 = 5
print(f"Perimeter of triangle: {perimeter_of_triangle(side1, side2, side3)}")

# Example usage of utility functions
number = 29
print(f"Is {number} a prime number? {is_prime(number)}")
n = 20
print(f"Fibonacci sequence up to {n}: {fibonacci(n)}")
