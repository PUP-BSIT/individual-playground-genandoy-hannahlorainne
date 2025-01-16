import asciibars

def generate_binary_heatmap(data):
    """
    Creates a heatmap from a list of binary representations.
    Each binary digit is visualized as a filled or empty cell.
    """
    for label, binary_rep in data:
        heatmap_row = ""  # This will hold the row for the heatmap
        for digit in binary_rep:
            # Append a filled or empty block based on the digit (1 or 0)
            heatmap_row += "[■]" if digit == '1' else "[ ]"
        print(f"{label}: {heatmap_row}")  # Print the label and its binary heatmap


def display_converted_binaries(data):
    """
    Separately displays the converted binary numbers for all entries.
    """
    print("\n-- CONVERTED BINARY NUMBERS --\n")
    for label, binary_rep in data:
        print(f"{label}: {binary_rep}")


def decimal_to_binary_bar(num):
    """
    Converts a decimal number into a binary string.
    """
    return bin(num)[2:]  # Convert to binary and remove the '0b' prefix


def main():
    data = []  # List to store the label and binary representation pairs
    print("\n--- Labels and Decimal counts to visualize in Binary ---")
    print("Type 'done' or 'DONE' to finish")

    while True:
        label = input("Enter label: ")  # Get a label from the user
        if label.lower() == 'done':  # Stop the loop if the user types 'done'
            break

        try:
            count = int(input(f"Enter decimal count for '{label}': "))  # Get a decimal number
            binary_rep = decimal_to_binary_bar(count)  # Convert to binary
            data.append((label, binary_rep))  # Add the label and binary to the list
        except ValueError:  # Handle invalid number inputs
            print("Invalid input. Please enter a valid number.")

    # Separate display for converted binary numbers
    if data:
        display_converted_binaries(data)
        print("\n-- BINARY HEATMAP --\n")
        generate_binary_heatmap(data)
    else:
        print("No data entered. Exiting program.")  # Exit message if no data was entered


if __name__ == "__main__":
    main()
