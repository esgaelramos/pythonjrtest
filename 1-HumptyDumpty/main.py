import pprint
from ins import ins_humpty

def Humpty(n):

    list = []

    for i in (n+1 for n in range(n)):
        if i % 3 == 0 and i % 5 == 0:
            i = 'HumptyDumpty'
            list.append(i)
        elif i % 3 == 0:
            i = 'Humpty'              
            list.append(i)
        elif i % 5 == 0:
            i = 'Dumpty'              
            list.append(i)
        else:
            list.append(str(i))
    return list

def run():
    # Instrucciones
    ins_humpty
    
    # Start
    try:
        n = int(input('Put at number: '))
    except (ValueError, TypeError):
        error = print('ERROR: POR FAVOR INGRESE UN NÚMERO NATURAL')
        return error

    list = Humpty(n)

    printer = pprint.PrettyPrinter(indent=0, width=40)
    printer.pprint(list)


if __name__ == "__main__":
    run()