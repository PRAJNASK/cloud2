# Function to find the maximum and minimum values in a list
def find_max_min(numbers):
    max_val = max(numbers)
    min_val = min(numbers)
    return max_val, min_val

# User input
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [float(num) for num in numbers]  # Convert input strings to float

# Finding max and min values
max_value, min_value = find_max_min(numbers)

# Output
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
