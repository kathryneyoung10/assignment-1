# Bonus Challenge: Integrated Decision Tool (if/elif version)

def is_profitable(revenue: float, cost: float) -> bool:
    return revenue > cost

def categorize(product: str) -> str:
    p = product.strip().lower()
    if p in ["electronics", "gadget"] or p.startswith("tech"):
        return "High Margin"
    elif p in ["clothing", "apparel"]:
        return "Medium Margin"
    elif p in ["food", "grocery"]:
        return "Low Margin"
    else:
        return "Uncategorized - Review Needed"

def suggestion(category: str) -> str:
    if category == "High Margin":
        return "Reinvest in marketing and product development."
    elif category == "Medium Margin":
        return "Optimize pricing and watch costs."
    elif category == "Low Margin":
        return "Focus on volume efficiencies or upselling."
    else:
        return "Review category mapping before investing."

# Main
rev = float(input("Business revenue: ").strip())
cost = float(input("Business cost: ").strip())
prod = input("Product category (e.g., electronics, clothing, food, tech ...): ").strip()

profitable = is_profitable(rev, cost)
cat = categorize(prod)

if profitable:
    profit = rev - cost
    print(f"Status: Profitable. Profit = ${profit:,.2f}")
    print(f"Category: {cat}")
    print("Advice:", suggestion(cat))
else:
    print("Status: Not profitable. Review costs, pricing, or demand.")
    print(f"Category: {cat}")