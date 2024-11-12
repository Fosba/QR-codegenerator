import os
import time
import sys
import qrcode
from PIL import Image
from colorama import Fore, Back, Style

qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)

# funzioni per scrittura 
def typingPrint(text, delay: float = 0.0005):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)

    
def typingPrint(text):
     for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)

# dizionari con valori 
credenziali = [
    {
        "username": "nikommok",
        "password": "123"
    },
    {
        "username": "ciao",
        "password": "222"
    }
]
monumenti = [
    {
        "nomemonumento": "Cava Bomba",
        "link": 'https://www.museocavabomba.it/',
    },
    {
        "nomemonumento": "Buso dei briganti",
        "link": 'https://www.collieuganei.it/parchi-aree-naturalistiche/busa-dei-briganti/',
    },
    {
        "nomemonumento": "Villa Beatrice d'Este",
        "link": 'https://www.collieuganei.it/ville/villa-beatrice-este/',

    },
    {
        "nomemonumento": "impostazioni",
        "link": ''
    }
]
lista_colori = [
    {
        "nome": 'rosso',
        "colore": Fore.RED,
        "nome_inglese": "red"
    },
    {
        "nome": 'blu',
        "colore": Fore.BLUE,
        "nome_inglese": "blue"
    },
    {
        "nome": 'giallo',
        "colore": Fore.YELLOW,
        "nome_inglese": "yellow"
    },
    {
        "nome": 'verde',
        "colore": Fore.GREEN,
        "nome_inglese": "green"
    },
    {
        "nome": 'magenta',
        "colore": Fore.MAGENTA,
        "nome_inglese": "magenta"
    },
    {
        "nome": 'bianco',
        "colore": Style.RESET_ALL,
        "nome_inglese": "black"
    },
    {
        "nome": 'exit',
        "colore": Style.RESET_ALL,
        "nome_inglese": "black"
    }
]

uscita = 0  # varibili per i cicli
KEY_USCITA = 1829
KEY_PANNELLO_ADMIN = 23
COLORE_IN_USO = Style.RESET_ALL
typingPrint('''██████╗░███████╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗██╗░░░██╗████████╗░█████╗░██╗
██╔══██╗██╔════╝████╗░██║██║░░░██║██╔════╝████╗░██║██║░░░██║╚══██╔══╝██╔══██╗██║
██████╦╝█████╗░░██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║██║░░░██║░░░██║░░░██║░░██║██║
██╔══██╗██╔══╝░░██║╚████║░╚████╔╝░██╔══╝░░██║╚████║██║░░░██║░░░██║░░░██║░░██║╚═╝
██████╦╝███████╗██║░╚███║░░╚██╔╝░░███████╗██║░╚███║╚██████╔╝░░░██║░░░╚█████╔╝██╗
╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝\n ''')
time.sleep(1)
colore = 7
os.system('cls')
while uscita != KEY_USCITA:
    os.system('cls')
    print(COLORE_IN_USO + "Benvenuto nel programma di creazione qrcode")
    time.sleep(2)
    errore = 1
    pannello_admin = 0
    os.system('cls')
    typingPrint("Di seguito elencati i luoghi per i quali è disponibile la creazione del qrcode\n")
    
    for mon in monumenti:
        typingPrint("[" + f"{monumenti.index(mon)}" + "] " + f"{mon['nomemonumento']}\n\n")
    while True:
        scelta = input("inserire il numero qui di seguito--> ")
        if scelta.isdigit():
            scelta = int(scelta)
            break
        else:
            print("Inserire un numero valido.")    
    if scelta == KEY_USCITA:
        uscita = KEY_USCITA

    elif scelta == 3:  # impostazioni per cambio colore
        print("impostazioni per la regolazione del colore valida per le scritte e per il qrcode")
        time.sleep(1)
        
        for color in lista_colori:
            print(
                Style.RESET_ALL + "[" + f"{lista_colori.index(color)}" + "] " + f" {color['colore']} {color['nome']}\n")
            
        while True:
            colore_input = input("Inserire il numero corrispondente al colore del testo e del qrcode: ")
        
            if colore_input.isdigit():
                colore = int(colore_input)
                break     
            else:
                print("Inserire un numero valido.")           
        if colore >= len(lista_colori) or colore == 6:
            print("Colore non valido. Si prega di selezionare un colore corretto dalla lista.")
        else:
            print(f"{lista_colori[colore]['colore']} {lista_colori[colore]['nome']}" + " è il colore scelto")
            COLORE_IN_USO = lista_colori[colore]['colore']
            time.sleep(1)
    elif scelta == KEY_PANNELLO_ADMIN:  # admin panel
        print("entrando nelle impostazioni admin\n")
        time.sleep(1)

        while errore == 1:
            errore = 0

            username = input("Inserisci username: ").strip() 
            password = input("Inserisci password: ").strip()

            credenziali_valide = False
            for credenziale in credenziali:
                if username == credenziale["username"] and password == credenziale["password"]:
                    credenziali_valide = True

            if credenziali_valide:
                print("Credenziali valide")
                print("accesso in corso...")
            elif not credenziali_valide:
                print("Credenziali non valide")
                print("riprovare...")
                errore = 1

        while (pannello_admin != 7) and (uscita != KEY_USCITA) and (scelta > 3 and scelta >= 0):
            for i in monumenti:
                print("[" + f"{monumenti.index(i)}" + "] " + f"{i['nomemonumento']}\n")
                print(f"{i['link']}\n")
            while True:
                scelta = input("Inserire il numero indice per cambiare il link-->  per uscire dalla console admin premere 7 ")
                if scelta.isdigit():
                    scelta = int(scelta)
                    break
                else:
                    print("Inserire un numero valido.")   
            
            if scelta == KEY_USCITA:  # spegnimento programma da impostazioni admin
                uscita = KEY_USCITA
                break
            elif scelta == 7:
                pannello_admin = 7
                print("uscendo dalle impostazioni admin...")
                time.sleep(1)
            elif scelta < 3:
                print(f"{monumenti[scelta]['nomemonumento']} è il monumento scelto per cambiare il link\n")
                nuovo_link = input("Inserire il nuovo link da mettere nel dictionary: ")
                monumenti[scelta]['link'] = nuovo_link

    if len(monumenti)-1 > scelta >= 0:  # creazione qrcode con colore modificato o di base
        if colore == 7:
            colore = 5
        qr.add_data(monumenti[scelta]['link'])
        colore_qrcode = lista_colori[colore]['nome_inglese']
        try:
            img = qr.make_image(fill_color=colore_qrcode, back_color='white').save(monumenti[scelta]['nomemonumento']+"_qrcode.png")
            Image.open((monumenti[scelta]['nomemonumento'])+"_qrcode.png").show()
            os.remove((monumenti[scelta]['nomemonumento'])+"_qrcode.png")
        except KeyError:
            print("Colore non valido. Si prega di selezionare un colore corretto dalla lista.")





