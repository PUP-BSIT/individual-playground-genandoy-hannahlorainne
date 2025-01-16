import asciibars

def generate_binary_heatmap(data):
    for label, binary_rep in data:
        heatmap_row = ""
        for digit in binary_rep:
            heatmap_row += "[■]" if digit == '1' else "[ ]"
        print(f"{label}: {heatmap_row}") 

def display_converted_binaries(data):
    print("\n-- CONVERTED BINARY NUMBERS --\n")
    for label, binary_rep in data:
        print(f"{label}: {binary_rep}")


def decimal_to_binary_bar(num):
    return bin(num)[2:] 

def main():
    data = [] 
    print("\n--- Labels and Decimal counts to visualize in Binary ---")
    print("Type 'done' or 'DONE' to finish")

    while True:
        label = input("Enter label: ")  
        if label.lower() == 'done':  
            break

        try:
            count = int(input(f"Enter decimal count for '{label}': "))  
            binary_rep = decimal_to_binary_bar(count)  
            data.append((label, binary_rep))  
        except ValueError: 
            print("Invalid input. Please enter a valid number.")

    if data:
        display_converted_binaries(data)
        print("\n-- BINARY HEATMAP --\n")
        generate_binary_heatmap(data)
    else:
        print("No data entered. Exiting program.") 


if __name__ == "__main__":
    main()
