# Użyte w komentarzach kody liczbowe układów na planszy oznaczają pozycje wewnątrz analizowanej czwórki/trójki pól;
# np. dla czwórki układ 1 4 oznacza sytuację X - - X (lub O - - O) w rozpatrywanym rzędzie, kolumnie, przekątnej lub przyprzekątnej

# Przeciwprzekątną nazywana jest ukośna linia pól długości 4 lub 3, "równoległa" do jednej z przekątnych planszy; np. pola (1,3), (2,2), (3,1)
# są jedną z przyprzekątnych 3-elementowych


# funkcja oceny heurystycznej wykorzystywana przez algorytm minimax;
# wykorzystuje dwie składowe funkcje fH1 i fH2 - są one wyliczane dla obu graczy, a następnie od wartości dla gracza wywołującego algorytm minimax (1)
# odejmowana jest wartość dla jego rywala (-1);
# funkcja fH1 jest systemem nagród i kar za linie, na których dany gracz może teoretycznie ustawić minimum 4 pionki (wynik może być zarówno dodatni,
# jak i ujemny), zaś fH2 jest systemem kar za linie, na których dany gracz jest zagrożony ustawieniem przegrywającej trójki (wynik zawsze jest niedodatni,
# zaś wynik rywala zawsze jest niedodatni)
def fHeurystyczna(plansza) -> int:
    return fH1(plansza,1)-fH1(plansza,-1)+fH2(plansza,1)-fH2(plansza,-1)


