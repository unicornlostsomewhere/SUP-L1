'''
Реализуйте программу «Магазин игрушек», которая будет включать в
себя шесть пунктов меню.  У вас есть словарь, где ключ – название игрушки.
Значение – список, который содержит состав игрушки, цену и кол-во (шт),которое есть в магазине.
1. Просмотр описания: название – описание
2. Просмотр цены: название – цена.
3. Просмотр количества: название – количество.
4. Всю информацию.
5. Покупка
В пункте «Покупка» необходимо совершить покупку,
с клавиатуры вводите название игрушки и его кол-во,
n – выход из программы. Посчитать цену выбранных товаров и
сколько товаров осталось в изначальном списке.
6. До свидания
'''



toys = {
    'Мяч': ['мяч', 100, 5],
    'Кукла': ['пластмасса', 200, 3],
    'Машинка': ['металл', 150, 4],
    'Пазл': ['картон', 300, 2],
    'Конструктор': ['пластик', 250, 6],
    'Кубики': ['дерево', 120, 7]
}

while True:
    print("Меню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        print("Описание игрушки:")
        toy_name = input("Введите название игрушки: ")
        if toy_name in toys:
            print(toy_name + " - " + toys[toy_name][0])
        else:
            print("Игрушка не найдена")

    elif choice == '2':
        print("Цена игрушки:")
        toy_name = input("Введите название игрушки: ")
        if toy_name in toys:
            print(toy_name + " - " + str(toys[toy_name][1]))
        else:
            print("Игрушка не найдена")

    elif choice == '3':
        print("Количество игрушки:")
        toy_name = input("Введите название игрушки: ")
        if toy_name in toys:
            print(toy_name + " - " + str(toys[toy_name][2]) + " шт")
        else:
            print("Игрушка не найдена")

    elif choice == '4':
        print("Вся информация о игрушках:")
        for toy, info in toys.items():
            print(toy + ": " + info[0] + ", Цена: " + str(info[1]) + ", Количество: " + str(info[2]) + " шт")

    elif choice == '5':
        total_price = 0
        print("Покупка игрушек:")
        while True:
            toy_name = input("Введите название игрушки (n для выхода): ")
            if toy_name == "n":
                break
            if toy_name not in toys:
                print("Игрушка не найдена")
                continue
            quantity = int(input("Введите количество: "))
            if quantity > toys[toy_name][2]:
                print("Не хватает товаров на складе")
                continue
            price = toys[toy_name][1] * quantity
            total_price += price
            toys[toy_name][2] -= quantity
            print("Вы приобрели " + toy_name + " в количестве " + str(quantity) + " шт по цене " + str(price))
        print("Сумма покупки: " + str(total_price))
        print("Остаток товаров:")
        for toy, info in toys.items():
            print(toy + ": " + info[0] + ", Количество: " + str(info[2]) + " шт")

    elif choice == '6':
        print("До свидания!")
        break

    else:
        print("Некорректный выбор, попробуйте снова.")
