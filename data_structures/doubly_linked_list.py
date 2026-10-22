class Node:
    def __init__(self,vrednost,sledeci,prosli) -> None:
        self._vrednost = vrednost
        self._sledeci = sledeci
        self._prosli=prosli

    @property
    def vrednost(self):
        return self._vrednost
    
    @vrednost.setter
    def vrednost(self,vrednost):
        self._vrednost = vrednost

    @property
    def sledeci(self):
        return self._sledeci
    
    @sledeci.setter
    def sledeci(self,sledeci):
        self._sledeci = sledeci

    @property
    def prosli(self):
        return self._prosli
    
    @prosli.setter
    def prosli(self,prosli):
        self._prosli = prosli

    def __eq__(self, drugi) -> bool:
       return self._vrednost==drugi.vrednost

    def __str__(self) -> str:
        return str(self._vrednost)

class GreskaLista(Exception):
    pass

class DvostrukoSpregnutaLista:
    def __init__(self) -> None:
        self._glava = None
        self._rep = None
        self._velicina = 0

    def dodaj_na_pocetak(self,vrednost):
        if self.prazna():
            self._glava=Node(vrednost,None,None)
            self._rep=self._glava
        else:
            novi=Node(vrednost,self._glava,None)
            self._glava.prosli=novi
            self._glava=novi
        self._velicina+=1

    def dodaj_na_kraj(self,vrednost):
        if self.prazna():
            self._glava=Node(vrednost,None,None)
            self._rep=self._glava
        else:
            novi=Node(vrednost,None,self._rep)
            self._rep.sledeci=novi
            self._rep=novi
        self._velicina+=1

    def izbrisi_sa_pocetka(self):
        if self.prazna():
            raise GreskaLista("Lista je prazna")
        self._glava = self._glava.sledeci
        self._velicina -= 1
        if self._glava is None:
            self._rep = None
        else:
            self._glava.prosli = None

    def izbrisi_sa_kraja(self):
        if self.prazna():
            raise GreskaLista("Lista je prazna")
        self._rep = self._rep.prosli
        self._velicina -= 1
        if self._rep is None:
            self._glava = None
        else:
            self._rep.sledeci = None

    def prvi(self):
        if self.prazna():
            raise GreskaLista("Lista je prazna")
        else:
            return self._glava.vrednost
        
    def poslednji(self):
        if self.prazna():
            raise GreskaLista("Lista je prazna")
        else:
            return self._rep.vrednost
        
    def __len__(self):
        return self._velicina
    
    def __iter__(self):
        trenutni=self._glava
        while trenutni is not None:
            yield trenutni
            trenutni=trenutni.sledeci

    def __delitem__(self,indeks):
        if indeks < 0 or indeks >= self._velicina:
            raise GreskaLista("Indeks je van opsega")
        if indeks == 0:
            self.izbrisi_sa_pocetka()
            return
        if indeks == self._velicina-1:
            self.izbrisi_sa_kraja()
            return
        trenutni = self._glava
        for _ in range(indeks):
            trenutni = trenutni.sledeci
        trenutni.prosli.sledeci = trenutni.sledeci
        trenutni.sledeci.prosli = trenutni.prosli
        self._velicina -= 1

    def __setitem__(self,indeks,vrednost):
        if indeks < 0 or indeks >= self._velicina:
            raise GreskaLista("Indeks je van opsega")
        trenutni = self._glava
        for _ in range(indeks):
            trenutni = trenutni.sledeci
        trenutni.vrednost = vrednost

    def __getitem__(self,indeks):
        if indeks < 0 or indeks >= self._velicina:
            raise GreskaLista("Indeks je van opsega")
        trenutni = self._glava
        for _ in range(indeks):
            trenutni = trenutni.sledeci
        return trenutni.vrednost

    def izbaci(self,vrednost):
        trenutni = self._glava
        while trenutni is not None:
            if trenutni.vrednost == vrednost:
                if trenutni.prosli is None:
                    self._glava = trenutni.sledeci
                else:
                    trenutni.prosli.sledeci = trenutni.sledeci
                if trenutni.sledeci is None:
                    self._rep = trenutni.prosli
                else:
                    trenutni.sledeci.prosli = trenutni.prosli
                self._velicina -= 1
                return
            trenutni = trenutni.sledeci
        raise GreskaLista("Element ne postoji u listi")
    
    def dodaj(self,druga_lista):
        for element in druga_lista:
            self.dodaj_na_kraj(element.vrednost)

    def prazna(self):
        if self._velicina==0:
            return True
        return False
    
    def ubaci(self,indeks,vrednost):
        if indeks < 0 or indeks > self._velicina:
            raise GreskaLista("Indeks je van opsega")
        if indeks == 0:
            self.dodaj_na_pocetak(vrednost)
            return
        if indeks == self._velicina:
            self.dodaj_na_kraj(vrednost)
            return
        trenutni = self._glava
        for _ in range(indeks):
            trenutni = trenutni.sledeci
        prethodni = trenutni.prosli
        novi = Node(vrednost,trenutni,prethodni)
        prethodni.sledeci = novi
        trenutni.prosli = novi
        self._velicina += 1
    
    def __str__(self):
        ispis=""
        for element in self:
            ispis+=str(element.vrednost)+" "
        return ispis
    
    def __eq__(self,druga_lista):
        if not isinstance(druga_lista,DvostrukoSpregnutaLista):
            return NotImplemented
        if self._velicina != druga_lista._velicina:
            return False
        return all(a.vrednost == b.vrednost for a,b in zip(self,druga_lista))
    
if __name__ == "__main__":
    lista=DvostrukoSpregnutaLista()
    lista.dodaj_na_pocetak(1)
    lista.dodaj_na_pocetak(2)
    lista.dodaj_na_pocetak(3)
    lista.dodaj_na_pocetak(4)
    lista.dodaj_na_pocetak(5)
    lista.dodaj_na_kraj(6)
    lista.dodaj_na_kraj(7)
    lista.dodaj_na_kraj(8)
    lista.dodaj_na_kraj(9)
    lista.dodaj_na_kraj(10)
    print(lista)
    print(lista.prazna())
    print(lista.prvi())
    print(lista.poslednji())
    print(len(lista))
    lista.izbrisi_sa_pocetka()
    lista.izbrisi_sa_kraja()
    print(lista)
    print(len(lista))
    lista[0]=10
    print(lista)
    lista.izbaci(10)
    print(lista)
    lista2=DvostrukoSpregnutaLista()
    lista2.dodaj_na_pocetak(1)
    lista2.dodaj_na_pocetak(2)
    lista2.dodaj_na_pocetak(3)
    lista2.dodaj_na_pocetak(4)
    lista2.dodaj_na_pocetak(5)
    lista.dodaj(lista2)
    print(lista)
    lista.ubaci(2,10)
    print(lista)
    lista.ubaci(0,10)
    print(lista)
    lista.ubaci(5,10)
    print(lista)
    lista.ubaci(8,10)
    print(lista)
    lista.ubaci(10,10)
    print(lista)
    del lista[0]
    print(lista)
    del lista[4]
    print(lista)
    del lista[7]
    print(lista)
    del lista[6]
    print(lista)
    del lista[3]