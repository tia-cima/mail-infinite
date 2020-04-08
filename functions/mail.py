import smtplib
import os
import sys
import time

def invio_mail():        
        def uscita():
            print("Uscita dal programma in corso...")
            time.sleep(2)
            sys.exit(0)
        

        email = smtplib.SMTP("smtp.gmail.com", 587) #SPECIFICO SERVIZIO, DOMINIO E PORTA
        email.ehlo()                                #PER CONNETTERMI AL SERVER 
        email.starttls()                            # PER STARTARE UN CANALE CRIPTATO
        
        #INSERIMENTO DELLA QUANTITA' DI MAIL DA INVIARE
        quantita = int(input("\nInserisci la quantità di mail da mandare -->" ))


        #LOGIN AL SERVIZIO
        while (True):
            try:
                user = input("\nInserisci la mail alla quale vuoi accedere (funge da mittente): ")
                password = input("Inserisci la password: ")
                email.login(user, password) 
                break      
            except:
                scelta = input("Email o password errata.\nATTENZIONE! Controlla se hai attivato la possibilità di accesso ad app meno sicure al seguente link: \nhttps://myaccount.google.com/u/6/lesssecureapps?pageId=none\n\nVuoi reinserire? Y/n: ")
                if scelta == 'Y' or scelta == 'y':
                    continue
                else:
                    uscita()

            print(f"\nVerranno inviate mail con l'account: {user}")
            mittente = user

        #INSERIMENTO DESTINATARIO 
        while(True):
            destinatario = input("\nInserisci il destinatario: ")
            scelta = input("Confermi? *assicurarsi dell'esistenza dell'indirizzo*\nY/n: ")
            if scelta == 'Y' or scelta == 'y':
                break
            else:
                continue

        #INSERIMENTO CONTENUTO          
        oggetto0 = input("\nInserisci l'oggetto della mail: ")          
        contenuto = input("Inserisci il messaggio da inviare: ")    
        print ('\n')

        #INVIO MAIL
        for n in range(1, quantita + 1):
            oggetto = (f"Subject: {oggetto0} {n}\n\n")    #per non accordare le mail
            messaggio = oggetto + contenuto

            email.sendmail(mittente, destinatario, messaggio)
            print(f"email mandate = {n}")
            
            
        #USCITA DALLA MAIL
        email.quit() 

        return n, oggetto0, contenuto
