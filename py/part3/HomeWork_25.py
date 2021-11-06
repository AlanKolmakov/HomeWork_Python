# Посчитайте гласные буквы в строке

user_str = input("Введите строку: ")
vowels_ru = set("ауоыэяюёие")
vowels_en = set("aeiouy")
lower_set = user_str.lower()
vowels_count_ru = sum(i in vowels_ru for i in lower_set)
vowels_count_en = sum(i in vowels_en for i in lower_set)
if vowels_count_ru > 0 and vowels_count_en > 0:
    print('Количество гласных в русской и английской раскладки равно:', vowels_count_ru + vowels_count_en)
else:
    print('Количество гласных равно:', 
        vowels_count_ru if vowels_count_ru > 0 and vowels_count_en == 0 else vowels_count_en)
