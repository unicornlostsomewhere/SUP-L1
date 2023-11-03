'''
Найдите три ключа с самыми маленькими значениями в словаре
my_dict = {'a':12, 'b':13, 'c': 56,'d':400, 'e':58, 'f': 20}
'''

my_dict = {'a': 12, 'b': 13, 'c': 56, 'd': 400, 'e': 58, 'f': 20}

values = list(my_dict.values())

sorted_values = sorted(values)

smallest_keys = []
for key, value in my_dict.items():
    if value in sorted_values[:3]:
        smallest_keys.append(key)

print(smallest_keys)
