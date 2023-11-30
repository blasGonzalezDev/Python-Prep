#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
lista_cuidades = ['Asuncion', 'Buenos Aires', 'Brasilia', 'Bogotá', 'Lima', 'La Paz']

for cuidad in lista_cuidades:
    print(cuidad)



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(lista_cuidades[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(lista_cuidades[1:4])



# 4) Visualizar el tipo de dato de la lista

# In[12]:

print(type(lista_cuidades))



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(lista_cuidades[2:])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(lista_cuidades[:4])

    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

lista_cuidades.append("Caracas")
lista_cuidades.append("Asuncion")







# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:
lista_cuidades.insert(3,"Montevideo")




# In[21]:

print(lista_cuidades)


# 9) Concatenar otra lista a la ya creada

# In[22]:
lista_ciudades_europa = ['París', 'Londres', 'Berlín', 'Madrid', 'Roma', 'Ámsterdam', 'Praga', 'Viena', 'Atenas', 'Varsovia']
lista_cuidades.extend(lista_ciudades_europa)
print(lista_cuidades)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

print(lista_cuidades.index('Asuncion')) # Si que encuentra solo el primero entre los dos



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

lista_cuidades.index('España') #Da un error que elemento buscado no esta en la lista



# 12) Eliminar un elemento de la lista

# In[25]:


lista_cuidades.remove('Lima')


# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

lista_cuidades.remove('España') #Da un error que el elemento a eliminar no existe



# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

ultimo_elemento = lista_cuidades.pop()
print(ultimo_elemento)



# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(lista_cuidades*4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
lista_enteros = list()
for i in range(1,21):
    lista_enteros.append(i)
tupla_enteros = tuple(lista_enteros)
print(type(tupla_enteros))
print(tupla_enteros)



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:
print(tupla_enteros[10:16])



# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:
print(20 in tupla_enteros)
print(30 in tupla_enteros)

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:
elemento = 'París'
if(not(elemento in lista_cuidades)):
    lista_cuidades.append(elemento)
    print('Se ha agregado ' +elemento+ ' a la lista de cuidades')
else:
    print(elemento + " ya exist en la lista de ciudades")

# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:
print(lista_cuidades.count("Asuncion"))
print(tupla_enteros.count(1))


# 21) Convertir la tupla en una lista

# In[52]:
lista_enteros_convert = list(tupla_enteros)
print(lista_enteros_convert)


# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

primero = tupla_enteros[0]
segundo = tupla_enteros[1]
tercero = tupla_enteros[2]

print(primero)
print(segundo)
print(tercero)



# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:

dicccionario_cuidad_pais_continente = dict()

dicccionario_cuidad_pais_continente['ciudad'] = lista_cuidades
dicccionario_cuidad_pais_continente['pais'] = ''
dicccionario_cuidad_pais_continente['continente'] = ''

print(dicccionario_cuidad_pais_continente)




# 24) Imprimir las claves del diccionario

# In[59]:
print(dicccionario_cuidad_pais_continente.keys())



# 25) Imprimir las ciudades a través de su clave

# In[61]:

print(dicccionario_cuidad_pais_continente['ciudad'])


