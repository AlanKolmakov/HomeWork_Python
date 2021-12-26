import os

# Вывести на экран сначала все файлы, а затем все директории расположенные в корневой директории дерева python.
print("Все папки и файлы:", os.listdir('.'))
lst1 = []
for file in os.listdir('files'):
    if os.path.isfile(os.path.join("files", file)):
        lst1.append('files\\' + file)
for dir_name in os.listdir('files'):
    if os.path.isdir(os.path.join('files', dir_name)):
        lst1.append('files\\' + dir_name)
print(lst1)

# Вывести на экран имена и размер всех непустых файлов дерева.
# Создайте директорию work/empty_files и переместите в нее все пустые файлы,
# при этом для каждого перемещенного файла должно быть выведено соответствующее сообщение,
# содержащее имя файла, старый путь к файлу относительно корневой директории и новый путь к файлу после перемещения.
root = "files"
folder = "empty_files"
for root, dirs, files in os.walk(root):
    if root == folder:
        continue
    for name in files:
        s = os.path.getsize(os.path.join(root, name))
        if s != 0:
            print(name, s, "bytes")
        if s == 0:
            old_file = os.path.join(root, name)
            new_file = os.path.join(folder, name)
            os.rename(old_file, new_file)
            print(f"пустой файл {name} перемещен из папки {root} в папку {new_file}")

