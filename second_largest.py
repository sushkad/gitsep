def second_largest(numbers):
    if len(numbers) < 2:
        return "List should contain at least two elements"

    largest = second_largest = float('-inf')  # Initialize with negative infinity

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "There is no second largest element in the list"
    else:
        return second_largest


# Test the function
numbers = [0, 1, 2, 7, 15]
print("Second largest number:", second_largest(numbers))
