# Funkcje badające statycznie (bez dostawiania pionków, jedynie na podstawie schematów) występowanie pozycji wygrywających/przegrywających
# dla danego gracza

# Użyte w komentarzach kody liczbowe układów na planszy oznaczają pozycje wewnątrz analizowanej czwórki/trójki pól;
# np. dla czwórki układ 1 4 oznacza sytuację X - - X (lub O - - O) w rozpatrywanym rzędzie, kolumnie, przekątnej lub przyprzekątnej

# Przeciwprzekątną nazywana jest ukośna linia pól długości 4 lub 3, "równoległa" do jednej z przekątnych planszy; np. pola (1,3), (2,2), (3,1)
# są jedną z przyprzekątnych 3-elementowych


# funkcja szukająca czy na planszy występują cztery pionki jednego gracza z rzędu
def czyCzworka(plansza, nr: int) -> bool:
    for i in range(5):
        # ustawione 4 z rzędu w rzędzie lub kolumnie
        if((plansza[5*i+1]==nr and plansza[5*i+2]==nr and plansza[5*i+3]==nr) and (plansza[5*i]==nr or plansza[5*i+4]==nr)):
            return True
        
        if((plansza[5+i]==nr and plansza[10+i]==nr and plansza[15+i]==nr) and (plansza[i]==nr or plansza[20+i]==nr)):
            return True
    
    
    # ustawione 4 z rzędu na przekątnej \
    if(plansza[6]==nr and plansza[12]==nr and plansza[18]==nr and (plansza[0]==nr or plansza[24]==nr)):
        return True
    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[1]==nr and plansza[7]==nr and plansza[13]==nr and plansza[19]==nr):
        return True
    
    if(plansza[5]==nr and plansza[11]==nr and plansza[17]==nr and plansza[23]==nr):
        return True
    
    
    # ustawione 4 z rzędu na przekątnej /
    if(plansza[8]==nr and plansza[12]==nr and plansza[16]==nr and (plansza[4]==nr or plansza[20]==nr)):
        return True
    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[3]==nr and plansza[7]==nr and plansza[11]==nr and plansza[15]==nr):
        return True
    
    if(plansza[9]==nr and plansza[13]==nr and plansza[17]==nr and plansza[21]==nr):
        return True
    
    return False






# funkcja szukająca czy na planszy występują trzy pionki jednego gracza z rzędu
def czyTrojka(plansza, nr: int) -> bool:    # wiadomo, że nie ma czwórek (nie trzeba sprawdzać), bo funkcja wyżej wywołana zawsze przed
    for i in range(5):
        # ustawione 3 z rzędu w rzędzie lub kolumnie
        if(plansza[5*i+1]==nr and plansza[5*i+2]==nr and plansza[5*i+3]==nr):
            return True
        
        if(plansza[5*i]==nr and plansza[5*i+1]==nr and plansza[5*i+2]==nr):
            return True
        
        if(plansza[5*i+2]==nr and plansza[5*i+3]==nr and plansza[5*i+4]==nr):
            return True
        
        
        if(plansza[5+i]==nr and plansza[10+i]==nr and plansza[15+i]==nr):
            return True
        
        if(plansza[i]==nr and plansza[5+i]==nr and plansza[10+i]==nr):
            return True
        
        if(plansza[10+i]==nr and plansza[15+i]==nr and plansza[20+i]==nr):
            return True
    
    
    # ustawione 3 z rzędu na przekątnej \
    if(plansza[0]==nr and plansza[6]==nr and plansza[12]==nr):
        return True

    if(plansza[12]==nr and plansza[18]==nr and plansza[24]==nr):
        return True
    
    if(plansza[6]==nr and plansza[12]==nr and plansza[18]==nr):
        return True
    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[7]==nr and plansza[13]==nr and (plansza[1]==nr or plansza[19]==nr)):
        return True
    
    if(plansza[11]==nr and plansza[17]==nr and (plansza[5]==nr or plansza[23]==nr)):
        return True
    
    
    # ustawione 3 z rzędu na przekątnej /
    if(plansza[4]==nr and plansza[8]==nr and plansza[12]==nr):
        return True

    if(plansza[12]==nr and plansza[16]==nr and plansza[20]==nr):
        return True
    
    if(plansza[8]==nr and plansza[12]==nr and plansza[16]==nr):
        return True
    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[7]==nr and plansza[11]==nr and (plansza[3]==nr or plansza[15]==nr)):
        return True
    
    if(plansza[13]==nr and plansza[17]==nr and (plansza[9]==nr or plansza[21]==nr)):
        return True
    
    
    # ustawione 3 z rzędu na którejś z 3-elementowych przyprzekątnych
    if(plansza[2]==nr and plansza[8]==nr and plansza[14]==nr):
        return True
    
    if(plansza[2]==nr and plansza[6]==nr and plansza[10]==nr):
        return True
                
    if(plansza[10]==nr and plansza[16]==nr and plansza[22]==nr):
        return True
    
    if(plansza[14]==nr and plansza[18]==nr and plansza[22]==nr):
        return True
    
    return False







