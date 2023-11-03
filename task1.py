
"""
На обработку поступает натуральное число. Нужно написать
программу, которая выводит на экран сумму чётных цифр этого числа
или 0, если чётных цифр в записи нет.
"""

number = int(input("Введите натуральное число: "))
if number < 0:
    print("Вы ввели не натуральное число")
else:
    number_str = str(number)
    sum_even_digits = 0

    for i in number_str:
        if int(i) % 2 == 0:
            sum_even_digits += int(i)
            if sum_even_digits == 0:
                print(0)
    else:
        print("Сумма четных цифр : ", sum_even_digits)



