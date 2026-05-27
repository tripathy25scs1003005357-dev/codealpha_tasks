# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 170
}

portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", ", ".join(stock_prices.keys()))

# Number of stocks user wants to enter
n = int(input("How many different stocks do you own? "))

for i in range(n):
    stock = input(f"\nEnter stock {i+1} symbol: ").upper()

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    else:
        print("Stock not available in price list!")

# Calculate total investment
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(
        f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}"
    )

print("\nTotal Investment Value = $", total_investment)

# Save result to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(
            f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}\n"
        )

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio summary saved to 'portfolio_summary.txt'")