class Element:
    def __init__(self,vrednost,kljuc) -> None:
        self._vrednost=vrednost
        self._kljuc=kljuc

    @property
    def vrednost(self):
        return self._vrednost
    
    @property
    def kljuc(self):
        return self._kljuc
    
    @kljuc.setter
    def kljuc(self,kljuc):
        self._kljuc=kljuc

    @vrednost.setter
    def vrednost(self,vrednost):
        self._vrednost=vrednost
    
    def __lt__(self,other):
        return self.kljuc<other.kljuc
    
    def __str__(self) -> str:
        return str(self.vrednost)
    
class RedSaPrioritetom:
    def __init__(self) -> None:
        self._elementi=[]

    @property
    def elementi(self):
        return self._elementi
    
    @elementi.setter
    def elementi(self,elementi):
        self._elementi=elementi

    def __len__(self):
        return len(self._elementi)
    
    def prazan(self):
        return len(self._elementi)==0
    
class SortiraniRedSaPrioritetom(RedSaPrioritetom):
    def __init__(self) -> None:
        super().__init__()

    def dodaj(self,element):
        if self.prazan():
            self._elementi.append(element)
        else:
            for i in range(len(self._elementi)):
                if element<self._elementi[i]:
                    self._elementi.insert(i,element)
                    return
            self._elementi.append(element)
                
    def minimalni(self):
        if self.prazan():
            return None
        return self._elementi[0]
    
    def izbaci_minimalni(self):
        if self.prazan():
            return None
        return self._elementi.pop(0)
    
    def __str__(self) -> str:
        ispis=""
        for i in self._elementi:
            ispis+=str(i)+" "
        return ispis

class NesortiraniRedSaPrioritetom(RedSaPrioritetom):
    def __init__(self) -> None:
        super().__init__()
    
    def dodaj(self,element):
        self._elementi.append(element)
    
    def minimalni(self):
        if self.prazan():
            return None
        min=self._elementi[0]
        for i in self._elementi:
            if i<min:
                min=i
        return min
    
    def izbaci_minimalni(self):
        if self.prazan():
            return None
        min=self.minimalni()
        self._elementi.remove(min)
        return min
    
    def __str__(self) -> str:
        ispis=""
        for i in self._elementi:
            ispis+=str(i)+" "
        return ispis

if __name__ == "__main__":
    red=SortiraniRedSaPrioritetom()
    red.dodaj(Element('a',1))
    red.dodaj(Element('b',2))
    red.dodaj(Element('c',3))
    red.dodaj(Element('d',4))
    red.dodaj(Element('e',5))
    red.dodaj(Element('f',6))
    red.dodaj(Element('g',7))
    red.dodaj(Element('h',8))
    red.dodaj(Element('i',9))
    red.dodaj(Element('j',10))
    red.dodaj(Element('k',11))
    red.dodaj(Element('l',12))
    red.dodaj(Element('m',13))
    red.dodaj(Element('n',14))
    red.dodaj(Element('o',15))
    red.dodaj(Element('p',16))
    red.dodaj(Element('q',17))
    print(red)
    print(red.minimalni())
    red.izbaci_minimalni()
    print(red)
    print(red.minimalni())
    red.izbaci_minimalni()
    print(red)
    red.dodaj(Element('x',5)) 
    print(red)

    red=NesortiraniRedSaPrioritetom()
    red.dodaj(Element('a',1))
    red.dodaj(Element('b',2))
    red.dodaj(Element('c',3))
    red.dodaj(Element('d',4))
    red.dodaj(Element('e',5))
    red.dodaj(Element('f',6))
    red.dodaj(Element('g',7))
    red.dodaj(Element('h',8))
    red.dodaj(Element('i',9))
    red.dodaj(Element('j',10))
    red.dodaj(Element('k',11))
    red.dodaj(Element('l',12))
    red.dodaj(Element('m',13))
    red.dodaj(Element('n',14))
    red.dodaj(Element('o',15))
    red.dodaj(Element('p',16))
    red.dodaj(Element('q',17))
    print(red)
    print(red.minimalni())
    red.izbaci_minimalni()
    print(red)
    print(red.minimalni())
    red.izbaci_minimalni()
    print(red)
    red.dodaj(Element('x',5))
    print(red)