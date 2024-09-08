def find_max_min(numbers):
    return max(numbers), min(numbers)


numbers = [10,20,8,5,3]
max_value,min_value = find_max_min(numbers)

print(f"Max: {max_value},Min: {min_value}")
