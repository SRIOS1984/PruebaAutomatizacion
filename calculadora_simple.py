#CALCULADORA CON FUNCIONES
def sumar(a, b):
    return a+b
def restar (a,b):
    return a-b
def dividir (a,b):
    return a//b #ejemplo : 2.9 =>2

def calculadora_simple(operacion , a, b):  
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
print (calculadora_simple ('dividir', 10, 5))
'''   
print (calculadora_simple('sumar', 1, 1)) #2
print (calculadora_simple('restar', 1, 1)) #0
print (calculadora_simple('dividir', 1, 1)) #1
print (calculadora_simple('dividir', 1, 0)) # Error no puede dividir x cero
print (calculadora_simple('dividir', 'R', 4)) #Error value
print(calculadora_simple('multiplicar', 4, 4)) # error key
'''
