ingresos_anuales = 0
ingresos_anualesSem = 0
suscriptores_actuales = 0  # Suscriptores al día 365

ingresos_anuales1=0
ingresos_anuales2=0
ingresos_anuales3=0
ingresos_anuales4=0
ingresos_anuales5=0


#365
#730
#1095
#1460
#1825


for dia in range(0, 1095, 1):
    ingreso_diario = 10000 * 3**(dia/365 - 1) * 3 * 0.79
    ingresos_anuales += ingreso_diario

for semana in range(0, 156, 1):
    ingresos_anualesSem = 10000 * 3**(semana/52 - 1) * 3 * 0.13
    ingresos_anuales += ingresos_anualesSem

ingresos_anuales3 = ingresos_anuales+ingresos_anualesSem
ingresos_anuales=0
ingresos_anualesSem=0
print("Ingresos anuales año 3:", ingresos_anuales3-ingresos_anuales2)
