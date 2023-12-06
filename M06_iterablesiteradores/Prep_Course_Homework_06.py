#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:

lista_negativos = list()
numero = -15
while numero<=-1:
    lista_negativos.append(numero)
    numero +=1
print(lista_negativos)



# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

i=0
while i<len(lista_negativos):
    if lista_negativos[i]%2==0:
        print(lista_negativos[i])
    i+=1



# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

for negativo in lista_negativos:
    if negativo%2==0:
        print(negativo)



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

for negativo in lista_negativos[:3]:
    print(negativo)


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:

for posicion, numero in enumerate(lista_negativos):
    print(posicion, numero)


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

lista = [1,2,5,7,8,10,13,14,15,17,20]
num = 1
while num<=20:
    if not(num in lista):
        lista.insert(num-1,num)
    num +=1
print(lista)



# In[11]:



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:

n0=0
n1=1
lista_fibonacci = list()
lista_fibonacci.append(n0)
lista_fibonacci.append(n1)

#print(lista_fibonacci.index(1))

for i in range(2,30):
    lista_fibonacci.append(lista_fibonacci[i-1]+lista_fibonacci[i-2])
    i+=1
print(lista_fibonacci)



# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

suma = sum(lista_fibonacci)
print(suma)


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:

ultimos_15 = 15
ultimos_5_del_15 = ultimos_15 - 5

while ultimos_5_del_15<ultimos_15:
    print(lista_fibonacci[ultimos_5_del_15]/lista_fibonacci[ultimos_5_del_15-1])
    ultimos_5_del_15 +=1 


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
print([pos for pos,letra in enumerate(cadena) if letra == 'n'])



# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:
dicc_pais_ciudad_continente = {
    'Ciudad': ['Buenos Aires', 'Caracas', 'Bogotá', 'Lisboa', 'Roma'],
    'País': ['Argentina', 'Venezuela', 'Colombia', 'Portugal', 'Italia'],
    'Continente': ['América', 'América', 'América', 'Europa', 'Europa']
}

for i in dicc_pais_ciudad_continente:
    print(i)




# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:

list_cadena = list(cadena)
#print(list_cadena)
for letra in list_cadena:
    print(letra)



# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

lista_pais = ['Paraguay','Argentina','Brasil','Uruguay','Bolivia']
lista_ciudades = ['Asucion','Buenos Aires','Brasilia','Montevideo','La paz']
tupla_pais_ciudades = zip(lista_pais,lista_ciudades)
print(list(tupla_pais_ciudades))



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

print([num for num in lis if num%7==0])



# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
cantidad = 0
for elemento in lis:
    if type(elemento)== list:
        cantidad+= len(elemento)
    else:
        cantidad+=1
print('En total hay : '+str(cantidad)+' de elementos')


# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:


lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
lista_nueva = list()
cantidad = 0
for elemento in lis:
    if type(elemento)!= list:
         lista_nueva.append([elemento])
    else:
        lista_nueva.append(elemento)
print(lista_nueva)
