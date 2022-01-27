def input_valid():
    while True:
        x = int(input("Введите переменную x = "))
        if x > 0:
            collatz(x)
            break
        print("Неверное число, попробуйте другое")
    return x

def x2():
    pass #Саня

def x3_1():
    pass #Кирилл

def collatz():
    pass #Макс

input_valid()