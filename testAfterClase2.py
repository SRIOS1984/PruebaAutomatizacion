
# EJERCICIO IMPRIMIR EDAD Y PROFESION
"""
nombre = input('Ingrese nombre:')
edad = int(input('Ingrese edad: '))
profesion = input('Ingrese profesion:')
#print(nombre, edad, profesion)
"""
"""
for i in range(1,11):
    print(i)
"""
nombre = ''
while True:
    if not nombre:
        nombre = input ('Ingrese nombre: ').strip() #estafuncioneliminaEspacios
        if not 2<= len(nombre) <= 10:
            print('Ingrese un nombre valido')
            continue
        if not nombre.isalpha():
            print('Ingrese solo letras')
            continue

    edad = input('Ingrese edad: ')
    if not edad.isdigit():
        print('Ingrese solo numeros')
        continue

    profesion = input('Ingrese profesion:').strip()
    if not profesion:
        print('Ingrese profesion valida')
        continue
    if not profesion.isalpha():
        print('Ingrese solo letras')
        continue

    break

print(f'Tus datos son : Nombre: {nombre}, Edad: {edad}, Profesion: {profesion}')