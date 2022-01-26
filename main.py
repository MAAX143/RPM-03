def input_valid():
    pass #Роман

def x2():
    pass #Саня

def x3_1():
    pass #Кирилл

def collatz(x):
    if x == 1:
        sp.append(x)
        return x
    elif x % 2 == 0:
        return x2(x)
    else:
        return x3_1(x)

print ('Список имеет вид: '+str(x))
sp = []
