import smtplib
import os
import sys
import time
sys.path.insert(4, 'functions/')
from random_mail import random_mail, random_password, accedi_random
from password import crea_password
from creazione_file import crea_file
from mail import invio_mail
from ascii_art import ascii_art 


if __name__ == "__main__":

    while(True):
        scelta = input(f'''
                                            
                                            
                                            
                                            
                                                        {ascii_art()}

                            1)CREA UNA MAIL E PASSWORD CASUALE E UN ACCOUNT ASSOCIATO
                            2)GENERA UNA PASSWORD SCEGLIENDO LUNGHEZZA E TIPOLOGIA
                            3)ACCEDI AD UN ACCOUNT E INVIA MAIL (ANCHE INFINITE)


                            Scelta:    ''')

    
        if scelta == '1':        
            print (f'''
                        LA MAIL CASUALE SARA': {random_mail()}
                        
                        LA PASSWORD CASUALE E': {random_password()}

                        SARAI INDIRIZZATO ALLA PAGINA DI ACCESSO DI GOOGLE''')
            time.sleep(2)
            accedi_random()

        elif scelta == '2':
            lista = crea_password()
                   
        
        elif scelta == '3':    
            n, oggetto0, contenuto = invio_mail()    
            crea_file(n, oggetto0, contenuto)        
            
    
        scelta = input('''                                                                       
                                                                            
        █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
        ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
                                                                            
                Vuoi effettuare altre operazioni? Y/n: ''') 
        if scelta == 'y' or scelta == 'Y':
            continue
        else:
            break
        
