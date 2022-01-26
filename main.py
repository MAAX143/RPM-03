def input_valid():
    x = float(input("Введите переменную x = "))
    if x % 1 == 0:
        if x > 1:
            collatz()
        else:
            input_valid()
    else:
        input_valid()

def x2():
    pass #Саня

def x3_1():
    pass #Кирилл

def collatz():
    pass #Макс
input_valid()
