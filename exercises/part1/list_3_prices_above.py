prices = [12.5, 99.9, 45.0, 150.0, 8.99]


def get_prices_above(prices, threshold):
    filtered_prices = []
    
    for price in prices:
        if price >= threshold:
            filtered_prices.append(price)
    return filtered_prices

print(get_prices_above(prices, 50))    # [99.9, 150.0]
print(get_prices_above(prices, 1000))  # []
print(get_prices_above([], 50))        # []