# funkcja szukająca czy na planszy występują cztery pola z rzędu takie, że trzy z nich są zajęte przez tego samego gracza (ale nie tworzą trójki),
# zaś czwarte z nich jest puste i zwracająca listę indeksów takich pustych pól
def gdzieMoznaZrobicCzworke(plansza, nr: int):
    indeksy=[]
    
    for i in range(5):
        # ustawione 1 2 4 w rzędzie lub kolumnie
        if(plansza[5*i]==nr and plansza[5*i+3]==nr):
            if(plansza[5*i+1]==nr and plansza[5*i+2]==0):
                if(5*i+2 not in indeksy):
                    indeksy.append(5*i+2)
            if(plansza[5*i+2]==nr and plansza[5*i+1]==0):
                if(5*i+1 not in indeksy):
                    indeksy.append(5*i+1)
        
        if(plansza[5*i+1]==nr and plansza[5*i+4]==nr):
            if(plansza[5*i+2]==nr and plansza[5*i+3]==0):
                if(5*i+3 not in indeksy):
                    indeksy.append(5*i+3)
            if(plansza[5*i+3]==nr and plansza[5*i+2]==0):
                if(5*i+2 not in indeksy):
                    indeksy.append(5*i+2)
        
        if(plansza[i]==nr and plansza[15+i]==nr):
            if(plansza[5+i]==nr and plansza[10+i]==0):
                if(10+i not in indeksy):
                    indeksy.append(10+i)
            if(plansza[10+i]==nr and plansza[5+i]==0):
                if(5+i not in indeksy):
                    indeksy.append(5+i)
        
        if(plansza[5+i]==nr and plansza[20+i]==nr):
            if(plansza[10+i]==nr and plansza[15+i]==0):
                if(15+i not in indeksy):
                    indeksy.append(15+i)
            if(plansza[15+i]==nr and plansza[10+i]==0):
                if(10+i not in indeksy):
                    indeksy.append(10+i)
    
    
    # ustawione 1 2 4 na przekątnej \
    if(plansza[0]==nr and plansza[18]==nr):
        if(plansza[6]==nr and plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
        if(plansza[12]==nr and plansza[6]==0):
            if(6 not in indeksy):
                indeksy.append(6)
    
    if(plansza[6]==nr and plansza[24]==nr):
        if(plansza[12]==nr and plansza[18]==0):
            if(18 not in indeksy):
                indeksy.append(18)
        if(plansza[18]==nr and plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[1]==nr and plansza[19]==nr):
        if(plansza[7]==nr and plansza[13]==0):
            if(13 not in indeksy):
                indeksy.append(13)
        if(plansza[7]==0 and plansza[13]==nr):
            if(7 not in indeksy):
                indeksy.append(7)
    
    if(plansza[5]==nr and plansza[23]==nr):
        if(plansza[11]==nr and plansza[17]==0):
            if(17 not in indeksy):
                indeksy.append(17)
        if(plansza[11]==0 and plansza[17]==nr):
            if(11 not in indeksy):
                indeksy.append(11)
    
    
    # ustawione 4 z rzędu na przekątnej /
    if(plansza[4]==nr and plansza[16]==nr):
        if(plansza[8]==nr and plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
        if(plansza[12]==nr and plansza[8]==0):
            if(8 not in indeksy):
                indeksy.append(8)
    
    if(plansza[8]==nr and plansza[20]==nr):
        if(plansza[12]==nr and plansza[16]==0):
            if(16 not in indeksy):
                indeksy.append(16)
        if(plansza[16]==nr and plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[3]==nr and plansza[15]==nr):
        if(plansza[7]==nr and plansza[11]==0):
            if(11 not in indeksy):
                indeksy.append(11)
        
        if(plansza[7]==0 and plansza[11]==nr):
            if(7 not in indeksy):
                indeksy.append(7)
    
    if(plansza[9]==nr and plansza[21]==nr):
        if(plansza[13]==nr and plansza[17]==0):
            if(17 not in indeksy):
                indeksy.append(17)
        
        if(plansza[13]==0 and plansza[17]==nr):
            if(13 not in indeksy):
                indeksy.append(13)
    
    wynik = []
    for ind in indeksy:     # zabezpieczenie na wypadek błędu w funkcji, który spowodowałby, że wynik zawierałby już zajęte pole
        if(plansza[ind]==0):
            wynik.append(ind)
    
    return wynik







# funkcja szukająca czy na planszy występują trzy pola z rzędu takie, że dwa z nich są zajęte przez tego samego gracza, zaś trzecie z nich
# jest puste i zwracająca listę indeksów takich pustych pól (są to pola „zabronione" dla danego gracza, które spowodowałyby porażkę);
# z listy na koniec wyłączone są pola, które oprócz stworzenia trójki, utowrzyłyby również zwycięską czwórkę w tej lub innej linii
def gdzieNieMoznaBoBedzieTrojka(plansza, nr: int):
    indeksyDajaceCzworke = gdzieMoznaZrobicCzworke(plansza,nr)
    indeksy=[]
    
    for i in range(5):
        # ustawione 2 z rzędu w rzędzie lub kolumnie (i postawienie kolejnego nie dałoby czwórki)
        if(plansza[5*i]==nr and plansza[5*i+1]==nr):
            if(plansza[5*i+2]==0):
                if(5*i+2 not in indeksy):
                    indeksy.append(5*i+2)
        
        if(plansza[5*i+1]==nr and plansza[5*i+2]==nr):
            if(plansza[5*i]==0):
                if(5*i not in indeksy):
                    indeksy.append(5*i)
            
            if(plansza[5*i+3]==0):
                if(5*i+3 not in indeksy):
                    indeksy.append(5*i+3)
        
        if(plansza[5*i+2]==nr and plansza[5*i+3]==nr):
            if(plansza[5*i+4]==0):
                if(5*i+4 not in indeksy):
                    indeksy.append(5*i+4)
            
            if(plansza[5*i+1]==0):
                if(5*i+1 not in indeksy):
                    indeksy.append(5*i+1)
        
        if(plansza[5*i+4]==nr and plansza[5*i+3]==nr):
            if(plansza[5*i+2]==0):
                if(5*i+2 not in indeksy):
                    indeksy.append(5*i+2)
        
        
        if(plansza[i]==nr and plansza[5+i]==nr):
            if(plansza[10+i]==0):
                if(10+i not in indeksy):
                    indeksy.append(10+i)
        
        if(plansza[5+i]==nr and plansza[10+i]==nr):
            if(plansza[i]==0):
                if(i not in indeksy):
                    indeksy.append(i)
            
            if(plansza[15+i]==0):
                if(15+i not in indeksy):
                    indeksy.append(15+i)
        
        if(plansza[10+i]==nr and plansza[15+i]==nr):
            if(plansza[20+i]==0):
                if(20+i not in indeksy):
                    indeksy.append(20+i)
            
            if(plansza[5+i]==0):
                if(5+i not in indeksy):
                    indeksy.append(5+i)
        
        if(plansza[20+i]==nr and plansza[15+i]==nr):
            if(plansza[10+i]==0):
                if(10+i not in indeksy):
                    indeksy.append(10+i)
        
        
        
        # ustawione 1 3 w  rzędzie lub kolumnie (i dostawienie w środek nie stworzy czwórki)
        
        if(plansza[5*i]==nr and plansza[5*i+2]==nr):
            if(plansza[5*i+1]==0):
                if(5*i+1 not in indeksy):
                    indeksy.append(5*i+1)
        
        if(plansza[5*i+1]==nr and plansza[5*i+3]==nr):
            if(plansza[5*i+2]==0):
                if(5*i+2 not in indeksy):
                    indeksy.append(5*i+2)
        
        if(plansza[5*i+4]==nr and plansza[5*i+2]==nr):
            if(plansza[5*i+3]==0):
                if(5*i+3 not in indeksy):
                    indeksy.append(5*i+3)
        
        
        if(plansza[i]==nr and plansza[10+i]==nr):
            if(plansza[5+i]==0):
                if(5+i not in indeksy):
                    indeksy.append(5+i)
        
        if(plansza[5+i]==nr and plansza[15+i]==nr):
            if(plansza[10+i]==0):
                if(10+i not in indeksy):
                    indeksy.append(10+i)
        
        if(plansza[20+i]==nr and plansza[10+i]==nr):
            if(plansza[15+i]==0):
                if(15+i not in indeksy):
                    indeksy.append(15+i)
    
    
    # ryzyko ustawienia 3 z rzędu na przekątnej \
    if(plansza[0]==nr and plansza[6]==nr):
        if(plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
    
    if(plansza[6]==nr and plansza[12]==nr):
        if(plansza[0]==0):
            if(0 not in indeksy):
                indeksy.append(0)
        
        if(plansza[18]==0):
            if(18 not in indeksy):
                indeksy.append(18)
    
    if(plansza[18]==nr and plansza[12]==nr):
        if(plansza[24]==0):
            if(24 not in indeksy):
                indeksy.append(24)
        
        if(plansza[6]==0):
            if(6 not in indeksy):
                indeksy.append(6)
                
    if(plansza[24]==nr and plansza[18]==nr):
        if(plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
    
    if(plansza[0]==nr and plansza[12]==nr):
        if(plansza[6]==0):
            if(6 not in indeksy):
                indeksy.append(6)
    
    if(plansza[6]==nr and plansza[18]==nr):
        if(plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
    
    if(plansza[24]==nr and plansza[12]==nr):
        if(plansza[18]==0):
            if(18 not in indeksy):
                indeksy.append(18)

    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[1]==nr and plansza[7]==nr):
        if(plansza[13]==0):
            if(13 not in indeksy):
                indeksy.append(13)
    
    if(plansza[7]==nr and plansza[13]==nr):
        if(plansza[1]==0):
            if(1 not in indeksy):
                indeksy.append(1)
        
        if(plansza[19]==0):
            if(19 not in indeksy):
                indeksy.append(19)
        
    if(plansza[13]==nr and plansza[19]==nr):
        if(plansza[7]==0):
            if(7 not in indeksy):
                indeksy.append(7)
    
    if(plansza[1]==nr and plansza[13]==nr):
        if(plansza[7]==0):
            if(7 not in indeksy):
                indeksy.append(7)
    
    if(plansza[7]==nr and plansza[19]==nr):
        if(plansza[13]==0):
            if(13 not in indeksy):
                indeksy.append(13)
    
    
    if(plansza[5]==nr and plansza[11]==nr):
        if(plansza[17]==0):
            if(17 not in indeksy):
                indeksy.append(17)
    
    if(plansza[11]==nr and plansza[17]==nr):
        if(plansza[5]==0):
            if(5 not in indeksy):
                indeksy.append(5)
        
        if(plansza[23]==0):
            if(23 not in indeksy):
                indeksy.append(23)
        
    if(plansza[17]==nr and plansza[23]==nr):
        if(plansza[11]==0):
            if(11 not in indeksy):
                indeksy.append(11)
    
    if(plansza[5]==nr and plansza[17]==nr):
        if(plansza[11]==0):
            if(11 not in indeksy):
                indeksy.append(11)
    
    if(plansza[11]==nr and plansza[23]==nr):
        if(plansza[17]==0):
            if(17 not in indeksy):
                indeksy.append(17)
    
    
    # ryzyko ustawienia 3 z rzędu na przekątnej /
    if(plansza[4]==nr and plansza[8]==nr):
        if(plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
    
    if(plansza[8]==nr and plansza[12]==nr):
        if(plansza[4]==0):
            if(4 not in indeksy):
                indeksy.append(4)
        
        if(plansza[16]==0):
            if(16 not in indeksy):
                indeksy.append(16)
    
    if(plansza[16]==nr and plansza[12]==nr):
        if(plansza[20]==0):
            if(20 not in indeksy):
                indeksy.append(20)
        
        if(plansza[8]==0):
            if(8 not in indeksy):
                indeksy.append(8)
                
    if(plansza[20]==nr and plansza[16]==nr):
        if(plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
    
    if(plansza[4]==nr and plansza[12]==nr):
        if(plansza[8]==0):
            if(8 not in indeksy):
                indeksy.append(8)
    
    if(plansza[8]==nr and plansza[16]==nr):
        if(plansza[12]==0):
            if(12 not in indeksy):
                indeksy.append(12)
    
    if(plansza[20]==nr and plansza[12]==nr):
        if(plansza[16]==0):
            if(16 not in indeksy):
                indeksy.append(16)
    
    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[3]==nr and plansza[7]==nr):
        if(plansza[11]==0):
            if(11 not in indeksy):
                indeksy.append(11)
    
    if(plansza[7]==nr and plansza[11]==nr):
        if(plansza[3]==0):
            if(3 not in indeksy):
                indeksy.append(3)
        
        if(plansza[15]==0):
            if(15 not in indeksy):
                indeksy.append(15)
        
    if(plansza[11]==nr and plansza[15]==nr):
        if(plansza[7]==0):
            if(7 not in indeksy):
                indeksy.append(7)
    
    if(plansza[3]==nr and plansza[11]==nr):
        if(plansza[7]==0):
            if(7 not in indeksy):
                indeksy.append(7)
    
    if(plansza[7]==nr and plansza[15]==nr):
        if(plansza[11]==0):
            if(11 not in indeksy):
                indeksy.append(11)
    
    
    if(plansza[9]==nr and plansza[13]==nr):
        if(plansza[17]==0):
            if(17 not in indeksy):
                indeksy.append(17)
    
    if(plansza[13]==nr and plansza[17]==nr):
        if(plansza[9]==0):
            if(9 not in indeksy):
                indeksy.append(9)
        
        if(plansza[21]==0):
            if(21 not in indeksy):
                indeksy.append(21)
        
    if(plansza[17]==nr and plansza[21]==nr):
        if(plansza[13]==0):
            if(13 not in indeksy):
                indeksy.append(13)
    
    if(plansza[9]==nr and plansza[17]==nr):
        if(plansza[13]==0):
            if(13 not in indeksy):
                indeksy.append(13)
    
    if(plansza[13]==nr and plansza[21]==nr):
        if(plansza[17]==0):
            if(17 not in indeksy):
                indeksy.append(17)
    
    
    # ryzyko ustawienia 3 z rzędu na którejś z 3-elementowych przyprzekątnych
    if(plansza[2]==nr and plansza[8]==nr):
        if(plansza[14]==0):
            if(14 not in indeksy):
                indeksy.append(14)
    
    if(plansza[14]==nr and plansza[8]==nr):
        if(plansza[2]==0):
            if(2 not in indeksy):
                indeksy.append(2)
    
    if(plansza[2]==nr and plansza[14]==nr):
        if(plansza[8]==0):
            if(8 not in indeksy):
                indeksy.append(8)
    
    
    if(plansza[2]==nr and plansza[6]==nr):
        if(plansza[10]==0):
            if(10 not in indeksy):
                indeksy.append(10)
    
    if(plansza[10]==nr and plansza[6]==nr):
        if(plansza[2]==0):
            if(2 not in indeksy):
                indeksy.append(2)
    
    if(plansza[2]==nr and plansza[10]==nr):
        if(plansza[6]==0):
            if(6 not in indeksy):
                indeksy.append(6)
    
                
    if(plansza[10]==nr and plansza[16]==nr):
        if(plansza[22]==0):
            if(22 not in indeksy):
                indeksy.append(22)
    
    if(plansza[22]==nr and plansza[16]==nr):
        if(plansza[10]==0):
            if(10 not in indeksy):
                indeksy.append(10)
    
    if(plansza[10]==nr and plansza[22]==nr):
        if(plansza[16]==0):
            if(16 not in indeksy):
                indeksy.append(16)
    
    
    if(plansza[14]==nr and plansza[18]==nr):
        if(plansza[22]==0):
            if(22 not in indeksy):
                indeksy.append(22)
    
    if(plansza[22]==nr and plansza[18]==nr):
        if(plansza[14]==0):
            if(14 not in indeksy):
                indeksy.append(14)
    
    if(plansza[14]==nr and plansza[22]==nr):
        if(plansza[18]==0):
            if(18 not in indeksy):
                indeksy.append(18)

    wynik = []
    for ind in indeksy:     # zabezpieczenie na wypadek błędu w funkcji, który spowodowałby, że wynik zawierałby już zajęte pole oraz usunięcie indeksów
        if(plansza[ind]==0 and (ind not in indeksyDajaceCzworke)):  # które dają nie tylko trójkę, ale też czwórkę
            wynik.append(ind)
            
    
    return wynik







# funkcja szukająca czy na planszy występują cztery pola z rzędu takie, że dwa z nich są zajęte przez tego samego gracza, a dwa pozostałe są puste,
# z czego gracz ten może postawić poprawnie swój pionek na jednym z tych pól (nie stworzy tym ruchem trójki), zaś postawienie przez przeciwnika
# pionka na drugim z tych pól spowoduje ułożenie przez niego trójki i porażki (funkcja wywoływana jest jedynie, gdy wiadomo, że rywal nie może
# utworzyć żadnej czwórki), ponieważ albo wykona przegrywający ruch, żeby zablokować możliwość utworzenia czwórki, albo tego nie zrobi, dzięki czemu
# umożliwi pierwszemu z graczy stworzenie własnej czwórki i zwycięstwo;
# funkcja ta odpowiada sytuacjom analogicznym do poniższej:
# - - O - -             - - O - -
# - X - X -             - X - X X
# - - O - -    ====>    - - O - -
# - - - - -             - - - - -
# - - - - -             - - - - -
def indkesyWymuszajace(plansza, nr: int):
    indeksy=[]
    wlasneRyzykaTrojek=gdzieNieMoznaBoBedzieTrojka(plansza,nr)
    przeciwneRyzykaTrojek=gdzieNieMoznaBoBedzieTrojka(plansza,-nr)
    
    for i in range(5):
        # ustawione 1 4 w rzędzie lub kolumnie
        if(plansza[5*i]==nr and plansza[5*i+3]==nr):
            if(plansza[5*i+1]==0 and plansza[5*i+2]==0):
                if((5*i+1 not in wlasneRyzykaTrojek) and (5*i+2 in przeciwneRyzykaTrojek)):
                    if(5*i+1 not in indeksy):
                        indeksy.append(5*i+1)
                
                if((5*i+2 not in wlasneRyzykaTrojek) and (5*i+1 in przeciwneRyzykaTrojek)):
                    if(5*i+2 not in indeksy):
                        indeksy.append(5*i+2)
        
        if(plansza[5*i+1]==nr and plansza[5*i+4]==nr):
            if(plansza[5*i+2]==0 and plansza[5*i+3]==0):
                if((5*i+2 not in wlasneRyzykaTrojek) and (5*i+3 in przeciwneRyzykaTrojek)):
                    if(5*i+2 not in indeksy):
                        indeksy.append(5*i+2)
                
                if((5*i+3 not in wlasneRyzykaTrojek) and (5*i+2 in przeciwneRyzykaTrojek)):
                    if(5*i+3 not in indeksy):
                        indeksy.append(5*i+3)
        
        
        if(plansza[i]==nr and plansza[15+i]==nr):
            if(plansza[5+i]==0 and plansza[10+i]==0):
                if((5+i not in wlasneRyzykaTrojek) and (10+i in przeciwneRyzykaTrojek)):
                    if(5+i not in indeksy):
                        indeksy.append(5+i)
                
                if((10+i not in wlasneRyzykaTrojek) and (5+i in przeciwneRyzykaTrojek)):
                    if(10+i not in indeksy):
                        indeksy.append(10+i)
        
        if(plansza[5+i]==nr and plansza[20+i]==nr):
            if(plansza[10+i]==0 and plansza[15+i]==0):
                if((10+i not in wlasneRyzykaTrojek) and (15+i in przeciwneRyzykaTrojek)):
                    if(10+i not in indeksy):
                        indeksy.append(10+i)
                
                if((15+i not in wlasneRyzykaTrojek) and (10+i in przeciwneRyzykaTrojek)):
                    if(15+i not in indeksy):
                        indeksy.append(15+i)
        
        
        # 1 3 ustawione w rzędzie lub kolumnie
        if(plansza[5*i]==nr and plansza[5*i+2]==nr):
            if(plansza[5*i+1]==0 and plansza[5*i+3]==0):                
                if((5*i+3 not in wlasneRyzykaTrojek) and (5*i+1 in przeciwneRyzykaTrojek)):
                    if(5*i+3 not in indeksy):
                        indeksy.append(5*i+3)
        
        if(plansza[5*i+1]==nr and plansza[5*i+3]==nr):
            if(plansza[5*i]==0 and plansza[5*i+2]==0):                
                if((5*i not in wlasneRyzykaTrojek) and (5*i+2 in przeciwneRyzykaTrojek)):
                    if(5*i not in indeksy):
                        indeksy.append(5*i)
            
            if(plansza[5*i+4]==0 and plansza[5*i+2]==0):                
                if((5*i+4 not in wlasneRyzykaTrojek) and (5*i+2 in przeciwneRyzykaTrojek)):
                    if(5*i+4 not in indeksy):
                        indeksy.append(5*i+4)
        
        if(plansza[5*i+4]==nr and plansza[5*i+2]==nr):
            if(plansza[5*i+1]==0 and plansza[5*i+3]==0):                
                if((5*i+1 not in wlasneRyzykaTrojek) and (5*i+3 in przeciwneRyzykaTrojek)):
                    if(5*i+1 not in indeksy):
                        indeksy.append(5*i+1)
        
        
        if(plansza[i]==nr and plansza[10+i]==nr):
            if(plansza[5+i]==0 and plansza[15+i]==0):                
                if((15+i not in wlasneRyzykaTrojek) and (5+i in przeciwneRyzykaTrojek)):
                    if(15+i not in indeksy):
                        indeksy.append(15+i)
        
        if(plansza[5+i]==nr and plansza[15+i]==nr):
            if(plansza[i]==0 and plansza[10+i]==0):                
                if((i not in wlasneRyzykaTrojek) and (10+i in przeciwneRyzykaTrojek)):
                    if(i not in indeksy):
                        indeksy.append(i)
            
            if(plansza[20+i]==0 and plansza[10+i]==0):                
                if((20+i not in wlasneRyzykaTrojek) and (10+i in przeciwneRyzykaTrojek)):
                    if(20+i not in indeksy):
                        indeksy.append(20+i)
        
        if(plansza[20+i]==nr and plansza[10+i]==nr):
            if(plansza[5+i]==0 and plansza[15+i]==0):                
                if((5+i not in wlasneRyzykaTrojek) and (15+i in przeciwneRyzykaTrojek)):
                    if(5+i not in indeksy):
                        indeksy.append(5+i)
        
        
        # 1 2 ustawione w rzędzie lub kolumnie
        if(plansza[5*i]==nr and plansza[5*i+1]==nr):
            if(plansza[5*i+2]==0 and plansza[5*i+3]==0):                
                if((5*i+3 not in wlasneRyzykaTrojek) and (5*i+2 in przeciwneRyzykaTrojek)):
                    if(5*i+3 not in indeksy):
                        indeksy.append(5*i+3)
        
        if(plansza[5*i+1]==nr and plansza[5*i+2]==nr):
            if(plansza[5*i+3]==0 and plansza[5*i+4]==0):                
                if((5*i+4 not in wlasneRyzykaTrojek) and (5*i+3 in przeciwneRyzykaTrojek)):
                    if(5*i+4 not in indeksy):
                        indeksy.append(5*i+4)
        
        if(plansza[5*i+3]==nr and plansza[5*i+2]==nr):
            if(plansza[5*i+1]==0 and plansza[5*i]==0):                
                if((5*i not in wlasneRyzykaTrojek) and (5*i+1 in przeciwneRyzykaTrojek)):
                    if(5*i not in indeksy):
                        indeksy.append(5*i)
        
        if(plansza[5*i+4]==nr and plansza[5*i+3]==nr):
            if(plansza[5*i+2]==0 and plansza[5*i+1]==0):                
                if((5*i+1 not in wlasneRyzykaTrojek) and (5*i+2 in przeciwneRyzykaTrojek)):
                    if(5*i+1 not in indeksy):
                        indeksy.append(5*i+1)
        
        
        if(plansza[i]==nr and plansza[5+i]==nr):
            if(plansza[10+i]==0 and plansza[15+i]==0):                
                if((15+i not in wlasneRyzykaTrojek) and (10+i in przeciwneRyzykaTrojek)):
                    if(15+i not in indeksy):
                        indeksy.append(15+i)
        
        if(plansza[5+i]==nr and plansza[10+i]==nr):
            if(plansza[15+i]==0 and plansza[20+i]==0):                
                if((20+i not in wlasneRyzykaTrojek) and (15+i in przeciwneRyzykaTrojek)):
                    if(20+i not in indeksy):
                        indeksy.append(20+i)
        
        if(plansza[15+i]==nr and plansza[10+i]==nr):
            if(plansza[5+i]==0 and plansza[i]==0):                
                if((i not in wlasneRyzykaTrojek) and (5+i in przeciwneRyzykaTrojek)):
                    if(i not in indeksy):
                        indeksy.append(i)
        
        if(plansza[20+i]==nr and plansza[15+i]==nr):
            if(plansza[10+i]==0 and plansza[5+i]==0):                
                if((5+i not in wlasneRyzykaTrojek) and (10+i in przeciwneRyzykaTrojek)):
                    if(5+i not in indeksy):
                        indeksy.append(5+i)
    
        
    # ustawione 1 4 na przekątnej \
    if(plansza[0]==nr and plansza[18]==nr):
        if(plansza[6]==0 and plansza[12]==0):
            if((6 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(6 not in indeksy):
                    indeksy.append(6)
                
            if((12 not in wlasneRyzykaTrojek) and (6 in przeciwneRyzykaTrojek)):
                if(12 not in indeksy):
                    indeksy.append(12)
        
    if(plansza[6]==nr and plansza[24]==nr):
        if(plansza[12]==0 and plansza[18]==0):
            if((12 not in wlasneRyzykaTrojek) and (18 in przeciwneRyzykaTrojek)):
                if(12 not in indeksy):
                    indeksy.append(12)
                
            if((18 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(18 not in indeksy):
                    indeksy.append(18)
        
        
    # 1 3 
    if(plansza[0]==nr and plansza[12]==nr):
        if(plansza[6]==0 and plansza[18]==0):                
            if((18 not in wlasneRyzykaTrojek) and (6 in przeciwneRyzykaTrojek)):
                if(18 not in indeksy):
                    indeksy.append(18)
        
    if(plansza[6]==nr and plansza[18]==nr):
        if(plansza[0]==0 and plansza[12]==0):                
            if((0 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(0 not in indeksy):
                    indeksy.append(0)
            
        if(plansza[24]==0 and plansza[12]==0):                
            if((24 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(24 not in indeksy):
                    indeksy.append(24)
        
    if(plansza[24]==nr and plansza[12]==nr):
        if(plansza[6]==0 and plansza[18]==0):                
            if((6 not in wlasneRyzykaTrojek) and (18 in przeciwneRyzykaTrojek)):
                if(6 not in indeksy):
                    indeksy.append(6)
        
        
    # 1 2
    if(plansza[0]==nr and plansza[6]==nr):
        if(plansza[12]==0 and plansza[18]==0):                
            if((18 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(18 not in indeksy):
                    indeksy.append(18)
        
    if(plansza[6]==nr and plansza[12]==nr):
        if(plansza[18]==0 and plansza[24]==0):                
            if((24 not in wlasneRyzykaTrojek) and (18 in przeciwneRyzykaTrojek)):
                if(24 not in indeksy):
                    indeksy.append(24)
        
    if(plansza[18]==nr and plansza[12]==nr):
        if(plansza[6]==0 and plansza[0]==0):                
            if((0 not in wlasneRyzykaTrojek) and (6 in przeciwneRyzykaTrojek)):
                if(0 not in indeksy):
                    indeksy.append(0)
        
    if(plansza[24]==nr and plansza[18]==nr):
        if(plansza[12]==0 and plansza[6]==0):                
            if((6 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(6 not in indeksy):
                    indeksy.append(6)

    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[1]==nr and plansza[19]==nr):
        if(plansza[7]==0 and plansza[13]==0):
            if((7 not in wlasneRyzykaTrojek) and (13 in przeciwneRyzykaTrojek)):
                if(7 not in indeksy):
                    indeksy.append(7)
            
            if((13 not in wlasneRyzykaTrojek) and (7 in przeciwneRyzykaTrojek)):
                if(13 not in indeksy):
                    indeksy.append(13)
    
    if(plansza[1]==nr and plansza[13]==nr):
        if(plansza[7]==0 and plansza[19]==0):
            if((19 not in wlasneRyzykaTrojek) and (7 in przeciwneRyzykaTrojek)):
                if(19 not in indeksy):
                    indeksy.append(19)
    
    if(plansza[7]==nr and plansza[19]==nr):
        if(plansza[1]==0 and plansza[13]==0):
            if((1 not in wlasneRyzykaTrojek) and (13 in przeciwneRyzykaTrojek)):
                if(1 not in indeksy):
                    indeksy.append(1)
    
    if(plansza[1]==nr and plansza[7]==nr):
        if(plansza[13]==0 and plansza[19]==0):
            if((19 not in wlasneRyzykaTrojek) and (13 in przeciwneRyzykaTrojek)):
                if(19 not in indeksy):
                    indeksy.append(19)
    
    if(plansza[13]==nr and plansza[19]==nr):
        if(plansza[1]==0 and plansza[7]==0):
            if((1 not in wlasneRyzykaTrojek) and (7 in przeciwneRyzykaTrojek)):
                if(1 not in indeksy):
                    indeksy.append(1)

    
    if(plansza[5]==nr and plansza[23]==nr):
        if(plansza[11]==0 and plansza[17]==0):
            if((11 not in wlasneRyzykaTrojek) and (17 in przeciwneRyzykaTrojek)):
                if(11 not in indeksy):
                    indeksy.append(11)
            
            if((17 not in wlasneRyzykaTrojek) and (11 in przeciwneRyzykaTrojek)):
                if(17 not in indeksy):
                    indeksy.append(17)
    
    if(plansza[5]==nr and plansza[17]==nr):
        if(plansza[11]==0 and plansza[23]==0):
            if((23 not in wlasneRyzykaTrojek) and (11 in przeciwneRyzykaTrojek)):
                if(23 not in indeksy):
                    indeksy.append(23)
    
    if(plansza[11]==nr and plansza[23]==nr):
        if(plansza[5]==0 and plansza[17]==0):
            if((5 not in wlasneRyzykaTrojek) and (17 in przeciwneRyzykaTrojek)):
                if(5 not in indeksy):
                    indeksy.append(5)
    
    if(plansza[5]==nr and plansza[11]==nr):
        if(plansza[17]==0 and plansza[23]==0):
            if((23 not in wlasneRyzykaTrojek) and (17 in przeciwneRyzykaTrojek)):
                if(23 not in indeksy):
                    indeksy.append(23)
    
    if(plansza[17]==nr and plansza[23]==nr):
        if(plansza[5]==0 and plansza[11]==0):
            if((5 not in wlasneRyzykaTrojek) and (11 in przeciwneRyzykaTrojek)):
                if(5 not in indeksy):
                    indeksy.append(5)
    
    
    # ustawione 1 4 na przekątnej /
    if(plansza[4]==nr and plansza[16]==nr):
        if(plansza[8]==0 and plansza[12]==0):
            if((8 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(8 not in indeksy):
                    indeksy.append(8)
                
            if((12 not in wlasneRyzykaTrojek) and (8 in przeciwneRyzykaTrojek)):
                if(12 not in indeksy):
                    indeksy.append(12)
        
    if(plansza[8]==nr and plansza[20]==nr):
        if(plansza[12]==0 and plansza[16]==0):
            if((12 not in wlasneRyzykaTrojek) and (16 in przeciwneRyzykaTrojek)):
                if(12 not in indeksy):
                    indeksy.append(12)
                
            if((16 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(16 not in indeksy):
                    indeksy.append(16)
        
        
    # 1 3 
    if(plansza[4]==nr and plansza[12]==nr):
        if(plansza[8]==0 and plansza[16]==0):                
            if((16 not in wlasneRyzykaTrojek) and (8 in przeciwneRyzykaTrojek)):
                if(16 not in indeksy):
                    indeksy.append(16)
        
    if(plansza[8]==nr and plansza[16]==nr):
        if(plansza[4]==0 and plansza[12]==0):                
            if((4 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(4 not in indeksy):
                    indeksy.append(4)
            
        if(plansza[20]==0 and plansza[12]==0):                
            if((20 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(20 not in indeksy):
                    indeksy.append(20)
        
    if(plansza[20]==nr and plansza[12]==nr):
        if(plansza[8]==0 and plansza[16]==0):                
            if((8 not in wlasneRyzykaTrojek) and (16 in przeciwneRyzykaTrojek)):
                if(8 not in indeksy):
                    indeksy.append(8)
        
        
    # 1 2 
    if(plansza[4]==nr and plansza[8]==nr):
        if(plansza[12]==0 and plansza[16]==0):                
            if((16 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(16 not in indeksy):
                    indeksy.append(16)
        
    if(plansza[8]==nr and plansza[12]==nr):
        if(plansza[16]==0 and plansza[20]==0):                
            if((20 not in wlasneRyzykaTrojek) and (16 in przeciwneRyzykaTrojek)):
                if(20 not in indeksy):
                    indeksy.append(20)
        
    if(plansza[16]==nr and plansza[12]==nr):
        if(plansza[8]==0 and plansza[4]==0):                
            if((4 not in wlasneRyzykaTrojek) and (8 in przeciwneRyzykaTrojek)):
                if(4 not in indeksy):
                    indeksy.append(4)
        
    if(plansza[20]==nr and plansza[16]==nr):
        if(plansza[12]==0 and plansza[8]==0):                
            if((8 not in wlasneRyzykaTrojek) and (12 in przeciwneRyzykaTrojek)):
                if(8 not in indeksy):
                    indeksy.append(8)
    
    
    # lub na przyprzekątnych po którejś jej stronie
    if(plansza[3]==nr and plansza[15]==nr):
        if(plansza[7]==0 and plansza[11]==0):
            if((7 not in wlasneRyzykaTrojek) and (11 in przeciwneRyzykaTrojek)):
                if(7 not in indeksy):
                    indeksy.append(7)
            
            if((11 not in wlasneRyzykaTrojek) and (7 in przeciwneRyzykaTrojek)):
                if(11 not in indeksy):
                    indeksy.append(11)
    
    if(plansza[3]==nr and plansza[11]==nr):
        if(plansza[7]==0 and plansza[15]==0):
            if((15 not in wlasneRyzykaTrojek) and (7 in przeciwneRyzykaTrojek)):
                if(15 not in indeksy):
                    indeksy.append(15)
    
    if(plansza[7]==nr and plansza[15]==nr):
        if(plansza[3]==0 and plansza[11]==0):
            if((3 not in wlasneRyzykaTrojek) and (11 in przeciwneRyzykaTrojek)):
                if(3 not in indeksy):
                    indeksy.append(3)
    
    if(plansza[3]==nr and plansza[7]==nr):
        if(plansza[11]==0 and plansza[15]==0):
            if((15 not in wlasneRyzykaTrojek) and (11 in przeciwneRyzykaTrojek)):
                if(15 not in indeksy):
                    indeksy.append(15)
    
    if(plansza[11]==nr and plansza[15]==nr):
        if(plansza[3]==0 and plansza[7]==0):
            if((3 not in wlasneRyzykaTrojek) and (7 in przeciwneRyzykaTrojek)):
                if(3 not in indeksy):
                    indeksy.append(3)
    
    
    if(plansza[9]==nr and plansza[21]==nr):
        if(plansza[13]==0 and plansza[17]==0):
            if((13 not in wlasneRyzykaTrojek) and (17 in przeciwneRyzykaTrojek)):
                if(13 not in indeksy):
                    indeksy.append(13)
            
            if((17 not in wlasneRyzykaTrojek) and (13 in przeciwneRyzykaTrojek)):
                if(17 not in indeksy):
                    indeksy.append(17)
    
    if(plansza[9]==nr and plansza[17]==nr):
        if(plansza[13]==0 and plansza[21]==0):
            if((21 not in wlasneRyzykaTrojek) and (13 in przeciwneRyzykaTrojek)):
                if(21 not in indeksy):
                    indeksy.append(21)
    
    if(plansza[13]==nr and plansza[21]==nr):
        if(plansza[9]==0 and plansza[17]==0):
            if((9 not in wlasneRyzykaTrojek) and (17 in przeciwneRyzykaTrojek)):
                if(9 not in indeksy):
                    indeksy.append(9)
    
    if(plansza[9]==nr and plansza[13]==nr):
        if(plansza[17]==0 and plansza[21]==0):
            if((21 not in wlasneRyzykaTrojek) and (17 in przeciwneRyzykaTrojek)):
                if(21 not in indeksy):
                    indeksy.append(21)
    
    if(plansza[17]==nr and plansza[21]==nr):
        if(plansza[9]==0 and plansza[13]==0):
            if((9 not in wlasneRyzykaTrojek) and (13 in przeciwneRyzykaTrojek)):
                if(9 not in indeksy):
                    indeksy.append(9)
    
    wynik = []
    for ind in indeksy:     # zabezpieczenie na wypadek błędu w funkcji, który spowodowałby, że wynik zawierałby już zajęte pole
        if(plansza[ind]==0):
            wynik.append(ind)
    
    return wynik
