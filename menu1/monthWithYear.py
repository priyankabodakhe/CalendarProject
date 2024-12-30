import calendar as cal
print("------Calender for given month and year-----\n")
def month_with_year(m,y):
    yy=int(y);
    mm=int(m);
    print("\n",cal.month(yy,mm))