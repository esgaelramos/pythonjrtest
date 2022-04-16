from datetime import date
from datetime import datetime
from datetime import timedelta

def run():
    # El día del programador corresponde al día 256 del año. 
    # Este número fue elegido porque es la cantidad de valores que se pueden representar en un byte de 8 bits, una cifra muy reconocible por los programadores y por supuesto es un valor menor a 365, que son los días del año.
    # Escribe una funcion que reciba como argumento el año.
    # Al ser llamada debe retornar una lista compuesta de los siguientes elementos en ese orden:

    # el día del mes en que se celebrará el día del programador,
    # el nombre del mes en que se celebrará el día del programador,
    # el año que se introdujo como entrada,
    # el nombre del día de la semana en que se celebrará el día del programador,
    # y la palabra "celebrará".

    # Por ejemplo si ejecuto la función con el parámetro 2025, el programa debe retornar [13, "septiembre", 2021, "sábado", "celebrará"], con lo que yo podría formar la frase: 
    # El día del programador del año 2025 se celebrará el sábado 13 de septiembre.
    # El programa debe calcular cuál es el día 256 del año, es más, esto debe ser un parámetro interno y debería poder modificarse, de modo que si decidimos que el día del programador fuera el día 128 o el día 48 del año esto pueda modificarse fácilmente. 
    # (Esto es para evitar que calculen a secas el día del programador como 12 ó 13 de septiembre según si el año es bisiesto).
    # Si el año es menor a 2002 la lista que retorna la función sólo tendrá un elemento, una cadena de texto con el mensaje Ese año aún no se celebraba el día del programador.
    # Si el año ingresado está en el pasado, el último elemento de la lista, la palabra, debe estar en pretérito (para que yo pueda armar la frase, por ejemplo: El día del programador del año 2014 se celebró el sábado 13 de septiembre).
    # Si ejecutas el programa el mismo día del programador, la función debería retornar una lista con un solo elemento, la cadena de texto con el mensaje ¡El día del programador se celebra hoy! ¡Felicidades!.

    year = int(input('Put a year baby: '))

    def WhenDayProgrammer(day, year):
        list_final = []
        
        today = datetime.today()        
        today_date = date.today()

        # Less 1, because in dates don't count January 0
        day_programmer = day - 1

        # Isn't a year parameter, because need check the same date, and that change it every year, for this 'today.year'
        date_programmer_now = date(year, 1, 1) + timedelta(days=day_programmer)
        # Another Var with DateTime for select the Weekly
        date_final = datetime(year, 1, 1) + timedelta(days=day_programmer)

        # It's today?
        if date_programmer_now == today_date:
            list_final.append('¡El día del programador se celebra hoy! ¡Felicidades!')
            # print(list_final[0])
            # print(list_final)

        else:
            # Before 2002 don't celebrate!
            if year < 2002:
                list_final.append('Ese año aún no se celebraba el día del programador.')
                # print(list_final[0])
                # print(list_final)


            if year >= 2002:
                # Calculate the programmer day since first day of year
                date_final = datetime(year, 1, 1) + timedelta(days=day_programmer)

                # Save Day Month Number as Var for Design
                day_num = date_final.day

                # Select the Month and Change Name
                monthys = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")            
                monthy = monthys[date_final.month - 1]

                # Select the Letter Day and Change Name
                day_lets = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
                day_let = day_lets[date_final.date().weekday()]

                if date_final < today:
                    cele_word = 'celebró'

                if date_final > today:
                    cele_word = 'celebrará'

                list_final.append(day_num)
                list_final.append(monthy)
                list_final.append(year)
                list_final.append(day_let)
                list_final.append(cele_word)

        print(list_final)

        return list_final


    WhenDayProgrammer(104, year)

if __name__ == "__main__":
    run()