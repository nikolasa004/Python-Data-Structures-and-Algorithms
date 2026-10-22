class Cvor:
    def __init__(self,vrednost,roditelj,deca) -> None:
        self._vrednost = vrednost
        self._roditelj = roditelj
        self._deca = deca

    @property
    def vrednost(self):
        return self._vrednost
    
    @property
    def roditelj(self):
        return self._roditelj
    
    @property
    def deca(self):
        return self._deca
    
    @vrednost.setter
    def vrednost(self,vrednost):
        self._vrednost = vrednost

    @roditelj.setter
    def roditelj(self,roditelj):
        self._roditelj = roditelj

    @deca.setter
    def deca(self,deca):
        self._deca = deca

    def koren(self):
        if self._roditelj == None:
            return True
        return False
    
    def list(self):
        if(len(self._deca) == 0):
            return True
        return False
    
    def dodaj_dete(self,vrednost_deteta):
        novi_cvor= Cvor(vrednost_deteta,self,[])
        self._deca.append(novi_cvor)

    def __str__(self):
        return str(self._vrednost)
    
class Red:
    def __init__(self) -> None:
        self._elementi = []

    @property
    def elementi(self):
        return self._elementi
    
    @elementi.setter
    def elementi(self,elementi):
        self._elementi = elementi

    def dodaj(self,element):
        self._elementi.append(element)
    
    def izbaci(self):
        return self._elementi.pop(0)

    def prazan(self):
        return len(self._elementi) == 0
    
    def __len__(self):
        return len(self._elementi)
    
    def __str__(self):
        return str(self._elementi)

class Stablo:
    def __init__(self,vrednost) -> None:
        self._koren = Cvor(vrednost,None,[])

    @property
    def koren(self):
        return self._koren
    
    @koren.setter
    def koren(self,koren):
        self._koren = koren

    def __len__(self):
        return self._duzina(self._koren)

    def _duzina(self,cvor):
        if cvor.list():
            return 1
        return 1 + sum(self._duzina(dete) for dete in cvor.deca)

    def dubina(self,cvor):
        trenutni_cvor = cvor
        dubina = 1
        while not trenutni_cvor.koren():
            trenutni_cvor = trenutni_cvor.roditelj
            dubina += 1
        return dubina
    
    def visina(self):
        return self._visina(self._koren)

    def _visina(self,cvor):
        if cvor.list():
            return 1
        else:
            return 1 + max(self._visina(dete) for dete in cvor.deca)
        
    def preorder(self):
        self._preorder(self._koren)

    def _preorder(self,cvor):
        print(cvor)
        for dete in cvor.deca:
            self._preorder(dete)

    def postorder(self):
        self._postorder(self._koren)

    def _postorder(self,cvor):
        for dete in cvor.deca:
            self._postorder(dete)
        print(cvor)

    def po_sirini(self):
        red=Red()
        red.dodaj(self._koren)
        while not red.prazan():
            cvor=red.izbaci()
            print(cvor)
            for dete in cvor.deca:
                red.dodaj(dete)

    def prazno(self):
        if self._koren == None:
            return True
        return False
    
    def broj_dece(self,cvor):
        return len(cvor.deca)
    
    def deca(self,cvor):
        for dete in cvor.deca:
            print(dete)

    def replace(self,stari,novi):
        if stari is self._koren:
            self._koren = novi
            novi.roditelj = None
            return
        if stari.roditelj is None:
            raise ValueError("Cvor nije deo ovog stabla")
        roditelj = stari.roditelj
        for i in range(len(roditelj.deca)):
            if roditelj.deca[i] is stari:
                roditelj.deca[i] = novi
                novi.roditelj = roditelj
                stari.roditelj = None
                return
        raise ValueError("Cvor nije deo ovog stabla")

    def __iter__(self):
        return self._iter(self._koren)
    
    def _iter(self,cvor):
        yield cvor
        for dete in cvor.deca:
            if not dete.list():
                yield from self._iter(dete)
            else:
                yield dete

    def str(self):
        for cvor in self:
            print(cvor)

if __name__ == "__main__":
    s = Stablo(1)
    s.koren.dodaj_dete(2)
    s.koren.dodaj_dete(3)
    s.koren.deca[0].dodaj_dete(4)
    s.koren.deca[0].dodaj_dete(5)
    s.koren.deca[1].dodaj_dete(6)
    s.koren.deca[1].dodaj_dete(7)
    s.koren.deca[0].deca[0].dodaj_dete(8)
    s.koren.deca[0].deca[0].dodaj_dete(9)
    s.koren.deca[0].deca[0].dodaj_dete(10)
    s.koren.deca[0].deca[0].deca[0].dodaj_dete(11)
    s.koren.deca[0].deca[0].deca[0].dodaj_dete(12)
    s.koren.deca[0].deca[0].deca[0].dodaj_dete(13)
    s.koren.deca[0].deca[0].deca[0].deca[0].dodaj_dete(14)
    s.koren.deca[0].deca[0].deca[0].deca[0].dodaj_dete(15)
    s.koren.deca[0].deca[0].deca[0].deca[0].dodaj_dete(16)
    s.koren.deca[0].deca[0].deca[0].deca[0].dodaj_dete(17)
    s.koren.deca[0].deca[0].deca[0].deca[0].dodaj_dete(18)
    s.koren.deca[0].deca[0].deca[0].deca[0].dodaj_dete(19)
    s.koren.deca[0].deca[0].deca[0].deca[0].dodaj_dete(20)
    s.koren.deca[0].deca[0].deca[0].deca[0].dodaj_dete(21)

    '''                                                1
                                                 2            3
                                           4          5      6  7
                                8          9  10
               11               12  13
    14 15 16 17 18 19 20 21'''

    print("Duzina stabla: ",len(s))
    print("Visina stabla: ",s.visina())
    print("Dubina cvora 14: ",s.dubina(s.koren.deca[0].deca[0].deca[0].deca[0].deca[0]))
    print("Preorder: ")
    s.preorder()
    print("Postorder: ")
    s.postorder()
    print("Po sirini: ")
    s.po_sirini()
    print("Broj dece cvora 8: ",s.broj_dece(s.koren.deca[0].deca[0].deca[0]))
    print("Deca cvora 10: ")
    s.deca(s.koren.deca[0].deca[0].deca[0])
    print("Menjanje cvora 8 sa 22: ")
    s.replace(s.koren.deca[0].deca[0].deca[0],Cvor(22,None,[]))
    s.str()
    print("iter: ")
    for cvor in s:
        print(cvor)


