import pprint

def run():
    # Escribe una funcion que reciba un numero n, que indica el limite superior de una lista de los números del 1 a n.
    # La función debe retornar dicha lista con sus elementos en forma de cadena, pero por cada múltiplo de 3 debe ser sustituido por 'Humpty' en vez del número, y para los múltiplos de 5, debe ser sustituido por 'Dumpty' en vez del número.
    # Para los números que son múltiplos tanto de 3 como de 5 debe ser sustituido por 'HumptyDumpty'.

    list = []

    n = int(input('Put at number baby: '))
    n += 1

    for i in (n+1 for n in range(n)):
    # for i in range(n): # Put 0
        if i % 3 == 0 and i % 5 == 0:
            i = 'HumptyDumpty'
            list.append(str(i))
        elif i % 3 == 0:
            i = 'Humpty'              
            list.append(str(i))
        elif i % 5 == 0:
            i = 'Dumpty'              
            list.append(str(i))
        else:
            list.append(str(i))
    print(list)

    # for i in list:
    #     print(i + '\n', end=' ') 
    
    printer = pprint.PrettyPrinter(indent=0, width=40)
    printer.pprint(list)


if __name__ == "__main__":
    run()