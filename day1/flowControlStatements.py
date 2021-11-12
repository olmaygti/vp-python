# https://docs.python.org/3/tutorial/controlflow.html
def ifStatement(value):
    if value < 0:
        value = 0
        print('Negative changed to zero')
    elif value == 0:
        print('Zero')
    elif value == 1:
        print('Single')
    else:
        print('More')

def forStatement():
    collection1 = ['collection', 'of', 'values']

    for element in collection1:
        print(element)


    collection2 = {
        'key1': 'value1',
        'key2': 'value2'
    }

    for key in collection2:
        print('key ' + key + ' value ' + collection2[key])

    for duple in collection2.items():
        print(duple)

    for i in range(10):
        print(i)

def whileStatement():
    a = 10
    while a > 0:
        print(a)
        a = a - 1
        # a -= 1

#ifStatement(0)
# forStatement()
whileStatement()
