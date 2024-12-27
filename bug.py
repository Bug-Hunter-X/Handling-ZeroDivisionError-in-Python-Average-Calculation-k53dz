def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 0

my_numbers = [1, 2, 3, 4, 5]
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 3.0

my_numbers = [1, 2, 3, 4, 5, 0]
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 2.5