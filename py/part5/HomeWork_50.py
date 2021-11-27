# Проверка соответствия пароля. Он должен может состоять из цифр, букв английского алфавмта, символов
# дефис, собака и подчеркивание. Длина пароля от 6 до 18 символов.
import re

password = "my-p@ssw0rd"
print(f'{password} - Valid' if re.match(r'^[A-Za-z\d@_-]{6,18}$', password) else f'{password} - Invalid')
