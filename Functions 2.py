# function = A block of reusable code
#           place () after the function name to invoke it

def happy_birthday(name, age, last_name):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} old!")
    print(f"Happy birthday to {name} {last_name}!")
    print()

happy_birthday("Emmanuel", 29, "Okoh")

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your invoice is ${amount:.2f}")
    print(f"It will be due on {due_date}")

display_invoice("Emmanuel", 29.50, "11/02/1996")