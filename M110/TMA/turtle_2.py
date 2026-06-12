# find_min_temperature

def find_min_temperature(temperature):
    lowest = temperature[0]
    for i in temperature:
        if i < lowest:
            lowest = i
    return lowest

temp_list = []
print("Enter 5 Temperature: ")
for i in range(5):
    temp = eval (input ())
    temp_list.append(temp)
print(f"the lowest temperature is {find_min_temperature(temp_list)}")







# celsius_to_



