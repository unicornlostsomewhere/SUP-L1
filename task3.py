'''
Дан список list=[12,511,'Python',311,122,'love’].
Все числа этого списка проверить на чётность. Если число чётное,
то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
'''

my_list = [12, 511, 'Python', 311, 122, 'love']
new_list = []

for item in my_list:
    if isinstance(item, int):
        if item % 2 == 0:
            sum_of_digits = sum(int(digit) for digit in str(item))
            new_list.append(sum_of_digits)
        else:
            new_list.append(1)
    else:
        new_list.append(item)

print(new_list)
