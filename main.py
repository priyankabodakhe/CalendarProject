import calendar as cal
from menu1 import monthWithYear
from menu2 import yearCal
print("------Calendar Project in Python-----\n")
print("Enter 'x' for exit.")
menu = input("Enter menu option (m1 for month/year, m2 for full year): ")

if menu == 'x':
    exit()

elif menu == 'm1':
    y = input("Enter year: ")
    m = input("Enter month: ")
    monthWithYear.month_with_year(m, y)

elif menu == 'm2':
    y = input("Enter year: ")
    yearCal.year_cal(y)

else:
    print("Invalid menu option!")
