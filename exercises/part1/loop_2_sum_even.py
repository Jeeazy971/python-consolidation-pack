numbers = [4, 7, 10, 3, 8, 11, 20]


def sum_even_numbers(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total


print(sum_even_numbers(numbers))    # 42
print(sum_even_numbers([]))         # 0
print(sum_even_numbers([1, 3, 5]))  # 0
