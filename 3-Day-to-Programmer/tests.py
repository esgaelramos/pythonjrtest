import unittest
from main import WhenDayProgrammer
from datetime import date, datetime, timedelta

# DAYS FOR TEST 8
today_now = date.today()
year = today_now.year
today_day = (today_now - date(year, 1, 1)).days + 1


# TESTS
class Check(unittest.TestCase):
    # TEST 1 - YEAR 1
    def test_dpay_one(self):
        test = WhenDayProgrammer(256, 1)
        self.assertEqual(test, ['Ese año aún no se celebraba el día del programador.'])

    # TEST 2 - YEAR 1000
    def test_dpay_thousand(self):
        test = WhenDayProgrammer(256, 1000)
        self.assertEqual(test, ['Ese año aún no se celebraba el día del programador.'])

    # TEST 3 - YEAR 2000
    def test_dpay_twothousand(self):
        test = WhenDayProgrammer(256, 2000)
        self.assertEqual(test, ['Ese año aún no se celebraba el día del programador.'])

    # TEST 4 - YEAR 2002
    def test_dpay_twothousandtwo(self):
        test = WhenDayProgrammer(256, 2002)
        self.assertEqual(test, [13, 'Septiembre', 2002, 'Viernes', 'celebró'])

    # TEST 5 - YEAR 2004
    def test_dpay_twothousandfour(self):
        test = WhenDayProgrammer(256, 2004)
        self.assertEqual(test, [12, 'Septiembre', 2004, 'Domingo', 'celebró'])

    # TEST 6 - YEAR 2020
    def test_dpay_twothousandtwenty(self):
        test = WhenDayProgrammer(256, 2020)
        self.assertEqual(test, [12, 'Septiembre', 2020, 'Sábado', 'celebró'])

    # TEST 7 - YEAR 2021
    def test_dpay_twothousandtwentyone(self):
        test = WhenDayProgrammer(256, 2021)
        self.assertEqual(test, [13, 'Septiembre', 2021, 'Lunes', 'celebró'])

    # TEST 8 - TODAY IS A DAY
    def test_dpay_today(self):
        test = WhenDayProgrammer(today_day, year)
        self.assertEqual(test, ['¡El día del programador se celebra hoy! ¡Felicidades!'])

    # TEST 9 - YEAR MORE 9999
    def test_dpay_morethan(self):
        test = WhenDayProgrammer(256, 10000)
        self.assertEqual(test,['Para esos años solo habrá robots, no estés molestando :)'])

    # TEST 10 - YEAR LESS 1
    def test_dpay_lessthan(self):
        test = WhenDayProgrammer(256, 0)
        self.assertEqual(test, ['Para esos años ni siquiera teniamos calendario, no estés molestando :)'])

    # TEST VALID UNTIL SEP 12, 2022
    # TEST 11 - FUTURE YEAR
    def test_dpay_twothousandtwentytwo(self):
        test = WhenDayProgrammer(256, 2022)
        self.assertEqual(test, [13, 'Septiembre', 2022, 'Martes', 'celebrará'])

    # TEST VALID UNTIL SEP 12, 2023
    # TEST 12 - FUTURE YEAR
    def test_dpay_twothousandtwentythree(self):
        test = WhenDayProgrammer(256, 2023)
        self.assertEqual(test, [13, 'Septiembre', 2023, 'Miércoles', 'celebrará'])

    # TEST VALID UNTIL SEP 12, 2100
    # TEST 13 - FUTURE YEAR
    def test_dpay_twothousandhundred(self):
        test = WhenDayProgrammer(256, 2100)
        self.assertEqual(test, [13, 'Septiembre', 2100, 'Lunes', 'celebrará'])

    # TEST VALID UNTIL SEP 12, 9999
    # TEST 14 - FUTURE YEAR
    def test_dpay_ninethousandnine(self):
        test = WhenDayProgrammer(256, 9999)
        self.assertEqual(test, [13, 'Septiembre', 9999, 'Lunes', 'celebrará'])


if __name__ == "__main__":
    unittest.main()