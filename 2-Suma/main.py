from ins import ins_suma

def Suma(n):
    list = []
    
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)

    final = sum(list)

    return final

def run():
    # Instrucciones
    ins_suma
    
    # Start
    try:
        n = int(input('Put at number: '))
    except (ValueError, TypeError):
        error = print('ERROR: POR FAVOR INGRESE UN NÚMERO NATURAL')
        return error

    final = Suma(n)

    print('The answer is:', final)


if __name__ == "__main__":
    run()