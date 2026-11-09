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
print("\n--- Exercise 4 ---")

for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

# Without .items(), the loop only gives the keys.
# With .items(), the loop gives both the keys and values.