# Exercise 5: Product Category Matcher (if/elif version)

name = input("What's the product name? ").strip().lower()

if name in ["electronics", "gadget"] or name.startswith("tech"):
    category = "High Margin"
elif name in ["clothing", "apparel"]:
    category = "Medium Margin"
elif name in ["food", "grocery"]:
    category = "Low Margin"
else:
    category = "Uncategorized - Review Needed"

print(f"Product: {name} | Category: {category}")