# pierwsza składowa funkcja oceny heurystycznej planszy;
# funkcja bada rzędy, kolumny, przekątne i czteroelementowe przyprzekątne w poszukiwaniu obszarów, na których dany gracz teoretycznie mógłby
# stworzyć czwórkę (a zatem szuka czterech lub pięciu pól z rzędu, na której albo stoi pionek danego gracza, albo jest ono puste);
# za każdą taką znalezioną linię funkcja dodaje +1 do wyniku (oprócz sytuacji 1 3 5 lub 2 3 na czteroelementowej przyprzekątnej, która nie daje
# możliwości ułożenia czwórki), a ponadto ocenia układ na obszarze tej linii zgodnie z systemem nagród i kar, których wartości wyrażone są przy
# użyciu zmiennych:
# a0 = 10 - nagroda za układy, które wymagają jednego ruchu do wygrania, a ponadto rywal nie może ich sprowadzić do ryzyka trójki (czyli 1 2 4 5, typu
#       1 2 4 lub typu 1 3 4 przy polu 5 zajętym przez rywala); zarazem kara za układ 1 3 5, niedający możliwości ułożenia czwórki, ale dającego podwójne ryzyko trójki
# a1 = 5 - nagroda za układ typu 1 3 4 przy wolnym polu 5 (istnieje ryzyko sprowadzenia go do ryzyka trójki)
# b = 4 - kara za układ typu 1 2 5 (ryzyko sprowadzenia do ryzyka trójki, a zarazem do wygranej potrzeba aż 2 ruchów)
# c = 3 - nagroda za układ 1 4
# d = 1 - kara za układ 1 3 na czteroelementowej przyprzekątnej lub za układ 2 4 na linii pięcioelementowej w przypadku, gdy któreś z pól skrajnych
#           jest zajęte przez rywala
# e = 1 - nagroda za układ 2 4 na linii pięcioelementowej w przypadku, gdy oba pola skrajne są wolne
# f = 3 - kara za układ 1 3 na linii pięcioelementowej
# g = 4 - kara za układ 1 5
# h = 2 - kara za dwa pionki pod rząd na linii pięcioelementowej
# k = 1 - kara w przypadku, gdy jedynym pionkiem na linii pięcioelementowej jest pole środkowe
# l = 1 - nagroda za pionek na linii pięcioelementowej na polu innym niż środkowe
# m = 5 - kara za posiadanie dwóch pionków na dwóch środkowych polach czteroelementowej przyprzekątnej (tworzy jedynie ryzyka trójek, ale uniemożliwia
#           stworzenie czwórki)
# n = 2 - kara za posiadanie dwóch pionków pod rząd na skrajnych polach czteroelementowej przyprzekątnej
# o = 1 - nagroda za pojedynczy pionek na którymś z pól skrajnych czteroelementowej przyprzekątnej
def fH1(plansza, nr: int) -> int:   # zlicza ilość linii, w których dany gracz ma szansę na ułożenie czwórki i przyznaje bonusy a niektóre układy
                                    # (zwłaszcza typu „1 2 4") i kary za układy niosące ryzyko zaowocowania zmuszeniem przez rywala do ułożenia trójki
    wynik = 0
    baza=1
    a0=10
    a1=5
    b=4
    c=3
    d=1
    e=1
    f=3
    g=4
    h=2
    k=1
    l=1
    m=5
    n=2
    o=1
    
    # rzędy i kolumny
    for i in range(5):               
        #rzędy gracza
        if((plansza[5*i+1]!=-nr and plansza[5*i+2]!=-nr and plansza[5*i+3]!=-nr) and (plansza[5*i]!=-nr or plansza[5*i+4]!=-nr)):
            wynik+=baza
            ile=0
            for j in range(5):
                if(plansza[5*i+j]==nr):
                    ile+=1
            
            if(ile==4):     # jedyną opcją niekończącą gry poprzez trójkę lub czwórkę jest 1 2 4 5
                wynik+=a0
                
            
            if(ile==3):
                if((plansza[5*i]==nr and plansza[5*i+3]==nr) and plansza[5*i+1]==nr):
                    wynik+=a0
                elif((plansza[5*i]==nr and plansza[5*i+3]==nr) and plansza[5*i+2]==nr):
                    if(plansza[5*i+4]==-nr):
                        wynik+=a0
                    else:
                        wynik+=a1
                elif((plansza[5*i+4]==nr and plansza[5*i+1]==nr) and plansza[5*i+3]==nr):
                    wynik+=a0
                elif((plansza[5*i+4]==nr and plansza[5*i+1]==nr) and plansza[5*i+2]==nr):
                    if(plansza[5*i]==-nr):
                        wynik+=a0
                    else:
                        wynik+=a1
                    
                elif(plansza[5*i]==nr and plansza[5*i+4]==nr and (plansza[5*i+1]==nr or plansza[5*i+3]==nr)):
                    wynik-=b
                elif(plansza[5*i]==nr and plansza[5*i+2]==nr and plansza[5*i+4]==nr):   # dla 1 3 5 nie można ułożyć czwórki, ale za to są dwa ryzyka trójki
                    wynik-=baza
                    wynik-=a0
            
            if(ile==2):
                if((plansza[5*i]==nr and plansza[5*i+3]==nr) or (plansza[5*i+1]==nr and plansza[5*i+4]==nr)):
                    wynik+=c
            
                elif(plansza[5*i+1]==nr and plansza[5*i+3]==nr):
                    if(plansza[5*i]==-nr or plansza[5*i+4]==-nr):   # pionek rywala na 5*i+2 niemożliwy, bo wtedy nie ma opcji stworzenia czwórki,
                        wynik-=d                                    # więc cały zewnętrzny if nie zostanie uruchomiony
                    else:
                        wynik+=e
      
                elif(plansza[5*i+2]==nr and (plansza[5*i]==nr or plansza[5*i+4]==nr)):
                    wynik-=f
                elif(plansza[5*i]==nr and plansza[5*i+4]==nr):
                    wynik-=g
                
                else:           # dwa pod rząd
                    wynik-=h
            
            if(ile==1):
                if(plansza[5*i+2]==nr):
                    wynik-=k
                else:
                    wynik+=l
        
        #kolumny gracza
        if((plansza[5+i]!=-nr and plansza[10+i]!=-nr and plansza[15+i]!=-nr) and (plansza[i]!=-nr or plansza[20+i]!=-nr)):
            wynik+=baza
            ile=0
            for j in range(5):
                if(plansza[5*j+i]==nr):
                    ile+=1
            
            if(ile==4):     # jedyną opcją niekończącą gry poprzez trójkę lub czwórkę jest 1 2 4 5
                wynik+=a0
                
            
            if(ile==3):
                if((plansza[i]==nr and plansza[15+i]==nr) and plansza[5+i]==nr ):
                    wynik+=a0
                elif((plansza[i]==nr and plansza[15+i]==nr) and plansza[10+i]==nr):
                    if(plansza[20+i]==-nr):
                        wynik+=a0
                    else:
                        wynik+=a1
                elif((plansza[20+i]==nr and plansza[5+i]==nr) and plansza[15+i]==nr):
                    wynik+=a0
                elif((plansza[20+i]==nr and plansza[5+i]==nr) and plansza[10+i]==nr):
                    if(plansza[i]==-nr):
                        wynik+=a0
                    else:
                        wynik+=a1
                    
                elif(plansza[i]==nr and plansza[20+i]==nr and (plansza[5+i]==nr or plansza[15+i]==nr)):
                    wynik-=b
                elif(plansza[i]==nr and plansza[10+i]==nr and plansza[20+i]==nr):    # dla 1 3 5 nie można ułożyć czwórki, ale za to są dwa ryzyka trójki
                    wynik-=baza
                    wynik-=a0
            
            if(ile==2):
                if((plansza[i]==nr and plansza[15+i]==nr) or (plansza[5+i]==nr and plansza[20+i]==nr)):
                    wynik+=c
            
                elif(plansza[5+i]==nr and plansza[15+i]==nr):
                    if(plansza[i]==-nr or plansza[20+i]==-nr):
                        wynik-=d
                    else:
                        wynik+=e
      
                elif(plansza[10+i]==nr and (plansza[i]==nr or plansza[20+i]==nr)):
                    wynik-=f
                elif(plansza[i]==nr and plansza[20+i]==nr):
                    wynik-=g
                
                else:           # dwa pod rząd
                    wynik-=h
            
            if(ile==1):
                if(plansza[10+i]==nr):
                    wynik-=k
                else:
                    wynik+=l
    
    
    #przekątna \ gracza
    if((plansza[6]!=-nr and plansza[12]!=-nr and plansza[18]!=-nr) and (plansza[0]!=-nr or plansza[24]!=-nr)):
        wynik+=baza
        ile=0
        for j in range(5):
            if(plansza[6*j]==nr):
                ile+=1
            
        if(ile==4):     # jedyną opcją niekończącą gry poprzez trójkę lub czwórkę jest 1 2 4 5
            wynik+=a0
                
            
        if(ile==3):
            if((plansza[0]==nr and plansza[18]==nr) and plansza[6]==nr):
                wynik+=a0
            elif((plansza[0]==nr and plansza[18]==nr) and plansza[12]==nr):
                if(plansza[24]==-nr):
                    wynik+=a0
                else:
                    wynik+=a1
            elif((plansza[24]==nr and plansza[6]==nr) and plansza[18]==nr):
                wynik+=a0
            elif((plansza[24]==nr and plansza[6]==nr) and plansza[12]==nr):
                if(plansza[0]==-nr):
                    wynik+=a0
                else:
                    wynik+=a1
                    
            elif(plansza[0]==nr and plansza[24]==nr and (plansza[6]==nr or plansza[18]==nr)):
                wynik-=b
            elif(plansza[0]==nr and plansza[12]==nr and plansza[24]==nr):    # dla 1 3 5 nie można ułożyć czwórki, ale za to są dwa ryzyka trójki
                wynik-=baza
                wynik-=a0
            
        if(ile==2):
            if((plansza[0]==nr and plansza[18]==nr) or (plansza[6]==nr and plansza[24]==nr)):
                wynik+=c
            
            elif(plansza[6]==nr and plansza[18]==nr):
                if(plansza[0]==-nr or plansza[24]==-nr):
                    wynik-=d
                else:
                    wynik+=e
      
            elif(plansza[12]==nr and (plansza[0]==nr or plansza[24]==nr)):
                wynik-=f
            elif(plansza[0]==nr and plansza[24]==nr):
                wynik-=g
                
            else:           # dwa pod rząd
                wynik-=h
            
        if(ile==1):
            if(plansza[12]==nr):
                wynik-=k
            else:
                wynik+=l
    
    
    #przekątna / gracza
    if((plansza[8]!=-nr and plansza[12]!=-nr and plansza[16]!=-nr) and (plansza[4]!=-nr or plansza[20]!=-nr)):
        wynik+=baza
        ile=0
        for j in range(5):
            if(plansza[4*(j+1)]==nr):
                ile+=1
            
        if(ile==4):     # jedyną opcją niekończącą gry poprzez trójkę lub czwórkę jest 1 2 4 5
            wynik+=a0
                
            
        if(ile==3):
            if((plansza[4]==nr and plansza[16]==nr) and plansza[8]==nr):
                wynik+=a0
            elif((plansza[4]==nr and plansza[16]==nr) and plansza[12]==nr):
                if(plansza[20]==-nr):
                    wynik+=a0
                else:
                    wynik+=a1
            elif((plansza[20]==nr and plansza[8]==nr) and plansza[16]==nr):
                wynik+=a0
            elif((plansza[20]==nr and plansza[8]==nr) and plansza[12]==nr):
                if(plansza[4]==-nr):
                    wynik+=a0
                else:
                    wynik+=a1
                    
            elif(plansza[4]==nr and plansza[20]==nr and (plansza[8]==nr or plansza[16]==nr)):
                wynik-=b
            elif(plansza[4]==nr and plansza[12]==nr and plansza[20]==nr):    # dla 1 3 5 nie można ułożyć czwórki, ale za to są dwa ryzyka trójki
                wynik-=baza
                wynik-=a0
            
        if(ile==2):
            if((plansza[4]==nr and plansza[16]==nr) or (plansza[8]==nr and plansza[20]==nr)):
                wynik+=c
            
            elif(plansza[8]==nr and plansza[16]==nr):
                if(plansza[4]==-nr or plansza[20]==-nr):
                    wynik-=d
                else:
                    wynik+=e
      
            elif(plansza[12]==nr and (plansza[4]==nr or plansza[20]==nr)):
                wynik-=f
            elif(plansza[4]==nr and plansza[20]==nr):
                wynik-=g
                
            else:           # dwa pod rząd
                wynik-=h
            
        if(ile==1):
            if(plansza[12]==nr):
                wynik-=k
            else:
                wynik+=l
    
    
    
    #4-elementowe "przyprzekątne" gracza
    if(plansza[1]!=-nr and plansza[7]!=-nr and plansza[13]!=-nr and plansza[19]!=-nr):
        wynik+=baza
        
        ile=0
        for i in range(4):
            if(plansza[6*i+1]==nr):
                ile+=1
                
        if(ile==3):     # tylko 1 2 4 lub 1 3 4, bo wygrana/porażka byłaby wychwycona wcześniej
            wynik+=a0
        
        if(ile==2):
            if(plansza[1]==nr and plansza[19]==nr):
                wynik+=c
        
            elif((plansza[1]==nr and plansza[13]==nr) or (plansza[7]==nr and plansza[19]==nr)):
                wynik-=d
            
            elif(plansza[7]==nr and plansza[13]==nr):
                wynik-=baza
                wynik-=m
            
            else:
                wynik-=n
        
        if(ile==1):
            if(plansza[1]==nr or plansza[19]==nr):
                wynik+=o
                
    
    
    if(plansza[5]!=-nr and plansza[11]!=-nr and plansza[17]!=-nr and plansza[23]!=-nr):
        wynik+=baza
        
        ile=0
        for i in range(4):
            if(plansza[6*i+5]==nr):
                ile+=1
                
        if(ile==3):     # tylko 1 2 4 lub 1 3 4, bo wygrana/porażka byłaby wychwycona wcześniej
            wynik+=a0
        
        if(ile==2):
            if(plansza[5]==nr and plansza[23]==nr):
                wynik+=c
        
            elif((plansza[5]==nr and plansza[17]==nr) or (plansza[11]==nr and plansza[23]==nr)):
                wynik-=d
            
            elif(plansza[11]==nr and plansza[17]==nr):
                wynik-=baza
                wynik-=m
            
            else:
                wynik-=n
        
        if(ile==1):
            if(plansza[5]==nr or plansza[23]==nr):
                wynik+=o
    
    if(plansza[3]!=-nr and plansza[7]!=-nr and plansza[11]!=-nr and plansza[15]!=-nr):
        wynik+=baza
        
        ile=0
        for i in range(4):
            if(plansza[4*i+3]==nr):
                ile+=1
                
        if(ile==3):     # tylko 1 2 4 lub 1 3 4, bo wygrana/porażka byłaby wychwycona wcześniej
            wynik+=a0
        
        if(ile==2):
            if(plansza[3]==nr and plansza[15]==nr):
                wynik+=c
        
            elif((plansza[3]==nr and plansza[11]==nr) or (plansza[7]==nr and plansza[15]==nr)):
                wynik-=d
            
            elif(plansza[7]==nr and plansza[11]==nr):
                wynik-=baza
                wynik-=m
            
            else:
                wynik-=n
        
        if(ile==1):
            if(plansza[3]==nr or plansza[15]==nr):
                wynik+=o
    
    if(plansza[9]!=-nr and plansza[13]!=-nr and plansza[17]!=-nr and plansza[21]!=-nr):
        wynik+=baza
        
        ile=0
        for i in range(4):
            if(plansza[4*i+9]==nr):
                ile+=1
                
        if(ile==3):     # tylko 1 2 4 lub 1 3 4, bo wygrana/porażka byłaby wychwycona wcześniej
            wynik+=a0
        
        if(ile==2):
            if(plansza[9]==nr and plansza[21]==nr):
                wynik+=c
        
            elif((plansza[9]==nr and plansza[17]==nr) or (plansza[13]==nr and plansza[21]==nr)):
                wynik-=d
            
            elif(plansza[13]==nr and plansza[17]==nr):
                wynik-=baza
                wynik-=m
            
            else:
                wynik-=n
        
        if(ile==1):
            if(plansza[9]==nr or plansza[21]==nr):
                wynik+=o
    
    return wynik





