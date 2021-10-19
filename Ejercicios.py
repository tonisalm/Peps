#Ejercicio 1

def print_down_from(n):
    for x in range(n, 0, -1):
        print(x, end=' ')

#print_down_from(10)

#Ejercicio 3

def count_spaces(texto):
    c = 0
    for x in texto:
        if x==' ':
            c += 1
    print(c)

#count_spaces('h o l a')

#Ejercicio 4

def print_spaced(texto):
    l = len(str(texto))
    c = 1
    for x in texto:
        if c == l:
            print(x)
        else:
            print(x, end=' ')
        c += 1

print_spaced('tonikun')

#Ejercicio 7

def ask_for_password():
    import random
    numero = random.radint(1,100)
    endgame = 0
    while endgame != 1:
        print('Averigua el número entre 1 y 100')
        entered = input()