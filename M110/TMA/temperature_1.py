# Find min Temperture 


# # # def find_min_temperature(temperature):
# # #     lowest = temperature[0]
# # #     for i in temperature:
# # #         if i < lowest:
# # #             lowest = i
# # #     return lowest

# # #     temp_list = []
# # #     print ("Enter a 5 Number")
# # #     for i in range(5):
# # #         temp = eval(input())
# # #         temp_list.append(temp)
# # #         print(f"The Lowest Temperature {find_min_temperature(temp_list)}")



# # def find_min_temperature(temperature):
# #     lowest = temperature[0]
# #     for i in temperature:
# #         if i < lowest:
# #             lowest = i
# #     return lowest


# # temp_list = []
# # print ("Enter 5  Temperature: ")
# # for i in range(5)
# #     temp = eval(input())
# #     temp_list.append(temp)  
# # print(f"The is Temperature {find_min_tempreture(temperature)}")






# def find_min_temperature(temperature):
#     lowest = temperature[0]
#     for i in temperature:
#         if i < lowest:
#             lowest = i
#     return lowest

# temp_list = []
# print("Enter 5 Temperature")
# for i in range(5):
#     temp = eval(input())
#     temp_list.append(temp)
# print (f"The is Temperture{find_min_temperature(temp_list)}")










def find_min_temperature(temperature):
    lowest = temperature[0]
    for i in temperature:
        if i < lowest :
            lowest = i
        return lowest
    
    temp_list = []
    print("Enter a Tempreture: ")
    for i in range(5):
        temp = eval (input ())
        temp_list.append(temp)
    print(f"The temperature" {find_min_temperature(temp_list)})