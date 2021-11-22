# Отсортировать список объектов по имени студентов и итоговым оценкам в порядке убывания

students_score = [{'name': 'Jennifer', 'final': 95},
                  {'name': 'David', 'final': 92},
                  {'name': 'Nikolas', 'final': 98}]

print(sorted(students_score, key=lambda x: x['name']))
print(sorted(students_score, key=lambda x: x['final'], reverse=True))
