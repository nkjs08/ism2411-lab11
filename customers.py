#ex1

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}


print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

#ex2


customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


#ex3
email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError caught: email is no longer in the dictionary")

#ex4


for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

# Without .items(), the loop only gives the keys.
# With .items(), the loop gives both the keys and values.

#ex5

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

price = 200
final_price = price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final Price: ${final_price:.2f}")

#ex6

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{person['name']} | Tier: {tier} | Discount: ${discount_amount:.2f}")

#ex7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left")

#ex8

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

region_totals = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    region_totals[region] = region_totals.get(region, 0) + amount

for region in sorted(region_totals):
    print(f"{region}: ${region_totals[region]}")

