store_a = ["apple", "banana", "rice", "milk"]
store_b = ["bread", "banana", "milk", "pasta"]


def get_common_products(store_a, store_b):
    return sorted(set(store_a) & set(store_b))


print(get_common_products(store_a, store_b))  # ["banana", "milk"]
print(get_common_products([], store_b))       # []
