#CALCULADORA CON FUNCIONES
def sumar(a, b):
    return a+b
def restar (a,b):
    return a-b
def dividir (a,b):
    return a//b #ejemplo : 2.9 =>2

"""def calculadora_simple(operacion , a, b):  
    try:
        a = int (a)
        b = int (b)

        if operacion == 'sumar':
            return sumar(a,b)
        elif operacion == 'restar':
            return restar(a,b)
        elif operacion == 'dividir':
            return dividir(a,b)
        else:
            return KeyError('Operacion no valida')

    except ZeroDivisionError:
        return 'Error: no se puede dividir por cero'
    except ValueError:
        return 'Error: Los valores deben ser numericos'
    
print (calculadora_simple('sumar', 1, 1)) #2
print (calculadora_simple('restar', 1, 1)) #0
print (calculadora_simple('dividir', 1, 1)) #1
print (calculadora_simple('dividir', 1, 0)) # Error no puede dividir x cero
print (calculadora_simple('dividir', 'R', 4)) #Error value
print(calculadora_simple('multiplicar', 4, 4)) # error key
"""

usuarios ={
    "ana":{"edad":56},
    "jose":{"edad": 49}
}
def pedirNombre():
    try:
        nombre = input ('Ingrese el nombre:') #japon
        edad = usuarios[nombre]["edad"]
        print (f'{nombre} tiene {edad} años')
    except KeyError:
        print(f'Error :  no se encontro edad de ese nombre')

try:
    edad = int(input('Ingresa tu edad: '))
    print (f'El año que viene  tendras {edad +1} años')
except ValueError:
    print ('Debes ingresar solo numeros')
