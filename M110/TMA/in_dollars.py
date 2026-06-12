meal = []
price = []
less_than20 = []
merged = []
total = 0

for i in range(1,7):
    m = input(f"Enter The name meal {i}: ")
    meal.append(m)

    p = eval (input (f"Enter its Price ( $ ): "))
    price.append(p)

for i in range(6):

    total += i
print(f"The Total Cost Of all meals is {total}")

for i in range(6):
    if price[i] < 20:
        less_than20.append(meal[i])


print("meals less than 20$ ", less_than20)

for i in range(6):
    merged.append((meal[i], price[i]))

print("merged list: "merged)