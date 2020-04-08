import random, sys, time

def crea_password():
    
    def crea(parola):
        parola = (''.join(random.choice(parola) for m in range(lunghezza)))
        print(f"\n\n        LA TUA PASSWORD E':      {parola}\n\n")

    lunghezza = int(input("\n       Inserisci la lunghezza della password (quantià di caratteri): "))
                                                                                        
    scelta = input('''

                Come vuoi la password?

                1)Solo lettere (maiuscole e minuscole)
                2)Solo numeri
                3)Alfanumerica (maiuscole/minuscole + numeri)
                4)Alfanumerica con simboli(maiuscole/minuscole + numeri + simboli(,.:;?!'"&*#@)
                

                Scelta: ''')

    if scelta == '1':
        lista = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        password_return = crea(lista)

    elif  scelta == '2':
        lista = ("0123456789")
        password_return = crea(lista)

    elif  scelta == '3':
        lista = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678901234567890123456789")
        password_return = crea(lista)

    elif  scelta == '4':
        lista = ('''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678901234567890123456789,.:;?!'"&*#@,.:;?!'"&*#@,.:;?!'"&*#@,.:;?!'"&*#@''')
        password_return = crea(lista)

    else:
        print("Ok, uscita dal programma in corso...")
        time.sleep(4)
        sys.exit(0)

    return password_return
