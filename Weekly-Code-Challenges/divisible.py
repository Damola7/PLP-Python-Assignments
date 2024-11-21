def divisible_by_ten(num):
    if num % 10 == 0:  # Check if the remainder is 0 when divided by 10
        return True
    else:
        return False

# Accept user input for the number
num = int(input("Enter a number: "))

# Call the function and print the result
print(divisible_by_ten(num))  # Prints True or False based on divisibility by 10
