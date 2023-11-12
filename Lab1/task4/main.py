from heapq import nsmallest
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
small = nsmallest(3, my_dict, key=my_dict.get)
print(my_dict.)
print(small)
