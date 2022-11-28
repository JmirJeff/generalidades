# generamos en dia cuando ya ha pasado un porcentaje del año

def fGetDays(year):
    # asumimos 365 dias
    numDays = 365
    from datetime import date, timedelta
    d = date(year,1,1)-timedelta(days=1)
    for i in range(1,101):
        pDays = round(i*365/100)
        g = d + timedelta(days=pDays)
        print(str(i)+"%\t es el\t",g)

if __name__=="__main__":
    fGetDays(2022)
