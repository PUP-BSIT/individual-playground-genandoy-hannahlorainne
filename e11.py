import roman

try:
    number = int(input("Enter an Arabic number: "))
    if number <= 0:
        print("Roman numerals are not defined for zero or negative numbers.")
    else:
        roman_numeral = roman(number)
        print(f"The Arabic number {number} is equal to {roman_numeral}.")
except ValueError:
    print("Please enter a valid integer.")
