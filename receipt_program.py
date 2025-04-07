# Getting prices from user
def input_prices():
    prices = []
    print("Type 'stop' to finish")
    while True:
        x = input("Enter cost: ")
        if x == "stop":
            break
        elif float(x) < 0:
            raise ValueError("Can't have a negative price!")
        else:
            prices.append(float(x))
    return prices

# Totaling up all the prices
def get_total(prices):
    total = 0
    for price in prices:
        total += price
    return round(total, 2)

# Apply tax
def apply_tax(total, tax_rate):
    new_total = total * (1 + tax_rate/100)
    return round(new_total, 2)

# Apply tip
def apply_tip(total, tip_rate):
    new_total = total * (1 + tip_rate/100)
    return round(new_total, 2)

def input_tip_percentage():
    tip = input("What percent would you like to tip? ")
    return float(tip)

prices = input_prices()
total = get_total(prices)
print("Your subtotal is: " + str(total))

tax_total = apply_tax(total, 10.25)
print("Your total after taxes is: " + str(tax_total))

tip_percent = input_tip_percentage()
final_total = apply_tip(tax_total, tip_percent)
print("Your grand total after tip and tax is: " + str(final_total))