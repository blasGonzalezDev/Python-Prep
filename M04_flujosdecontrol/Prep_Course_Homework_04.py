#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
numEntero = 10
if numEntero > 0:
    print("Es mayor a cero")
elif numEntero < 0:
    print("Es menor a cero")
else:
    print("Es igual a cero")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

precio = 10000
nombre = "COCA COLA"
if type(precio) !=  type(nombre):
    print("No son el mismo tipo de dato")
else:
    print("Son el mismo tipo de dato") 



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1,21):
    if(i%2==0):
        print("El ", str(i)," es par")
    else:
        print("El ",str(i), " es impar")



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(0,6):
    print(str(i),  " elevado a la 3 es igual a: ",str(i**3))



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

veces = 10
for i in range(0,veces):
    print(i)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
factorial = 1
numeroEntero =7


if (type(numeroEntero) == int):
    print("El factorial de: ",str(numeroEntero)," es:")
    while numeroEntero > 0:
        factorial = factorial*numeroEntero;
        numeroEntero-=1
    print(str(factorial))
else:
    print("No es un numero entero")




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
numero = 3
while numero > 0:
    for i in range(1,11):
        print(str(numero),"X",str(i), " = ", str(numero*i))
    numero -=1




# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

numero = 3
for num in range(1,numero+1):
    i=1
    while i<=10:
        print(str(num),"X",str(i), " = ", str(num*i))
        i+=1



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
for num in range(0, 31):
    numeroPrimo = True
    if num !=0 and num!= 1:
        for div in range(2,num):
            if num%div==0:
                numeroPrimo = False
                #break
        if numeroPrimo == True:
            print(str(num)+" es primo")



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

for num in range(0, 31):
    numeroPrimo = True
    if num !=0 and num!= 1:
        for div in range(2,num):
            if num%div==0:
                numeroPrimo = False
                break # Al agregarle un break en este punto no buscará más números 
        if numeroPrimo == True:
            print(str(num)+" es primo")



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
totalCicloSinBreak = 0
for num in range(0, 31):
    numeroPrimo = True
    if num !=0 and num!= 1:
        for div in range(2,num):
            totalCicloSinBreak+=1
            if num%div==0:
                numeroPrimo = False
                #break
        if numeroPrimo == True:
            print(str(num)+" es primo")
print("Total de ciclos sin break: ", totalCicloSinBreak)



# In[57]:

totalCicloConBreak = 0
for num in range(0, 31):
    numeroPrimo = True
    if num !=0 and num!= 1:
        for div in range(2,num):
            totalCicloConBreak+=1
            if num%div==0:
                numeroPrimo = False
                break
        if numeroPrimo == True:
            print(str(num)+" es primo")
print('Cantidad de ciclos: ' + str(totalCicloConBreak))
print('Se optimizó a un ' + str(totalCicloConBreak/totalCicloSinBreak) + '% de ciclos aplicando break')


# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

numero = 99
while numero <=300:
    if numero%12!=0:
        numero+=1
        continue
    print(numero)
    numero +=1



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
numero = 2 
while(True):
    numeroPrimo = True
    for i in range(2,numero):
        if numero%i==0:
            numeroPrimo = False
            break
    if numeroPrimo == True:
        print('¿Desea encontrar el siguiente número primo? Presione cualquier tecla, 1 para salir')
        if input()!='1':
            print(numero)
        else:
            print('Se finaliza el proceso')
            break
    numero+=1



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

numero = 100
while numero <=300:
    if(numero % 3 == 0 and numero % 6 == 0):
        print("El numero es: ",numero)
        break
    numero+=1

