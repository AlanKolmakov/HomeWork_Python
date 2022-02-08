import json
from random import choice

def get_person():
    name, tel, nums = '', '', ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)
        nums += choice(num)

    person = {
        nums: {"name" + choice(num): name,
               "tel" + choice(num): tel}
    }
    return person


def write_json(person):
    try:
        person.update(json.load(open("persons.json")))
    except FileNotFoundError:
        dict.update(person)
    with open("persons.json", "w", encoding='UTF-8') as f:
        json.dump(person, f, indent=4)


for i in range(5):
    write_json(get_person())
