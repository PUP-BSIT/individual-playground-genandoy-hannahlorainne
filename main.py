import math

# Print Hello World
print("Hello World!")

# Get user input
number = float(input("Enter a number: "))

# Function to calculate the area of a circle using the number as the radius
def calculate_area(radius):
    return math.pi * radius ** 2

# Calculate the area
area = calculate_area(number)

# Display the result
print(f"The area of the circle with radius {number} is {area:.2f}")
