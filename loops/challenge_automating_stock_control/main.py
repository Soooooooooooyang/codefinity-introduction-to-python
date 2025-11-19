# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started")
for item,stock in inventory.items():
    print(f"Processing {item}")
    current_stock = stock[0]
    minimum_stock = stock[1]
    restock = stock[2]
    on_sale = stock[-1]
    while current_stock < minimum_stock:
        current_stock += restock
    stock[0] = current_stock
    if current_stock > discount_threshold and on_sale != True:
        stock[-1] = True
print("Processing completed")