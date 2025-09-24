# Exercise 1: Profit Margin Calculator

# Prompt the user for revenue and cost (floats)
revenue_input = input("What's the revenue? ").strip()
cost_input = input("What's the cost? ").strip()

# Convert to float
revenue = float(revenue_input)
cost = float(cost_input)

# Compute profit
profit = revenue - cost

# Guard against invalid revenue
if revenue <= 0:
    print("Invalid revenue.")
else:
    margin = (profit / revenue) * 100
    # Nicely formatted output with 2 decimals and commas
    print(f"Profit: ${profit:,.2f} | Margin: {margin:.2f}%")