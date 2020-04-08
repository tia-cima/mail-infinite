import os, time, sys
#CREAZIONE FILE DI TESTO PER VEDERE QUANTE MAIL SONO STATE INVIATE
def crea_file(n, oggetto0, contenuto):    
    
    def uscita():
            print("Uscita dal programma in corso...")
            time.sleep(2)
            sys.exit(0)
    
    percorso = os.getcwd()
    scelta = input("\n\nVuoi creare un file di testo in cui viene salvata la quantità di email inviate, oggetto e messaggio? Y/n: ")
    while(True):
        if scelta == 'Y' or scelta == 'y':
            try:
                nomefile = input("\nInserisci il nome del file: ")
                file1 = open(f"{nomefile}.txt", "a")
                file1.write(f"\nQuantitaìà di mail inviate:{str(n)}\nOggetto: {oggetto0}\nMessaggio: {contenuto}")
                file1.close
                print(f"\n\"{nomefile}.txt\" aperto e sovrascritto con successo al percorso <{percorso}>\n")
                os.system("pause")
                break
            except: 
                scelta = input("Qualcosa è andato storto, vuoi riprovare? Y/n: ")
                if scelta == 'Y' or scelta == 'y':
                    continue
                else:
                    uscita()
        else:
            print("\nEmail inviate con successo ma nessun file creato.\n")
            uscita()
