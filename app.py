# write 'hello world' to the console
print('hello world')

import random

opciones = ['piedra', 'papel', 'tijeras']

while True:
    eleccion_usuario = input('Elige piedra, papel o tijeras: ')
    eleccion_computadora = random.choice(opciones)

    print('La computadora eligió:', eleccion_computadora)

    if eleccion_usuario == eleccion_computadora:
        print('Es un empate')
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra'):
        print('¡Has ganado!')
    else:
        print('Has perdido')

    jugar_de_nuevo = input('¿Quieres jugar de nuevo? (s/n): ')
    if jugar_de_nuevo.lower() != 's':
        break