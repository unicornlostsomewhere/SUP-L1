'''
С клавиатуры вводится текст, определить, сколько в нём гласных,
a сколько согласных. В случае равенства вывести на экран все гласные
буквы. Посчитать количество слов в тексте.
'''

text = input("Введите текст: ")
vowels_count = 0
consonants_count = 0
vowels = []
vowels_list = ['a', 'e', 'i', 'o', 'u', 'у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']

text_lower = text.lower()

for char in text_lower:
    if char.isalpha():
        if char in vowels_list:
            vowels_count += 1
            vowels.append(char)
        else:
            consonants_count += 1

print("Гласных букв: ", vowels_count)
print("Согласных букв: ", consonants_count)

if vowels_count == consonants_count:
    print("Гласные буквы в тексте:")
    for vowel in vowels:
        print(vowel)

words = text.split()
words_count = len(words)
print("Количество слов: ", words_count)



