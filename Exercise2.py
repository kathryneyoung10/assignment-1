# Exercise 2: Credit Score Evaluator

# Prompt the user
score_str = input("Enter your credit score (300-850): ").strip()

# Convert to int
score = int(score_str)

# Validate and categorize
if score < 300 or score > 850:
    print("Invalid score.")
else:
    if score >= 750:
        msg = "Excellent - Loan Approved"
        approved = True
    elif 700 <= score < 750:
        msg = "Good - Loan Approved with Review"
        approved = True
    elif 600 <= score < 700:
        msg = "Fair - Loan Conditional"
        approved = False
    else:
        msg = "Poor - Loan Denied"
        approved = False

    rate_msg = "Interest rate: Low" if approved else "Seek credit improvement."
    print(f"{msg}. {rate_msg}")
