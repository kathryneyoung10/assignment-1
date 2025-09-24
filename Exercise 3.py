# Exercise 3: Customer Greeting Formatter

def format_greeting(name: str, title: str = "Customer") -> str:
    cleaned = name.strip()
    if cleaned == "":
        return "Hello, Valued Customer!"
    titled = cleaned.title()
    parts = titled.split()
    first = parts[0] if parts else ""
    return f"Hello, {first} ({title})!"

# Main
full_name = input("What's your full name? ")
greeting = format_greeting(full_name)
print(greeting)