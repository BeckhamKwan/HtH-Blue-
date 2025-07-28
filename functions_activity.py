#F & OP Beckham,Kwan

#STEP I: Menu items
menu = {"Pizza": 2.99, "Burger": 3.99, "Hot dog": 1.99, "Cheese": 0.59, "Ice cream": 1.49, "Churro": 0.79, "Soda": 0.89}

# STEP II: Add prices of two or more items
def total_price(*items):
    total = 0
    missing_items = []
    for item in items:
        if item in menu:
            total += menu[item]
        else:
            missing_items.append(item)
    if missing_items:
        return f"Error: The following items are not on the menu: {', '.join(missing_items)}"
    return f"The total price of {', '.join(items)} is {total:.2f}"

# STEP III: price difference between 2 items
def price_difference(item1, item2):
    if item1 in menu and item2 in menu:
        difference = abs(menu[item1] - menu[item2])
        return f"The difference between {item1} and {item2} is {difference:.2f}"
    else:
        return f"Error: One or both items are not on the menu."

# STEP IV: Multiply one item's price by a multiplier
def inflation(item, multiplier):
    if item in menu:
        menu[item] *= multiplier
        return menu
    else:
        return f"Error: {item} is not in the menu."

# STEP V: Divide one item's price by a divisor
def deflation(item, divisor):
    if item not in menu:
        return f"Error: {item} is not in the menu."
    if divisor == 0:
        return "Error: Cannot divide by zero."
    menu[item] /= divisor
    return menu

# STEP VI: Find items with prices that are divisible by 0.50 using modulus
def half_dollar_items():
    result = [item for item, price in menu.items() if round(price % 0.5, 2) == 0]
    return f"Items with prices divisible by $0.50: {', '.join(result)}"
