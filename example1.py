person = {}

while True:
    name = input("name : ")
    age = input("age : ")
    person[name] = age

    addMore = input('add more y/n:')
    if addMore == 'y':
        continue
    else:
        break

ages = list(person.values())  # [20,40,20]

for age in set(ages):
    count = ages.count(age)
    print(f'{age} years old - {count}')

    # 20 years old -2
    # 40 years old - 1
