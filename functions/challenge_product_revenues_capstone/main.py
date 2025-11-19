# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices,quantities_sold):
    revenue = []
    for i in range(len(prices)):
        R = prices[i]*quantities_sold[i]
        revenue.append(R)
    return revenue
revenue = calculate_revenue(prices,quantities_sold)
revenue_per_product = list(zip(products,revenue))
def formatted_output(revenues):
    new_list = sorted(revenues)
    for j in range(len(new_list)):
        item = new_list[j][0]
        Revenue = new_list[j][1]
        print(f"{item} has total revenue of ${Revenue}")

formatted_output(revenue_per_product)  
 