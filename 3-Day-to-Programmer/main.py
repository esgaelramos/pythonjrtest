from ins import ins_day
from datetime import date
from datetime import datetime
from datetime import timedelta

def WhenDayProgrammer(day, year):
    list_final = []

    # Put a valid year, less than 9999
    if year > 9999:
        list_final.append('Para esos años solo habrá robots, no estés molestando :)')
        return list_final

    # Put a valid year, greater than 0
    if year < 1:
        list_final.append('Para esos años ni siquiera teniamos calendario, no estés molestando :)')
        return list_final

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
        return list_final

    # Before 2002 don't celebrate!
    if year < 2002:
        list_final.append('Ese año aún no se celebraba el día del programador.')


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

    return list_final

def run():
    # Instrucciones
    ins_day
    
    # Start
    try:
        year = int(input('Put a year: '))
    except (ValueError, TypeError):
        error = print('ERROR: POR FAVOR SELECCIONA UN AÑO VÁLIDO')
        return error

    list_final = WhenDayProgrammer(256, year)

    print(list_final)
    
if __name__ == "__main__":
    run()