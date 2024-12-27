def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 0

my_numbers = [1, 2, 3, 4, 5]
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 3.0

my_numbers = [1, 2, 3, 4, 5, 0]
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will print 2.5