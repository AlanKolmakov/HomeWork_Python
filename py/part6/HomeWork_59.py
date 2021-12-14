# Объединение файлов
file_name1 = 'test_file1.txt'
file_name2 = 'test_file2.txt'
file_name3 = 'test_file3.txt'
# Открываем (или создаем, если их нет) файлы в режиме записи и записываем туда тестовый текст
with open(file_name1, 'w', encoding='utf-8') as text1, open(file_name2, 'w', encoding='utf-8') as text2:
    text1.write('This is line1 on file1\nThis is line2 on file1\nThis is line3 on file1\n')
    text2.write('This is line1 on file2\nThis is line2 on file2\nThis is line3 on file2\n')
# Открываем файлы для чтения
with open(file_name1, 'r', encoding='utf-8') as f1, open(file_name2, 'r', encoding='utf-8') as f2:
    # Считываем файлы
    l1 = f1.readlines()
    l2 = f2.readlines()
# Объединяем списки
l3 = l1 + l2
# Открываем файл для записи
with open(file_name3, 'w', encoding='utf-8') as f3:
    f3.writelines(l3)