# druga składowa funkcja oceny heurystycznej planszy;
# funkcja bada rzędy, kolumny, przekątne oraz cztero- i trzyelementowe przyprzekątne w poszukiwaniu obszarów, na których dany gracz ma ryzyko
# stworzenia czwórki (a zatem szuka trzech, lecz nie więcej, pól z rzędu, na której albo stoi pionek danego gracza, albo jest ono puste);
# za każdą taką znalezioną linię funkcja odejmuje 1 od wyniku, a ponadto ocenia układ na obszarze tej linii zgodnie z systemem kar,
# których wartości wyrażone są przy użyciu zmiennych:
# a = 4 - kara za posiadanie na obszarze takiej "trójki" pól dwóch pionków
# b = 1 - kara za posiadanie na obszarze takiej "trójki" pól jednego pionka
def fH2(plansza, nr: int) -> int:
    wynik = 0
    baza = 1
    a=4
    b=1
    
    
    #rzędy i kolumny
    for i in range(5):
        #rzędy gracza
        if(plansza[5*i]!=-nr and plansza[5*i+1]!=-nr and plansza[5*i+2]!=-nr and plansza[5*i+3]==-nr):
            wynik-=baza
            ile=0
            for j in range(3):
                if(plansza[5*i+j]==nr):
                    ile+=1
            
            if(ile==2):
                wynik-=a
            elif(ile==1):
                wynik-=b
        
        if(plansza[5*i+2]!=-nr and plansza[5*i+3]!=-nr and plansza[5*i+4]!=-nr and plansza[5*i+1]==-nr):
            wynik-=baza
            ile=0
            for j in range(3):
                if(plansza[5*i+j+2]==nr):
                    ile+=1
            
            if(ile==2):
                wynik-=a
            elif(ile==1):
                wynik-=b
            
        if(plansza[5*i+1]!=-nr and plansza[5*i+2]!=-nr and plansza[5*i+3]!=-nr and plansza[5*i]==-nr and plansza[5*i+4]==-nr):
            wynik-=baza
            ile=0
            for j in range(3):
                if(plansza[5*i+j+1]==nr):
                    ile+=1
            
            if(ile==2):
                wynik-=a
            elif(ile==1):
                wynik-=b
        
        
        #kolumny gracza
        if(plansza[i]!=-nr and plansza[5+i]!=-nr and plansza[10+i]!=-nr and plansza[15+i]==-nr):
            wynik-=baza
            ile=0
            for j in range(3):
                if(plansza[5*j+i]==nr):
                    ile+=1
            
            if(ile==2):
                wynik-=a
            elif(ile==1):
                wynik-=b
        
        if(plansza[10+i]!=-nr and plansza[15+i]!=-nr and plansza[20+i]!=-nr and plansza[5+i]==-nr):
            wynik-=baza
            ile=0
            for j in range(3):
                if(plansza[5*(j+2)+i]==nr):
                    ile+=1
            
            if(ile==2):
                wynik-=a
            elif(ile==1):
                wynik-=b
            
        if(plansza[5+i]!=-nr and plansza[10+i]!=-nr and plansza[15+i]!=-nr and plansza[i]==-nr and plansza[20+i]==-nr):
            wynik-=baza
            ile=0
            for j in range(3):
                if(plansza[5*(j+1)+i]==nr):
                    ile+=1
            
            if(ile==2):
                wynik-=a
            elif(ile==1):
                wynik-=b
    
    
    
    #przekątna \ gracza
    if(plansza[0]!=-nr and plansza[6]!=-nr and plansza[12]!=-nr and plansza[18]==-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[6*j]==nr):
                ile+=1
            
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
        
    if(plansza[12]!=-nr and plansza[18]!=-nr and plansza[24]!=-nr and plansza[6]==-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[6*(j+2)]==nr):
                ile+=1
            
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
        
    if(plansza[6]!=-nr and plansza[12]!=-nr and plansza[18]!=-nr and plansza[0]==-nr and plansza[24]==-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[6*(j+1)]==nr):
                ile+=1
            
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
    
    #przekątna / gracza
    if(plansza[4]!=-nr and plansza[8]!=-nr and plansza[12]!=-nr and plansza[16]==-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[4*j+4]==nr):
                ile+=1
            
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
        
    if(plansza[12]!=-nr and plansza[16]!=-nr and plansza[20]!=-nr and plansza[8]==-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[4*(j+2)+4]==nr):
                ile+=1
            
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
        
    if(plansza[8]!=-nr and plansza[12]!=-nr and plansza[16]!=-nr and plansza[4]==-nr and plansza[20]==-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[4*(j+1)+4]==nr):
                ile+=1
            
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
    
    
    
    #4-elementowe "przyprzekątne" gracza
    if(plansza[7]!=-nr and plansza[13]!=-nr and ((plansza[1]==-nr and plansza[19]!=-nr) or (plansza[1]!=-nr and plansza[19]==-nr))):
        wynik-=baza
        ile=0
        for j in range(4):
            if(plansza[6*j+1]==nr):
                ile+=1
        
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
            
    
    if(plansza[11]!=-nr and plansza[17]!=-nr and ((plansza[5]==-nr and plansza[23]!=-nr) or (plansza[5]!=-nr and plansza[23]==-nr))):
        wynik-=baza
        ile=0
        for j in range(4):
            if(plansza[6*j+5]==nr):
                ile+=1
        
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
    
    if(plansza[7]!=-nr and plansza[11]!=-nr and ((plansza[3]==-nr and plansza[15]!=-nr) or (plansza[3]!=-nr and plansza[15]==-nr))):
        wynik-=baza
        ile=0
        for j in range(4):
            if(plansza[4*j+3]==nr):
                ile+=1
        
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
    
    if(plansza[13]!=-nr and plansza[17]!=-nr and ((plansza[9]==-nr and plansza[21]!=-nr) or (plansza[9]!=-nr and plansza[21]==-nr))):
        wynik-=baza
        ile=0
        for j in range(4):
            if(plansza[4*j+9]==nr):
                ile+=1
        
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
    
    
    
    #3-elementowe "przyprzekątne" gracza
    if(plansza[2]!=-nr and plansza[8]!=-nr and plansza[14]!=-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[6*j+2]==nr):
                ile+=1
        
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
    
    if(plansza[2]!=-nr and plansza[6]!=-nr and plansza[10]!=-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[4*j+2]==nr):
                ile+=1
        
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
                
    if(plansza[10]!=-nr and plansza[16]!=-nr and plansza[22]!=-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[6*j+10]==nr):
                ile+=1
        
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
    
    if(plansza[14]!=-nr and plansza[18]!=-nr and plansza[22]!=-nr):
        wynik-=baza
        ile=0
        for j in range(3):
            if(plansza[4*j+14]==nr):
                ile+=1
        
        if(ile==2):
            wynik-=a
        elif(ile==1):
            wynik-=b
    

    return wynik
    




