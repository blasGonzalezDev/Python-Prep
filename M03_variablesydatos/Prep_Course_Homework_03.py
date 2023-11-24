#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
num = 73
print(num)
# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

NUM = 8.5
print(type(NUM))
# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(num))
# 4) Crear una variable que contenga tu nombre

# In[2]:
name = 'Blas'
# 5) Crear una variable que contenga un número complejo

# In[3]:
numComplejo = 1 + 2j
# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(numComplejo))
# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
pi = 3.1416
# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
boolVar1 = True
boolVar2 = True
print(type(boolVar1) == type(boolVar2))
print(bool(boolVar1) == bool(boolVar2)) # Se tra del mismo tipo de dato

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(boolVar1))
print(type(boolVar2))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
num2 = 5 + 2.6
# 11) Realizar una operación de suma de números complejos
# In[2]:
numComplejo2 = 2 + 3j
resultComplex = numComplejo + numComplejo2
print(resultComplex) 

# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
numReal = 5
numComplejo3 = 10 + 9j
resultSumRealComplex = numReal + numComplejo3
print(resultSumRealComplex)

# 13) Realizar una operación de multiplicación

# In[5]:
numMultiplicacion = 5*12
print(numMultiplicacion)

# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
print(2**8)
# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
cociente = 27/4
print(cociente)
# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
parteEntera = 27//4
print(parteEntera)
# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
resto = 27%4
print(resto)
# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
numeroOriginal = 4*parteEntera + resto
print(numeroOriginal)
# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
surName = 'Gonzalez'
nameAndSurName = name + ' ' + surName
print(nameAndSurName)
# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
print(2==2) #Porque en este caso son dos enteros y son dos numeros iguales por eso da True
# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
print(int(2)==float(2)) #A pesar de que los dos números son de tipos de datos distintos, da True porque númericamente son iguales
# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
a = float('3,8') # '3.8' es un tipo de dato String no es numerico y no puede hacer la conversion
# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
numValor = 3
numValor -= 1
print(numValor) 
# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
print(1<<2) #Porque se ha corrido dos bits, al correrse dos bits, el primer bit corresponde 2 a la 1, el siguiente bit correspeonde a 2 a la dos y como el número es 1
            # esto correspondería a 4, por ejemplo 5<<1 corresponde a 10 porque 5 en binario corresponde a 0101 y al correr 1 lugar corresponde a 1010 por lo que convirtiendo
            # este numero binario a decimal (1*2^3) + (0*2^0) + (1*2^2) + (0*2^0) =  10, equivale a 10 en decimal 
print(5<<1)
# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
print(2+2)
print(2+'2') #No esta permitido uno es numerico y otro es String, no se puede hacer una operacion con un tipo de dato numero 
             # y otro que sea cadena de caracteres, si lo dos operandos son del mismo tipo arrojaría un resultado en este caso numérico y se va realizar la operación
# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
nombre = 'Blas '
repetirNombre = 3
numero = '7'
veces = 4 



print(nombre*repetirNombre + " EDAD: " + str(int(numero)*veces))