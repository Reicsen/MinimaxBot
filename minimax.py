from heurystyka import fHeurystyczna
from wygranaPrzegrana import *
from random import randrange

symPlansza = []

def planszaNaStr(plansza) -> str:
    s = ""
    for el in plansza:
        s+=str(el)
    return s

zbadane = {}    # słownik słowników dla W PEŁNI zbadanych poddrzew 


# funkcja badająca ruchy do określonej głebokości algorytmem minimax z alfa-beta cięciami i dodatkową statyczną analizą sytuacji na planszy (bez dostawiania
# nowych pionków) zdefiniowaną w pliku wygranaPrzegrana.py;
# w przypadku sytuacji określonej jako wygrana/porażka gracza, wynik zapisywany jest jako liczba o wartości bezwzględnej nieosiągalnej standardową
# funkcją oceny heurystycznej; wartość bezwzględna takiej liczby jest zmniejszana o 1 przy każdym kolejnym przekazaniu wyniku do wywołującego
# „poziomu" rekurencji, tak, aby bot mając kilka zwycięskich ścieżek zawsze wybrał tę najkrótszą, a mając same przegrywające ścieżki (przy optymalnej grze
# rywala), zawsze wybrał tę najdłuższą (zwiększając szanse rywala na popełnienie błędu)
def minimax(glebokosc: int, jestMax: bool, wartoscTnaca: int, czyPierwszaWarstwa: bool):
    global zbadane, symPlansza
    
    # sprawdzenie, czy to poddrzewo nie zostało już w pełni zbadane
    if(glebokosc>=3 and not czyPierwszaWarstwa):
        kod = planszaNaStr(symPlansza)
        if(kod in zbadane[glebokosc]):
            return (zbadane[glebokosc])[kod]
            
    
    ## sekcja statycznej analizy sytuacji na planszy w celu sprawdzenia wystąpienia schematu uznawanego jako wygrywający/przegrywający
    
    if(czyCzworka(symPlansza,1)):          # wartość zbyt duża, żeby mogła być osiągnięta standardowym liczeniem
        if(glebokosc>=3 and not czyPierwszaWarstwa):
            (zbadane[glebokosc])[kod] = 1000000025
        return 1000000025
    if(czyCzworka(symPlansza,-1)):         # wartość zbyt mała, żeby mogła być osiągnięta standardowym liczeniem
        if(glebokosc>=3 and not czyPierwszaWarstwa):
            (zbadane[glebokosc])[kod] = -1000000025
        return -1000000025
    if(czyTrojka(symPlansza,-1)):          # wartość zbyt duża, żeby mogła być osiągnięta standardowym liczeniem
        if(glebokosc>=3 and not czyPierwszaWarstwa):
            (zbadane[glebokosc])[kod] = 1000000025
        return 1000000025
    if(czyTrojka(symPlansza,1)):           # wartość zbyt mała, żeby mogła być osiągnięta standardowym liczeniem
        if(glebokosc>=3 and not czyPierwszaWarstwa):
            (zbadane[glebokosc])[kod] = -1000000025
        return -1000000025
    
    indeksyMozliwychCzworekPlus = gdzieMoznaZrobicCzworke(symPlansza,1)
    indeksyMozliwychCzworekMinus = gdzieMoznaZrobicCzworke(symPlansza,-1)
    
    if(jestMax and len(indeksyMozliwychCzworekPlus)>0):
        if(glebokosc>=3 and not czyPierwszaWarstwa):
            (zbadane[glebokosc])[kod] = 1000000025
        return 1000000025
    
    if((not jestMax) and len(indeksyMozliwychCzworekMinus)>0):
        if(glebokosc>=3 and not czyPierwszaWarstwa):
            (zbadane[glebokosc])[kod] = -1000000025
        return -1000000025
    
    if(jestMax and len(indeksyMozliwychCzworekMinus)>1): # rywal może wygrać dwoma różnymi ruchami
        if(glebokosc>=3 and not czyPierwszaWarstwa):
            (zbadane[glebokosc])[kod] = -1000000025
        return -1000000025
    
    if((not jestMax) and len(indeksyMozliwychCzworekPlus)>1):
        if(glebokosc>=3 and not czyPierwszaWarstwa):
            (zbadane[glebokosc])[kod] = 1000000025
        return 1000000025
    
    if(jestMax and len(indeksyMozliwychCzworekMinus)==1):
        if(indeksyMozliwychCzworekMinus[0] in gdzieNieMoznaBoBedzieTrojka(symPlansza,1)):  # rywal może zrobić jedną czwórkę, ale nie można jej zablokować, bo wtedy samemu zrobi się trójkę
            if(glebokosc>=3 and not czyPierwszaWarstwa):
                (zbadane[glebokosc])[kod] = -1000000025
            return -1000000025
        
    if((not jestMax) and len(indeksyMozliwychCzworekPlus)==1):
        if(indeksyMozliwychCzworekPlus[0] in gdzieNieMoznaBoBedzieTrojka(symPlansza,-1)):
            if(glebokosc>=3 and not czyPierwszaWarstwa):
                (zbadane[glebokosc])[kod] = 1000000025
            return 1000000025
        
    if(jestMax and len(indeksyMozliwychCzworekMinus)==0):   # żaden gracz nie może zrobić czwórki, ale można wymusić na rywalu zrobienie trójki (lub niezablokowanie czwórki)
        if(len(indkesyWymuszajace(symPlansza,1))>0):
            if(glebokosc>=3 and not czyPierwszaWarstwa):
                (zbadane[glebokosc])[kod] = 1000000025
            return 1000000025
    
    if((not jestMax) and len(indeksyMozliwychCzworekPlus)==0):
        if(len(indkesyWymuszajace(symPlansza,-1))>0):
            if(glebokosc>=3 and not czyPierwszaWarstwa):
                (zbadane[glebokosc])[kod] = -1000000025
            return -1000000025
    
    
    ## koniec sekcji analizy statycznej
        
    
    if(glebokosc<=0):                   # przeszukiwanie dotarło do maksymalnej dopuszczonej głebokości i nie da się na podstawie planszy określić niczyjej
        return fHeurystyczna(symPlansza)    # pozycji wygrywającej/przegrywającej - ocenienie planszy funkcją heurystyczną
    
    else:        
        if(jestMax):    # maksymalizuje wybór, a „piętro" wyżej minimalizuje - jeśli przekroczy "wartość tnącą", to nie ma sensu dalej liczyć, bo max będzie większy od niej
            
            wartMax=-10000000000    # mniejsze od każdego możliwego wyniku
            
            czworkiRywala=indeksyMozliwychCzworekMinus
            if(len(czworkiRywala)==1):  # >1 lub sprzeczność z własnymi trójkami wykluczone wyżej
                ind = czworkiRywala[0]  # trzeba postawić tu (nie ma sensu analizować innych ruchów, bo oznaczają one porażkę)
                symPlansza[ind] = 1
                wynik = minimax(glebokosc-1,False,wartMax,False)
                symPlansza[ind] = 0
                if(wynik>=1000000000):
                    wynik-=1
                if(wynik<=-1000000000):
                    wynik+=1
                return wynik
            
            
            for i in range(25):
                if(symPlansza[i]==0):  # w przeciwnym razie coś już tam stoi
                    symPlansza[i]=1
                    wynik = minimax(glebokosc-1,False,wartMax,False)
                    symPlansza[i]=0

                    if(wynik>wartoscTnaca or (not czyPierwszaWarstwa and wynik==wartoscTnaca)): # alfa-beta cięcie
                        return wynik
                    
                    elif(wynik>wartMax):
                            wartMax=wynik
            
            if(wartMax>=1000000000):
                wartMax-=1
            if(wartMax<=-1000000000):
                wartMax+=1
            
            if(glebokosc>=3 and not czyPierwszaWarstwa):                       # w pełni zbadane
                (zbadane[glebokosc])[kod] = wartMax
            return wartMax
        
        
        else:    # minimalizuje wybór, a „piętro" wyżej maksymalizuje - jeśli spadnie poniżej "wartości tnącej", to nie ma sensu dalej liczyć, bo min będzie mniejszy od niej
            
            wartMin=10000000000    # mniejsze od każdego możliwego wyniku
            
            czworkiRywala=indeksyMozliwychCzworekPlus
            if(len(czworkiRywala)==1):  # >1 lub sprzeczność z własnymi trójkami wykluczone wyżej
                ind = czworkiRywala[0]  # trzeba postawić tu (nie ma sensu analizować innych ruchów, bo oznaczają one porażkę)
                symPlansza[ind] = -1
                wynik = minimax(glebokosc-1,True,wartMin,False)
                symPlansza[ind] = 0
                if(wynik>=1000000000):
                    wynik-=1
                if(wynik<=-1000000000):
                    wynik+=1
                return wynik
            
            for i in range(25):
                if(symPlansza[i]==0):  # w przeciwnym razie coś już tam stoi
                    symPlansza[i]=-1
                    wynik = minimax(glebokosc-1,True,wartMin,False)
                    symPlansza[i]=0

                    if(wynik<wartoscTnaca or (not czyPierwszaWarstwa and wynik==wartoscTnaca)): # alfa-beta cięcie
                        return wynik
                        
                    elif(wynik<wartMin):
                        wartMin=wynik
        
            if(wartMin>=1000000000):
                wartMin-=1
            if(wartMin<=-1000000000):
                wartMin+=1
            
            if(glebokosc>=3 and not czyPierwszaWarstwa):                       # w pełni zbadane
                (zbadane[glebokosc])[kod] = wartMin
            return wartMin



