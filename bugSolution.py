def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") #This will return 0 as expected

my_list = [10,20,30,40,50]
average = calculate_average(my_list)
print(f"The average is: {average}") #This will return 30 as expected

my_list = [10,20,30,40,50, "a"]
average = calculate_average(my_list)
print(f"The average is: {average}") #This will return 30 as expected because it ignores the non-numeric element