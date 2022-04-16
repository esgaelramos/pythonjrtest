def run():
    # Si listamos todos los números naturales debajo del 10 que son múltiplos del 3 o 5, obtenemos 3, 5, 6, y 9. 
    # La suma de estos múltiplos es 23.
    # Escribe una función que reciba n y retorne la suma de todos los múltiplos de 3 o 5 debajo de n.
    
    list = []

    n = int(input('Put at number baby: '))
    
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            list.append(i)

    final = sum(list)

    print('The answer is: ')
    print(final)    



if __name__ == "__main__":
    run()