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
for dia in range(0, 365, 1):
    ingreso_diario = 10000 * 3**(dia/365 - 1) * 3 * 0.79
    ingresos_anuales += ingreso_diario

for semana in range(0, 52, 1):
    ingresos_anualesSem= 10000 * 3**(semana/52 - 1) * 3 * 0.13
    ingresos_anuales += ingresos_anualesSem

ingresos_anuales1 = ingresos_anuales+ingresos_anualesSem
ingresos_anuales=0
ingresos_anualesSem=0
print("Ingresos anuales año 1:", ingresos_anuales1)



for dia in range(0, 730, 1):
    ingreso_diario = 10000 * 3**(dia/365 - 1) * 3 * 0.79
    ingresos_anuales += ingreso_diario

for semana in range(0, 104, 1):
    ingresos_anualesSem = 10000 * 3**(semana/52 - 1) * 3 * 0.13
    ingresos_anuales += ingresos_anualesSem

ingresos_anuales2 = ingresos_anuales+ingresos_anualesSem
ingresos_anuales=0
ingresos_anualesSem=0
print("Ingresos anuales año 2:", ingresos_anuales2-ingresos_anuales1) 

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

for dia in range(0, 1460, 1):
    ingreso_diario = 10000 * 3**(dia/365 - 1) * 3 * 0.79
    ingresos_anuales += ingreso_diario

for semana in range(0, 208, 1):
    ingresos_anualesSem = 10000 * 3**(semana/52 - 1) * 3 * 0.13
    ingresos_anuales += ingresos_anualesSem

ingresos_anuales4 = ingresos_anuales+ingresos_anualesSem
ingresos_anuales=0
ingresos_anualesSem=0
print("Ingresos anuales año 4:", ingresos_anuales4-ingresos_anuales3)

for dia in range(0, 1825, 1):
    ingreso_diario = 10000 * 3**(dia/365 - 1) * 3 * 0.79
    ingresos_anuales += ingreso_diario

for semana in range(0, 260, 1):
    ingresos_anualesSem = 10000 * 3**(semana/52 - 1) * 3 * 0.13
    ingresos_anuales += ingresos_anualesSem

ingresos_anuales5 = ingresos_anuales+ingresos_anualesSem
ingresos_anuales=0
ingresos_anualesSem=0
print("Ingresos anuales año 5:", ingresos_anuales5-ingresos_anuales4)

#52
#104
#156
#208
#260


#OPTIMISTA
#Ingresos anuales año 1: 21.468.163
#Ingresos anuales año 2: 85.842107
#Ingresos anuales año 3: 
#Ingresos anuales año 4: 
#Ingresos anuales año 5: 

#NEUTRO
#Ingresos anuales año 1: 
#Ingresos anuales año 2: 
#Ingresos anuales año 3: 
#Ingresos anuales año 4: 
#Ingresos anuales año 5: 

#PESIMISTA
#Ingresos anuales año 1:
#Ingresos anuales año 2: 
#Ingresos anuales año 3: 
#Ingresos anuales año 4: 
#Ingresos anuales año 5: 

#####OLD VERSION


#OPTIMISTA
#Ingresos anuales año 1: 61.039.712
#Ingresos anuales año 2: 183.119.137
#Ingresos anuales año 3: 549.357.414
#Ingresos anuales año 4: 1.648.072.241
#Ingresos anuales año 5: 4.944.216.722

#NEUTRO
#Ingresos anuales año 1: 30.519.856
#Ingresos anuales año 2: 91.559569
#Ingresos anuales año 3: 274.678.707
#Ingresos anuales año 4: 824.036.120
#Ingresos anuales año 5: 2.472.108.361

#PESIMISTA
#Ingresos anuales año 1: 6.103.971
#Ingresos anuales año 2: 18.311.914
#Ingresos anuales año 3: 54.935.741
#Ingresos anuales año 4: 164.807.224
#Ingresos anuales año 5: 494.421.672
