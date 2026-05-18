numbers = [-5, 3, 0, 12, -2, 8, 1]


def count_positive_numbers(numbers):
    count = 0
    if len(numbers) == 0:
        return 0
    
    if numbers is None:
        return None
    
    for number in numbers:
        if number > 0:
            count += 1
        
    return count

print(count_positive_numbers(numbers))   # 4
print(count_positive_numbers([]))        # 0
print(count_positive_numbers([-1, -2]))  # 0
