import re

# Найти цифры, рядом с которой нет цифр: 1Х, Text ABC 123 A1B2C3
text = 'ABC 123 A1B2C3'
reg = r'(?<!\d)\d'
print(re.findall(reg, text, re.I))

# Найти цифры, рядом с которой нет цифр: Х, Text ABC 123 A1B2C3
text = 'ABC 123 A1B2C3'
reg = r'(?<!\d)\d(?!\d)'
print(re.findall(reg, text, re.I))

# Найти текст от #START# до #END#: text from #START# till #END#
text = 'from #START# till #END#'
reg = r'(?<=#START#).*?(?=#END#)'
print(re.findall(reg, text, re.I))

# Найти последовательность цифр, после которой идет ровно одно подчеркивание: 12_34__56
text = '12_34__56'
reg = r'\d+(?=_(?!_))'
print(re.findall(reg, text, re.I))
