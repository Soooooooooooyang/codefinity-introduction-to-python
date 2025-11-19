def apply_discount(price,discount=0.05):
    t_discount = price*(1-discount)
    return t_discount

def apply_tax(price,tax = 0.07):
    t_tax = price*(1+tax)
    return t_tax

def calculate_total(price,discount=0.05,tax=0.07):
    t_discount = apply_discount(price,discount)
    total = apply_tax(t_discount,tax)
    return total

total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")
total_price_custom = calculate_total(100,discount=0.1,tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")

