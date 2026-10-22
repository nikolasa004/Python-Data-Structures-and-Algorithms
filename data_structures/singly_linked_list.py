class Node:
    def __init__(self,vrednost,sledeci) -> None:
        self._vrednost = vrednost
        self._sledeci = sledeci

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

    def __eq__(self, drugi) -> bool:
       return self._vrednost==drugi.vrednost

    def __str__(self) -> str:
        return str(self._vrednost)

class GreskaLista(Exception):
    pass

class JednostrukoSpregnutaLista:
    def __init__(self) -> None:
        self._glava = None
        self._rep = None
        self._velicina = 0

    def dodaj_na_pocetak(self,vrednost):
        novi = Node(vrednost,self._glava)
        self._glava = novi
        if self.prazna():
            self._rep = novi
        self._velicina += 1

    def dodaj_na_kraj(self,vrednost):
        novi = Node(vrednost,None)
        if self.prazna():
            self._glava = novi
        else:
            self._rep.sledeci = novi
        self._rep = novi
        self._velicina += 1

    def izbrisi_sa_pocetka(self):
        if self.prazna():
            raise GreskaLista("Lista je prazna")
        self._glava = self._glava.sledeci
        self._velicina -= 1
        if self.prazna():
            self._rep = None

    def izbrisi_sa_kraja(self):
        if self.prazna():
            raise GreskaLista("Lista je prazna")
        if self._velicina == 1:
            self._glava = None
            self._rep = None
        else:
            trenutni = self._glava
            while trenutni.sledeci is not self._rep:
                trenutni = trenutni.sledeci
            trenutni.sledeci = None
            self._rep = trenutni
        self._velicina -= 1

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
        prethodni = self._glava
        for _ in range(indeks-1):
            prethodni = prethodni.sledeci
        obrisani = prethodni.sledeci
        prethodni.sledeci = obrisani.sledeci
        if obrisani is self._rep:
            self._rep = prethodni
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
        prethodni = None
        trenutni = self._glava
        while trenutni is not None:
            if trenutni.vrednost == vrednost:
                if prethodni is None:
                    self._glava = trenutni.sledeci
                else:
                    prethodni.sledeci = trenutni.sledeci
                if trenutni is self._rep:
                    self._rep = prethodni
                self._velicina -= 1
                return
            prethodni = trenutni
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
        prethodni = self._glava
        for _ in range(indeks-1):
            prethodni = prethodni.sledeci
        prethodni.sledeci = Node(vrednost,prethodni.sledeci)
        self._velicina += 1
    
    def __str__(self):
        ispis=""
        for element in self:
            ispis+=str(element.vrednost)+" "
        return ispis
    
    def __eq__(self,druga_lista):
        if not isinstance(druga_lista,JednostrukoSpregnutaLista):
            return NotImplemented
        if self._velicina != druga_lista._velicina:
            return False
        return all(a.vrednost == b.vrednost for a,b in zip(self,druga_lista))
    
if __name__ == "__main__":
    lista=JednostrukoSpregnutaLista()
    lista.dodaj_na_pocetak(1)
    lista.dodaj_na_pocetak(2)
    lista.dodaj_na_pocetak(3)
    lista.dodaj_na_pocetak(4)
    lista.dodaj_na_pocetak(5)
    lista.dodaj_na_pocetak(6)
    lista.dodaj_na_pocetak(7)
    lista.dodaj_na_pocetak(8)
    lista.dodaj_na_pocetak(9)
    lista.dodaj_na_pocetak(10)
    print(lista)
    lista.izbrisi_sa_pocetka()
    print(lista)
    lista.izbrisi_sa_kraja()
    print(lista)
    print(lista.prvi())
    print(lista.poslednji())
    print(len(lista))
    lista[2]=0
    print(lista)
    lista.izbaci(0)
    print(lista)
    lista.ubaci(2,0)
    print(lista)
    lista2=JednostrukoSpregnutaLista()
    lista2.dodaj_na_pocetak(1)
    lista2.dodaj_na_pocetak(2)
    lista2.dodaj_na_pocetak(3)
    lista2.dodaj_na_pocetak(4)
    lista2.dodaj_na_pocetak(5)
    lista2.dodaj_na_pocetak(6)
    lista2.dodaj_na_pocetak(7)
    lista2.dodaj_na_pocetak(8)
    lista2.dodaj_na_pocetak(9)
    lista2.dodaj_na_pocetak(10)
    print(lista2)
    lista.dodaj(lista2)
    print(lista)
    print(lista==lista2)
    del lista[2]
    print(lista)
    print(lista==lista2)