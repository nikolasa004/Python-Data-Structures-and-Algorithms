import math

class Element:
    def __init__(self,vrednost,kljuc) -> None:
        self._vrednost = vrednost
        self._kljuc = kljuc

    @property
    def vrednost(self):
        return self._vrednost
    
    @property
    def kljuc(self):
        return self._kljuc
    
    @kljuc.setter
    def kljuc(self,kljuc):
        self._kljuc = kljuc

    @vrednost.setter
    def vrednost(self,vrednost):
        self._vrednost = vrednost

    def __lt__(self,other):
        return self._kljuc < other.kljuc

    def __str__(self) -> str:
        return str(self._vrednost)
    
class Heap:
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
        self.up_heap(len(self._elementi)-1)

    def up_heap(self,pozicija):
        if pozicija == 0:
            return
        elif(self._elementi[pozicija]<self._elementi[(pozicija-1)//2]):
            self._elementi[pozicija],self._elementi[(pozicija-1)//2] = self._elementi[(pozicija-1)//2],self._elementi[pozicija]
            self.up_heap((pozicija-1)//2)
        return

    def odstrani(self):
        if self.prazen():
            return None
        self._elementi[0],self._elementi[-1] = self._elementi[-1],self._elementi[0]
        element = self._elementi.pop()
        self.down_heap(0)
        return element

    def down_heap(self,pozicija):
        if pozicija*2+1>=len(self._elementi):
            return
        levi_kljuc=self._elementi[pozicija*2+1]
        if pozicija*2+2>=len(self._elementi):
            desni_kljuc=None
        else:
            desni_kljuc=self._elementi[pozicija*2+2]

        minimalni=0
        if desni_kljuc is None or levi_kljuc<desni_kljuc:
            minimalni=pozicija*2+1
        else:
            minimalni=pozicija*2+2

        if self._elementi[minimalni]<self._elementi[pozicija]:
            self._elementi[minimalni],self._elementi[pozicija] = self._elementi[pozicija],self._elementi[minimalni]
            self.down_heap(minimalni)

    def __len__(self):
        return len(self._elementi)
    
    def prazen(self):
        return len(self._elementi) == 0

    def __str__(self) -> str:
        odvojeno_na_pocetku=0
        izmedju=3
        znak="   "
        ispisi=[]

        broj_celih_nivoa=int(math.sqrt(len(self._elementi)))
        broj_prvog_lista=2**broj_celih_nivoa-1

        ispis=znak*odvojeno_na_pocetku
        for i in range(len(self.elementi)-broj_prvog_lista):
            ispis+=str(self.elementi[broj_prvog_lista+i])
            ispis+=znak*izmedju
        ispis+="\n"
        ispisi.append(ispis)

        stepen=broj_celih_nivoa
        for i in range(broj_celih_nivoa):
            odvojeno_na_pocetku=odvojeno_na_pocetku*2+2
            izmedju=izmedju*2+1
            ispis=znak*odvojeno_na_pocetku
            stepen=stepen-1
            broj_prvog_lista=2**(stepen)-1
            for i in range(2**stepen):
                ispis+=str(self.elementi[i+broj_prvog_lista])
                ispis+=znak*izmedju
            ispis+="\n"
            ispisi.append(ispis)

        glavni_ispis=""
        for i in range(len(ispisi)-1,-1,-1):
            glavni_ispis+=ispisi[i]
        
        return glavni_ispis


            

if __name__ == "__main__":
    h = Heap()
    h.dodaj(Element(1,1))
    h.dodaj(Element(2,2))
    h.dodaj(Element(3,3))
    h.dodaj(Element(4,4))
    h.dodaj(Element(5,5))
    h.dodaj(Element(6,6))
    h.dodaj(Element(7,7))
    h.dodaj(Element(8,8))
    h.dodaj(Element(9,9))
    h.dodaj(Element(10,10))
    h.dodaj(Element(11,11))
    h.dodaj(Element(12,12))
    h.dodaj(Element(13,13))
    h.dodaj(Element(14,14))
    h.dodaj(Element(15,15))
    h.dodaj(Element(16,16))
    h.dodaj(Element(17,17))
    h.dodaj(Element(18,18))
    h.dodaj(Element(19,19))
    h.dodaj(Element(20,20))
    h.dodaj(Element(21,21))
    h.dodaj(Element(22,22))
    h.dodaj(Element(23,23))

    print(h)
    '''print(h.odstrani())
    print(h)
    print(h.odstrani())
    print(h)
    print(h.odstrani())
    print(h)
    print(h.odstrani())
    print(h)

    h.dodaj(Element(1,1))
    print(h)
    h.dodaj(Element(2,2))
    print(h)'''