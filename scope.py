# global variable
name = "Htet Ko"


def sayMyName():
    global name
    name = "aung aung"
    print(name)


sayMyName()

print(name)
