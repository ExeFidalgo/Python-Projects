import random

def guess (x):
    random_number = random.randint (1, x)
    guess = 0
    while guess != random_number:
        guess = int (input (f'Elige un numero entre 1 y {x}: '))
        if guess < random_number :
            print ('Perdon, adivina otra vez, demasiado bajo.')
        elif guess > random_number :
            print('Perdon, adivina otra vez, demasiado alto.')

    print (f'Si, felicitaciones, adivinaste el numero {random_number} correctamente')


guess(100)