# funkcja dokonująca wyboru ruchu do gry - najpierw statycznie analizuje istnienie ruchu wygrywającego lub wymuszonego w celu obrony przed zwycięstwem
# rywala, a w przypadku jego braku, dla każdego obecnie pustego pola uruchamia algorytm minimax (o ile dopuszczona głębokość przeszukiwań nie jest zerowa)
# i wybiera najbardziej optymalny ruch (lub losuje jeden z nich, jeśli jest ich kilka)
def wyborRuchu(glebokosc: int, plansza) -> int:
    global zbadane, symPlansza
    
    symPlansza=[]
    for i in range(25):
        symPlansza.append(plansza[i])
        
    ## sekcja statycznej analizy sytuacji na planszy w celu sprawdzenia wystąpienia schematu uznawanego jako wygrywający/przegrywający
        
    indeksyTworzaceCzworke = gdzieMoznaZrobicCzworke(symPlansza,1)     # czy można samemu zrobić czwórkę
    if(len(indeksyTworzaceCzworke)>0):
        return indeksyTworzaceCzworke[randrange(0,len(indeksyTworzaceCzworke))] # jeśli tak, zwróć któryś z tych ruchów
    
    indeksyTworzaceCzworke = gdzieMoznaZrobicCzworke(symPlansza,-1)    # czy rywal może zrobić gdzieś czwórkę
    if(len(indeksyTworzaceCzworke)>0):
        indeksyTworzaceTrojke = gdzieNieMoznaBoBedzieTrojka(symPlansza,1)
        roznica = []
        for ind in indeksyTworzaceCzworke:
            if(ind not in indeksyTworzaceTrojke):
                roznica.append(ind)
        
        if(len(roznica)>0):
            return roznica[randrange(0,len(roznica))]   # zablokowanie czwórki (lub którejś z czwórek) rywala ruchem, który nie tworzy własnej trójki
        
        return indeksyTworzaceCzworke[randrange(0,len(indeksyTworzaceCzworke))] # wymuszone postawienie pionka na polu blokującym czwórkę rywala,
                                                                                # ale tworzącym własną trójkę


    wymuszanie = indkesyWymuszajace(symPlansza,1)           # z powyższego, żaden gracz nie może w jednym ruchu zrobić czwórki
    if(len(wymuszanie)>0):                                  # ryzyko zrobienia własnej trójki wykluczone wewnątrz funkcji
        return wymuszanie[randrange(0,len(wymuszanie))]     # jeśli jest takie pole, wykonanie ruchu, który wymusza na rywalu albo stworzenie
                                                            # trójki, albo niezablokowanie czwórki
    
    ## koniec sekcji analizy statycznej
    
    zbadane.clear()
    for i in range(glebokosc-1,2,-1):   # przygotowanie słownika wyników w pełni przeszukanych poddrzew
        zbadane[i]={}
    
    if(glebokosc>0):
        wartMax = -10000000000  # mniejsze od każdego możliwego wyniku
        indMax=[]
        
        for i in range(25):
            if(symPlansza[i]==0):
                symPlansza[i]=1
                wynik = minimax(glebokosc-1,False,wartMax,True)
                symPlansza[i]=0      # cofnięcie zmian
                                                
                if(wynik==wartMax):     # kolejny ruch o wartości równej najlepszej dotychczasowej
                    indMax.append(i)
                elif(wynik>wartMax):    # nowy najlepszy ruch
                    wartMax=wynik
                    indMax=[]
                    indMax.append(i)
        
        if(len(indMax)==1): # 0 niemożliwe, bo plansza musiałaby być cała zajęta, a wtedy serwer by skończył grę
            return indMax[0]

        else:
            n=len(indMax)
            return indMax[randrange(0,n)]   # zwrócenie losowego ruchu spośród tych o najwyższym wyniku

    else:                       # głębokość szukania=0 - brak możliwości legalnego sprawdzenia czegokolwiek
        ind = randrange(0,25)
        while(symPlansza[ind]!=0):
            ind = randrange(0,25)
        return ind