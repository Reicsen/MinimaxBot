# plik zawiera bibliotekę otwarć - są one określone do głębokości 3 oraz dla głębokości 4 w sytuacji, gdy ruchy rywala umożliwiają zajęcie skrajnych
# pól którejś z czteroelementowych przyprzekątnych planszy

# funkcja zamieniająca numer pola z notacji planszowej na indeks w tablicy
def nrPola(rzad,kol):
    return 5*(rzad-1)+(kol-1)


# funkcja zwracająca ruch z biblioteki lub infromację -1 oznaczającą uruchomienie algorytmu minimax
def ruch(tura: int, plansza) -> int:
    if(tura==1):
        return nrPola(4,1)

    
    if(tura==2):
        ########### najpierw blokowanie przyprzekątnych
        if(plansza[nrPola(1,2)]==-1):
            return nrPola(4,5)
        if(plansza[nrPola(1,4)]==-1):
            return nrPola(4,1)
        if(plansza[nrPola(2,1)]==-1):
            return nrPola(5,4)
        if(plansza[nrPola(2,5)]==-1):
            return nrPola(5,2)
        if(plansza[nrPola(4,1)]==-1):
            return nrPola(1,4)
        if(plansza[nrPola(4,5)]==-1):
            return nrPola(1,2)
        if(plansza[nrPola(5,2)]==-1):
            return nrPola(2,5)
        if(plansza[nrPola(5,4)]==-1):
            return nrPola(2,1)
        ###############################################
        ## jeśli na żadnej nic nie stoi, postawienie samemu na krańcu jednej, przy okazji blokując jedną z możliwych linii czwórek rywala,
        ## najlepiej sprowadzając ją do ryzyka trójki
        
        if(-1 in [plansza[nrPola(1,3)],plansza[nrPola(1,5)]]):
            return nrPola(1,2)
        if(-1 in []):
            return nrPola(1,4)
        if(-1 in [plansza[nrPola(5,1)],plansza[nrPola(2,2)]]):
            return nrPola(2,1)
        if(-1 in [plansza[nrPola(2,3)],plansza[nrPola(5,5)],plansza[nrPola(2,4)]]):
            return nrPola(2,5)
        if(-1 in [plansza[nrPola(1,1)],plansza[nrPola(3,1)],plansza[nrPola(3,3)],plansza[nrPola(4,2)]]):
            return nrPola(4,1)
        if(-1 in [plansza[nrPola(3,5)],plansza[nrPola(4,3)],plansza[nrPola(4,4)]]):
            return nrPola(4,5)
        if(-1 in [plansza[nrPola(3,2)],plansza[nrPola(5,3)]]):
            return nrPola(5,2)
        if(-1 in [plansza[nrPola(3,4)]]):
            return nrPola(5,4)
    
    
    
    
    if(tura==3):                            # jeżeli nie zablokowano przyprzekątnej (1,4), (2,3), (3,2), (4,1), zajęcie jej drugiego końca
        if((-1) not in [plansza[nrPola(1,4)],plansza[nrPola(2,3)],plansza[nrPola(3,2)]]):
            return nrPola(1,4)
        elif(plansza[nrPola(1,4)]==-1):     # w przeciwnym razie, ruchy wyznaczone testowo przez bota z dużą głębokością
            return nrPola(2,1)
        elif(plansza[nrPola(2,3)]==-1):
            return nrPola(4,4)
        elif(plansza[nrPola(3,2)]==-1):
            return nrPola(4,4)
    
    
    if(tura==4):    # jeśli w swoim pierwszym ruchu zajęto koniec którejś 4-elementowej przyprzekątnej i jej drugi koniec jest wolny, zajęcie go
        if(plansza[nrPola(1,2)]==1 and plansza[nrPola(4,5)]==0):
            return nrPola(4,5)
        if(plansza[nrPola(1,4)]==1 and plansza[nrPola(4,1)]==0):
            return nrPola(4,1)
        if(plansza[nrPola(2,1)]==1 and plansza[nrPola(5,4)]==0):
            return nrPola(5,4)
        if(plansza[nrPola(2,5)]==1 and plansza[nrPola(5,2)]==0):
            return nrPola(5,2)
        if(plansza[nrPola(4,1)]==1 and plansza[nrPola(1,4)]==0):
            return nrPola(1,4)
        if(plansza[nrPola(4,5)]==1 and plansza[nrPola(1,2)]==0):
            return nrPola(1,2)
        if(plansza[nrPola(5,2)]==1 and plansza[nrPola(2,5)]==0):
            return nrPola(2,5)
        if(plansza[nrPola(5,4)]==1 and plansza[nrPola(2,1)]==0):
            return nrPola(2,1)
        
        return -1   # w przeciwnym razie uruchomienie minimaxa
        
        
    
    
    return -1   # przejście do minimaxa