# Exercise 4: Tax Bracket Determiner

def get_tax_bracket(income: float) -> str:
    if income < 0:
        return "Invalid income."
    if income < 50_000:
        bracket = "Low (10%)"
    elif income < 100_000:
        bracket = "Medium (20%)"
    else:
        bracket = "High (30%)"
    eligible = " (Deduction Eligible)" if int(income) % 2 == 0 else ""
    return bracket + eligible

def rate_for_bracket(bracket: str) -> float:
    if "10%" in bracket:
        return 0.10
    if "20%" in bracket:
        return 0.20
    if "30%" in bracket:
        return 0.30
    return 0.0

income_str = input("What's your annual income? ").strip()
income = float(income_str)

bracket = get_tax_bracket(income)
if bracket == "Invalid income.":
    print(bracket)
else:
    rate = rate_for_bracket(bracket)
    est_tax = income * rate
    print(f"Your bracket: {bracket}. Estimated tax: {est_tax}")