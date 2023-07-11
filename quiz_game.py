print('¡Bienvenido a la test de español!')

playing = input('¿Quieres jugar? ').lower()

if playing != 'yes':
    quit()

print('Bien,¡Vamos a jugar!')
score = 0

answer = input('¿Cómo se dice "cat" en español? ').lower()
if answer == 'gato':
    print('¡Correcta!')
    score += 1
else:
    print('¡Incorrecta!')

answer = input('¿Cómo se dice "dog" en español? ').lower()
if answer == 'perro':
    print('¡Correcta!')
    score += 1
else:
    print('¡Incorrecta!')

answer = input('¿Cómo se dice "turtle" en español? ').lower()
if answer == 'tortuga':
    print('¡Correcta!')
    score += 1
else:
    print('¡Incorrecta!')

answer = input('¿Cómo se dice "bunny" en español? ').lower()
if answer == 'conejito':
    print('¡Correcta!')
    score += 1
else:
    print('¡Incorrecta!')

answer = input('¿Cómo se dice "deer" en español? ').lower()
if answer == 'ciervo':
    print('¡Correcta!')
    score += 1
else:
    print('¡Incorrecta!')

print('Tienes ' + str(score) + ' preguntas correctas.')    
print('Tienes ' + str((score / 5) * 100 ) + '%.')  