#!/usr/bin/env python
# coding: utf-8

# ![CFT-Los-R%C3%ADos.png](attachment:CFT-Los-R%C3%ADos.png)
# 
# # Guía de programación básica en Python
# 
# ## Curso: Fundamentos para Data Science Vespertino
# ## Profesor: Diego Miranda Olavarría
# 
# * Esta guía contiene operaciones básicas que se pueden realizar en lenguaje de programación Python

# # Operaciones básicas

# ### Este es un markdown, sirve pra escribir, por ejemplo títulos
# ### " Este es el título"

# In[1]:


# este símbolo sirve para dejar comentarios


# ### Operaciones matemáticas

# In[47]:


# suma de dos o más números
3+2+3


# In[48]:


# resta de dos o más números
8-2-3


# In[4]:


# Mulpiplicación
3*3*2


# In[5]:


# División
3/2/1


# In[46]:


# Potencia
3**2


# In[7]:


# Operacion compleja <----- tener en cuenta que la mutiplicación tiene prioridad antes que la suma o la resta
3-2+4*10


# In[8]:


# Asignación de un valor a una variable
n = 3
n


# In[9]:


n+3


# In[10]:


n = 3
m = 10
n+m


# In[11]:


nota1 = 5
nota2 = 7
nota_final = (nota1+nota2)/2
nota_final


# In[ ]:





# ### Textos

# In[12]:


"hola mundo"


# In[13]:


'hola mundo'


# In[14]:


'se puede incluir " "'


# In[15]:


n = "hola"
m = "mundo"
n+m


# In[16]:


"hola mundo"
"hola gente"
"hola a todos"


# In[17]:


print("hola mundo")
print("hola gente")
print("hola a todos")


# ### Listas

# In[ ]:





# In[18]:


numeros = [1,2,3,4] # Las listas se crean con []
numeros


# In[19]:


datos = [4,"hola mundo", -15, 3.14, "hola gente"]
datos


# In[20]:


datos.append("hola") # El comando .append agrega una variable nueva al final de la lista
datos


# In[ ]:





# ### Lectura por teclado

# In[50]:


valor = input("Introduce un valor: ")


# In[3]:


valor1 = int(input("Introduce un número entero: "))


# In[5]:


valor2 = float(input("Introduce un número flotante: "))


# ### A continuación crearemos un programa que calcule la edad:

# In[22]:


nombre = input("Ingrese Nombre: ")
año_nacimiento = int(input("Ingrese año de nacimiento: "))
año_actual = int(input("Ingrese año actual: "))
edad = año_actual-año_nacimiento
print("hola",nombre, "usted tiene", edad, "años")


# In[ ]:





# ### Ingresar 4 datos numéricos en una Lista 

# In[51]:


print("Ingrese un número: ")
a=input()
print("Ingrese un segundo número: ")
b=input()
print("Ingrese un tercer número: ")
c=input()
print("Ingrese un cuarto número: ")
d=input()
e=[a,b,c,d]
print(e,"Las listas pueden ser modificadas")


# In[52]:


e.sort()
print(e)


# In[25]:


e.reverse()
print(e)


# ### Diccionarios

# In[26]:


diccionario = {"azul": "blue", "naranjo":"orange", "yellow": "amarillo"} # se ingresa clave y valor y llevan llaves {}


# In[27]:


print(diccionario["azul"])


# In[28]:


diccionario2 = {"cristiano":"Portugal", "Messi":"Argentina", "alexis":"Chile", "Neymar":"Brasil"}


# In[29]:


print(diccionario2["alexis"])


# #### Ejercicio de Diccionario: Cree un diccionario cuya clave sea nombre y el valor sea la edad. Cree 4 y consulte la edad de uno de los nombres.

# In[30]:


ejercicio = {"diego": 36, "maria":20, "juan": 50, "pedro": 70}


# In[31]:


print(ejercicio["diego"])


# ### If

# #### El if es una sentencia condicional, este permite condicionar el flujo de un programa en diferentes caminos. Es como darle al computador la capacidad de distinguir varias opciones para actuar de forma distinta

# In[9]:


if True: # Los 2 puntos significa que esta "indentado", es decir que está dentro de la condición
    print("se cumple la condición")
    print("También se muestra este print")


# In[11]:


# Intenta hacer un if cambiando el True a False y comprueba
if False: 
    print("se cumple la condición")
    print("También se muestra este print")


# In[15]:


a = 10

if a == 2: # Se coloca con 2 signos igual
    print("a vale 2")
if a == 10:
    print("a vale 10") 

# El resultado solo reconocerá el segundo ya que es el que cumple la condición


# In[13]:


a = 5
b = 10

if a == 5:
    print("a vale", a)
