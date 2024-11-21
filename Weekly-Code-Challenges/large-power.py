def large_power(base, exponent):
    result = base ** exponent  # Calculate base raised to the power of exponent
    if result > 5000:  # Check if the result is greater than 5000
        return True
    else:
        return False

# Accept user input for base and exponent
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Call the function and print the result
print(large_power(base, exponent))  # Prints True or False based on the result
