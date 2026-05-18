products = [
    {"name": "Laptop", "available": True},
    {"name": "Mouse", "available": False},
    {"name": "Keyboard", "available": True},
]


def get_available_products(products):
    available_prodcuts = []

    for product in products:
        if product["available"]:
            available_prodcuts.append(product['name'])
    return available_prodcuts


print(get_available_products(products))  # [Laptop, Keyboard]
print(get_available_products([]))        # []
