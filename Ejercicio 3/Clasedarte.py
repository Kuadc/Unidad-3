from datetime import date

from dateutil.relativedelta import relativedelta

fecha1 = date(int(input("Ingrese Año: ")),int(input("Ingrese mes: ")),int(input("Ingrese dia: ")))
fecha2 = date.today()
fecha3 = relativedelta(months=6)
fecha4 = fecha2 +fecha3
print(fecha4)
if fecha2 + fecha3 < fecha1:
    print("es menor")
else:
    print("Es mayor")
