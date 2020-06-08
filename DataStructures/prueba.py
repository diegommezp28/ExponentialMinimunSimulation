
def prueba():
    print('hola')
    yield 1
    print('mundo')
    yield 2
    print('soy ')
    yield 3
    print('Diego')

# for i in prueba():
#     print(i)

class Generator:
    def __iter__(self):
        list = range(3)
        for i in list:
            yield i*i

clase = Generator()

for i in clase:
    print(i)


