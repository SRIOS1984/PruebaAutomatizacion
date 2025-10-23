
# ciclo while
""""
i = 1
while i <= 5:
 print (i)
i += 1
"""
#lista
"""
mi_lista = ['Argentina', 200, True]
#0,1,2
#print(mi_lista[0])
for i in mi_lista:
    print (i)
    """
"""
mi_lista.append (4000)
mi_lista.insert(1,"Alemania")

print(mi_lista)
"""
#tuplas
mi_tuplas = { "celeste", 200, "Rojo"}

#dicc
"""
persona = {
 "nombre" : "Jaime",
 "apellido": "Desconocido",
 "edad": 34
}
print (persona.keys())
print (persona.values())
"""
#FUNCIONES
"""
def saludo(nombre):
    print (f"Hola {nombre}") #funciones con argumento
saludo("Sil")
saludo("Wanda")
saludo("Brisa")
"""
#calculadora

def sumar (a,b):
    return a + b

def calculadora_simple(operacion, a, b):
    if operacion == 'sumar':
        return sumar(a,b)
    else:
        return'Operacion no valida'
print(calculadora_simple("sumar", 6,2))

#manejo de errores

try:                    
    resultado = 10/0
#except ZeroDivisionError :   print (f'Error : No se puede dividir entre 0')
except ZeroDivisionError as e:
    print(f'Error : {e}')

persona = {
    "nombre" : "Sil",
    "edad" : 41
}
try:
    print(persona ['nombre'])
except KeyError as e:
    print ('La clave no existe')