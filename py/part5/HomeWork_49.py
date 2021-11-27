# Найти номер телефона в формате +7xxxxxxxxxx или 7xxxxxxxxxx
import re

s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
print(re.findall(r'\+?7\d{10}', s))
