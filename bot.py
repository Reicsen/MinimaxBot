# główny program obsługujący grę, wywołania funkcji i komunikację z serwerem

import otwarcia
import minimax
import sys
import socket

if(len(sys.argv)!=6):
    print("Podano złą ilość parametrów startowych!\n\n")
else:
    try:    
        adresSerwera = sys.argv[1]
        nrPortu = int(sys.argv[2])
        nrGracza = int(sys.argv[3])
        nazwaGracza = sys.argv[4]
        if(len(nazwaGracza)>9):
            raise NameError("Za dużo znaków")
        glebokosc = int(sys.argv[5])
        
        nrPola: int
        rzad: int
        kolumna: int
        tura: int = 1
        plansza=[]
        for i in range(25):
            plansza.append(0)
        
        polaczenie = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        polaczenie.connect((adresSerwera,nrPortu))
        
        odebrane = int(polaczenie.recv(128).decode("utf-8"))
        
        polaczenie.sendall((str(nrGracza)+" "+nazwaGracza).encode("utf-8"))
        print("Start gry")
        
        odebrane = int(polaczenie.recv(128).decode("utf-8"))
        
        while(odebrane<100 or odebrane==600):
            if(odebrane!=600):
                rzad = (odebrane//10)-1
                kolumna = (odebrane%10)-1
                plansza[5*rzad+kolumna] = -1
                tura+=1
            
            if(tura<=glebokosc):    # nie osiągnięto maksymalnej dopuszczalnej głębokości - można skorzystać z biblioteki otwarć
                nrPola=otwarcia.ruch(tura,plansza)
                if(nrPola==-1):     # brak ruchu w bibliotece - uruchomienie algorytmu minimax
                    nrPola=minimax.wyborRuchu(glebokosc,plansza)
            
            else:                                              # ilośc wykonanych łącznie przez obu graczy ruchów przekroczyła dopuszczalną głębokość
                nrPola=minimax.wyborRuchu(glebokosc,plansza)   # przeszukiwania - uruchomienie algorytmu minimax
                
            rzad=(nrPola//5)+1
            kolumna=(nrPola%5)+1
            plansza[nrPola] = 1
            tura+=1
            polaczenie.sendall((str(rzad)+str(kolumna)).encode("utf-8"))
            
            odebrane = int(polaczenie.recv(128).decode("utf-8"))
        
        if((odebrane//100) in [1,4]):
            print("Wygrana!\n\n")
        elif((odebrane//100) in [2,5]):
            print("Porażka!\n\n")
        elif((odebrane//100)==3):
            print("Remis!\n\n")
        else:
            print("Wystąpił błąd komunikacji!")
        
        polaczenie.close()
    
    except NameError as e:
        print(e)
        #print("Wystąpił błąd parsowania parametrów!")