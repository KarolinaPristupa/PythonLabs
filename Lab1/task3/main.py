string = input("Enter List: ")
workString = string.split()
numbers = []
for item in workString:
    try:
        numbers.append(int(item))
    except ValueError:
        print("Error!")
        break

sorted_numbers = sorted(numbers)
sorted_numbers.reverse()
for num in sorted_numbers:
    if num % 2 == 0:
        print(num)
        break

pos = [num for num in numbers if num > 0]
neg = [num for num in numbers if num <= 0]
res = pos + neg
print(res)