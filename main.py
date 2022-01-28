def input_valid():
    while True:
        x = int(input("Введите переменную x = "))
        if x > 0:
            collatz(x)
            break
        print("Неверное число, попробуйте другое")
    return x

def x2(x):
    x = x / 2
    sp.append(int(x))
    return collatz(x)

def x3_1(x):
    x = x * 3 + 1
    sp.append(int(x))
    return collatz(x)

def collatz(x):
    if x in sp:
        print ('Значение уже есть в списке')
        return input_valid()
    while x != 1:
        sp.append(x)
        return x
    elif x % 2 == 0:
        return x2(x)
    else:
        return x3_1(x)

sp = []
input_valid()
print ('Список имеет вид: '+str(x))

