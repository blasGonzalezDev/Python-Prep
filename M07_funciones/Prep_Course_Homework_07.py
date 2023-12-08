#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:
def is_primo(numero):
    is_primo_ban = True 
    if numero>0:
        if numero == 1:
            return False
        else:
            for i in range(2, numero):
                if numero % i==0:
                    is_primo_ban = False
                    break
            return is_primo_ban
print(is_primo(13))




# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:
def list_primos(numeros):
    lista_numeros_primos = list()
    for numero in numeros:
        if(is_primo(numero)):
            lista_numeros_primos.append(numero)
    return lista_numeros_primos
lista_numeros = [2,3,4,5,6,7,8,9,10,11,12,13,1,4,15,16,17,18,19,20]

print(list_primos(lista_numeros))


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:
def numero_mas_veces_repetido(numeros):
    numeros_key_value = dict()
    mayor = 0
    veces = 0  
    for numero in numeros:
        numeros_key_value[numero] = numeros.count(numero)
    for key_value in numeros_key_value:
        if(numeros_key_value[key_value]>mayor):
            veces = numeros_key_value[key_value]
            mayor = key_value
    return mayor, veces

lista_numeros_repetidos = [2,3,4,5,6,7,8,9,10,11,12,13,1,4,15,16,17,18,19,20, 2,3,4,5,6,7,8,9,10,11,12,13,1,4,15,16,17,18,19,20, 20]

print(numero_mas_veces_repetido(lista_numeros_repetidos))


# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:
def convert_unit_of_measure(valor, unidad_medida_origen, unidad_medida_destino):
    if unidad_medida_origen=='Celsius':
        if unidad_medida_destino =='Farenheit':
            return (valor * 9/5) + 32
        elif unidad_medida_destino =='Kelvin':
            return valor + 273.15
        else:
            return valor

    elif unidad_medida_origen=='Farenheit':
        if unidad_medida_destino =='Celsius':
            return (valor - 32)/(9/5)
        elif unidad_medida_destino =='Kelvin':
            return ((valor - 32)/(9/5)) + 273.15
        else:
            return valor
    else:
        if unidad_medida_destino =='Celsius':
            return valor  - 273.15
        elif unidad_medida_destino =='Farenheit':
            return ((valor  - 273.15) * 9/5) + 32
        else:
            return valor
convert_unit_of_measure(300,'Kelvin','Celsius')



# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:
metricas = ['Celsius', 'Kelvin', 'Farenheit']  # Lista de las unidades métricas

for i in range(0, 3):  # Bucle exterior que itera sobre los índices de la lista de metricas
    for j in range(0, 3):  # Bucle interior que itera sobre los índices de la lista de metricas
        # Se imprime la conversión de 1 grado desde la unidad métrica en el índice i a la unidad métrica en el índice j
        # utilizando la función de conversión_grados
        print('1 grado', metricas[i], 'a', metricas[j], ':', convert_unit_of_measure(1, metricas[i], metricas[j]))



# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def factorial_numero(numero):
    if type(numero) == float:
        return 'Es flotante'
    if not(numero>0):
        return 'Es numero es negativo o igual cero'
    return factorial_calculate(numero)

def factorial_calculate(numero):
    if numero>1:
        return numero * factorial_calculate(numero-1)
    else:
        return numero

print(factorial_numero(10))
