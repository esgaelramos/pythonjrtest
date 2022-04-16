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


    # def DateFormat(day_let, monthy):
    #     monthys = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    #     day_lets = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")


    def WhenDayProgrammer(day, year):
        list_final = []
        
        today = date.today()        

        # Less 1, because in dates don't count January 0
        day_programmer = day - 1

        # Isn't a year parameter, because need check the same date, and that change it every year, for this 'today.year'
        date_programmer_now = date(today.year, 1, 1) + timedelta(days=day_programmer)

        # It's today?
        if date_programmer_now == today:
            list_final.append('¡El día del programador se celebra hoy! ¡Felicidades!')
            # print(list_final[0])
            # print(list_final)

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

            if date_programmer_now < today:
                cele_word = 'celebró'

            if date_programmer_now > today:
                cele_word = 'celebrará'

            list_final.append(day_num)
            list_final.append(monthy)
            list_final.append(year)
            list_final.append(day_let)
            list_final.append(celeword)

            return list_final

            # # Day Letter Week
            # print(day_let)

            # # Day Month Number
            # print(date_final.day)
            # day_num = date_final.day
            # print('Save in var', day_num)
            # list_final.append(day_num)

            # # Month Letter
            # print(monthy)

            # # Month Number
            # print(date_final.month)

            # # Year 
            # print(date_final.year)

            # list_final.append(year)

            # print(list_final)




            # # Print Date with Standart Format
            # print("Fecha de ese año", date_final)


            # Date or Datetime | USE DATE TIME FOR WEEKLY
            # date_final = date(year, 1, 1) + timedelta(days=day_programmer)


            # list_final.append('Vamos a calcular baby.')
            # print(list_final)

        # print('El día para testear', date_equal)

        # print('El día de hoy es: ', today)
            # Select the day of Programmer => 256

    # print('Con input es: ', year)

    # fecha2 = datetime(today.year, 1, 1) + timedelta(days=day_programmer)

    # month = months[date.month - 1]

    # year = int(input('Put a year baby: '))

    # year = int(input('Put a year baby: '))

    # list_test = ['rosa']
    # list_test.append(year)

    # print(list_test)

    # tu_anio = list_test[1]

    # print(list_test[1])
    # print('Vamos a bailar', tu_anio)

    # Put in a var every index of the final list for test

    # Var if today is day programmer
    # today = date.today()
    # print(today)
    # print("El día actual es {}".format(today.day))

    
    # print("El día actual es {}".format(today.day))
    # print("El mes actual es {}".format(today.month))
    # print("El año actual es {}".format(today.year))


    # # #Who calculate days?
    # # hoy = datetime.now()
    # # numero_dia = (hoy - datetime(hoy.year, 1, 1)).days + 1
    # # print(numero_dia)
    
    # hoy = datetime.now()

    # day_pro = (hoy - datetime(hoy.year, 1, 1)).days + 1

    # print(day_pro)

    # fecha2 = datetime(hoy.year, 1, 1) + timedelta(days=256)
    # print("\tFecha2:", fecha2)


    # def current_date_format(date):
    #     months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    #     day_lets = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
    #     day = date.day
    #     month = months[date.month - 1]
    #     day_let = day_lets[datetime.today().weekday()]
    #     year = date.year
    #     messsage = "{}. {} de {} del {}".format(day_let, day, month, year)

    #     return messsage

    # now = datetime.now()
    # print(current_date_format(now))


    # print(datetime.today().weekday())
    # 104
    WhenDayProgrammer(104, year)

if __name__ == "__main__":
    run()