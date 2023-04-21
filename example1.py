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

for (key, value) in person.items():
    print(f'{key} is {value} year old')

print(person)
