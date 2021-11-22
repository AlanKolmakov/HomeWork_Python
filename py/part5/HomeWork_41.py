# Получить минимальную и максимальную итоговую оценку студентов

students_score = [{'name': 'Jennifer', 'final': 95},
                  {'name': 'David', 'final': 92},
                  {'name': 'Nikolas', 'final': 98}]

print(f"Максимальная оценка: {max(students_score, key=lambda x: x['final'])}")
print(f"Минимальная оценка:  {min(students_score, key=lambda x: x['final'])}")
