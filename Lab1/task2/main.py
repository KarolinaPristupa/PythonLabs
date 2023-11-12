string = str(input("Enter string: "))
string_list = string.split()
s='qwert'


amount = 0
for i in string_list:
    if len(i) % 2 == 0:
        amount = amount + 1
print(amount)

print(max(string_list, key=len))