if b == 10:
        print("y b vale",b)


# In[18]:


n = 0

if n == 0:
    print("n vale 0")
else:
    print("n vale", n)
    
# La sentencia else (sino) se encadena a un if para indicar el caso contrario cuando NO se cumple la condición


# In[20]:


n = float(input("Introduce un número: "))

if n == 0:
    print("n vale 0")
elif n >= 5:
    print("n vale 5")
elif n >=  7:
    print("n vale 7")
else:
    print("n vale ",n)

# la sentencia elif muestra por pantalla la condición que cumple n


# In[21]:


n = float(input("Introduce un número: "))

if n == 0:
    print("n vale 0")
if n == 5:
    print("n vale 5")
if n == 7:
    print("n vale 7")
else:
    print("n vale ",n)

# La sentencia if hace que muestre por pantalla todas las condiciones que cumple n


# #### Ejercicio: Crear un programa en donde el menú tenga las siguientes opciones: ENTRAR, SALUDAR, SALIR

# In[25]:


comando = input()
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola, como lo estás pasando?")
elif comando == "SALIR":
    print("Saliendo del sistema")
else:
    print("Este comando no se reconoce")


# In[26]:


nota = float(input("Introduce una nota: "))

if nota >= 6:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Reprobado")


# In[29]:


nota = float(input("Introduce una nota: "))

if nota >= 6:
    print("Nota Máxima")
if nota >= 5:
    print("Aprobado")
else:
    print("Reprobado")


# #### Ejercicio de If: Cree un programa en donde usted pueda introducir una nota y de salida que me diga si la nota es sobresaliente, bien, regular o reprobado

# In[44]:


nota = float(input("Introduce una nota: "))
if nota >= 6:
    print("Sobresaliente")
elif nota >= 5:
    print("Bien")
elif nota >= 4:
    print("regular")
else:
    print("Reprobado")


# ### Bucle While

# #### Bucle o Iterar: Es realizar una acción varias veces
# #### Ejemplo práctico: imagine que tiene una base de datos con un montón de registros y necesita encontrar uno en especial para consultarlo, para encontrar el elemento el computador debe recorrer entre todos los registros de la base de datos y compararlos hasta encontrar el que se busca
# 
# #### La clave del while es que a partir de una expresión relacional o lógica, de la misma forma que trabaja la sentencia if es capax de repetir un bloque de instrucciones siempre que este devuelva True, nosotros tenemos que encargarnos de cambiar esta condición a False para salir de la iteración o del bucle, sino estaríamos en un bucle infinito

# In[33]:


c = 0

while c <=5:
    c+=1
    print("c vale ",c)
    
# Le estamos pidiendo al bucle while que mientras la c sea mas pequeña que 5, esta me incremente el valor de c en 1


# In[53]:


c = 0

while c <=5:
    c+=1
    print("c vale ",c)
else:
    print("Se ha completado toda la iteración y c vale ",c)
    
# se puede utilizar un else que se cumplirá una vez cuando la condición no se cumpla


# In[44]:


# Sentencia break

c = 0
while c <= 5:
    c+=1
    if (c==4):
        print("Rompemos el bucle cuando c vale", c)
        break
    print("c vale",c)
else:
    print("Se ha completado toda la iteración y c vale", c)


# #### Ejercicio: Cree un menú interactivo que tenga 3 instrucciones ENTRAR, SALIR y COMANDO DESCONOCIDO

# In[37]:


print("Bienvenido")
while(True):
    print("""Elige una opción: 
    1) Entrar
    2) Salir""")
    opcion = input()
    if opcion == "1":
        print("Entrando al sistema")
    elif opcion == "2":
        print("Saliendo del sistema")
        break
    else:
        print("Comando desconocido")


# #### Ejercicio: Cree un menú interactivo que SALUDE, SUME 2 NÚMEROS y SALIR 

# In[41]:


print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ",n1+n2)
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
        


# ### Bucle for

# In[6]:


for x in range(0,5):
    print("el numero es: ",x)


# In[7]:


for x in "hola":
    print(x)


# In[1]:


numeros = [1,2,3,4,5,6,7]

for numero in numeros:
    print(numero)


# In[5]:


cadena = "Hola mundo"

for caracter in cadena:
    print(caracter)


# ### EJERCICIO FINAL: CREE UN CAJERO BANCARIO CON LO SIGUIENTE:
# ### 1) Cree una variable con el saldo
# ### 2) Cree un menú que ingrese al sistema
# ### 3) Consulte el saldo disponible
# ### 4) realice un giro, si el saldo es insuficiente cree alerta
# ### 5) Salga del sistema

# In[9]:





# In[ ]:





# In[ ]:





# In[ ]:




