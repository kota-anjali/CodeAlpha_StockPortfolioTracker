stock_prices={
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350
}
total_value = 0
num_stocks = int(input("How many stocks do you want to enter? "))
for i in range(num_stocks):
    print(f"\nStock {i+1}")
    stock_name = input("Enter stock name (AAPL/TSLA/GOOGL/MSFT): ").upper()
    quality = int(input("Enter quality: "))
    if stock_name in stock_prices:
        stock_value = stock_prices[stock_name]*quality 
        total_value+=stock_value
        print("Stock Value =", stock_value)
    else:
        print("Stock not found!")
print("\nTotal Portfolio Value =", total_value)