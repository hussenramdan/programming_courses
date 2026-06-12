numbers = []
no_dublicate = []
sum = 0
count = 0

num = int(input("Enter A Number"))
while(num >= 0):
    numbers.append(num)
    sum += num
    count += 1

    if num not in no_dublicate:
        no_dublicate.append(num)
    num = int(input("Enter A Numbers"))

    avg = sum / count
    print(f"Age {avg}")
    print(f"list{numbers}")
    print(f"unique{no_dublicate}")










numbers = []
no_dublicate = []
sum = 0
count = 0

num = int (input("Enter a Number"))

while(num >= 0):

    numbers.append(num)
    sum += num
    count = 1

    if num not in no_dublicate:
        no_dublicate.append(num)
    num = int (input ("Enter a Number"))

    avg = sum / count

    print(f"Avg{avg}")
    print(f"list{numbers}")
    print(f"unique{no_dublicate}")










numbers = []
no_dublicate = []

sum = 0
count = 0

num = int (input ("Enter a Numbers"))

while(num >= 0):
    numbers.append(num)
    sum += num
    count += 1

    if num not in no_dublicate:
        no_dublicate.append(num)
    num = int (input ("Enter a Enter"))

    avg = sum / count

    print(f"avg{avg}")
    print(f"list{numbers}")
    print(f"unqiue{no_dublicate}")