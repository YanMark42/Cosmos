"""
Just a simple rolling dice program written in python
"""

import random

# print(random.randint(1, 6)) stampa un numero intero random compreso tra 1 e 6

def roll():

    """
    This function rolls the dice with the setup you choose
    """

    list=[]

    if retry > 1:
        for i in range(retry):
            list.append(random.randint(1, max))
        return list

    else:
        return random.randint(1, max)


def settings():

    """
    This function sets the options for the roll
    """

    global max  # "global" serve per passare la variabile globale "max" nella funzione
                # ed è necessario per poterla modificare
    global retry

    print('Current settings roll a d'+ str (max) +' and does',retry,'throw\n')

        # '+ str () +' stampa il valore tra parentesi attaccato alla d nella stringa
        # altrimenti con un normale ',  ,' avrebbe stampato il valore con uno spazio

    a=input('Do you want to change the settings?? Enter <Y> or <N> or <D> for default\n')

    if a in ('Y','y','yes','Yes',):
        print('Leave empty to default\n')
        try:
            max=int(input('Enter the faces of the dice: '))
        except ValueError:
            pass
        try:
            retry=int(input('Enter the throws to make: '))
        except ValueError:
            pass

    elif a in ('D','d','default','Default'):
        max=6
        retry=1

    else: pass
    
    return

print('Welcome to rolling dice!\n')

max = 6
retry = 1

while True:

    print('Enter <roll> to roll a dice\nEnter <settings> to change the faces'
    ' and decide how many throws to make\nDefault is [6] faces and [1] take\n'
    'Enter <exit> to leave\n')
    a=input()
    if a == 'roll' :
        while True:

            if retry > 1:
                print('The dice rolled', retry,'times and says',roll())

            elif retry == 1:
                print('The dice says',roll())

            print('Roll again?? Enter <Y> to roll again with the same options, or <N> return to menu')
            b=input()

            if b in ('n','N','no','No'):
                break

            else:
                continue

    elif a == 'settings' :
        settings()

    elif a == 'exit' :
        break

x = input('Press <Enter> to leave \n')

if x == 'asdrubale':
    print('Just a simple code created by YanMark\n') # è solo un easter egg buttato lì

    input('Now you can leave! ;)')
