import calendar as cal
print("------Calender for given year-----\n")
def year_cal(y):
    yy=int(y)
    for i in range(1,13):
        mm=int(i)
        print("\n",cal.month(yy,mm))