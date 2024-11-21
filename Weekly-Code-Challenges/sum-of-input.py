# Accepting user input to create a list of integers
user_input = input("Enter integers separated by spaces: ")
my_list = list(map(int, user_input.split()))

# Computing the sum of all integers in the list
total_sum = sum(my_list)

print("The sum of all the integers in the list is:", total_sum)
 