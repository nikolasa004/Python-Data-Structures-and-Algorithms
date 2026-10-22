import random
from enum import Enum

class HashMap():
    def __init__(self, kapacitet=8):
        self._kapacitet = kapacitet
        self._velicina = 0
        self._broj_za_hash = 109345121
        self._niz = []

        # konstante heširanja
        self._a = 1 + random.randrange(self._broj_za_hash-1)
        self._b = random.randrange(self._broj_za_hash)
    #Heš funkcija:
    #Izračunavanje heš koda vrši se po formuli (ax + b) mod p
    
class HashMapBucket(HashMap):
    def __init__(self, kapacitet=8):
        super().__init__(kapacitet)
        for i in range(kapacitet):
            self._niz.append([])

    def _hash(self, x):
        hashed_vrednost = (hash(x)*self._a + self._b) % self._broj_za_hash
        kompresovano = hashed_vrednost % self._kapacitet
        return kompresovano
    
    def __getitem__(self,kljuc):
        indeks=self._hash(kljuc)
        for i in range(len(self._niz[indeks])):
            if self._niz[indeks][i][0]==kljuc:
                return self._niz[indeks][i][1]
        raise KeyError("Ključ nije pronađen")
    
    def __setitem__(self,kljuc,vrednost):
        indeks=self._hash(kljuc)
        for i in range(len(self._niz[indeks])):
            if self._niz[indeks][i][0]==kljuc:
                self._niz[indeks][i][1]=vrednost
                return
        self._niz[indeks].append([kljuc,vrednost])
        self._velicina+=1

    def __delitem__(self,kljuc):
        indeks=self._hash(kljuc)
        for i in range(len(self._niz[indeks])):
            if self._niz[indeks][i][0]==kljuc:
                del self._niz[indeks][i]
                self._velicina-=1
                return
        raise KeyError("Ključ nije pronađen")
    
    def __len__(self):
        return self._velicina
    
    def __iter__(self):
        for i in range(self._kapacitet):
            for j in range(len(self._niz[i])):
                yield self._niz[i][j][0]

    def __contains__(self,kljuc):
        indeks=self._hash(kljuc)
        for i in range(len(self._niz[indeks])):
            if self._niz[indeks][i][0]==kljuc:
                return True
        return False
    
    def kljucevi(self):
        for i in range(self._kapacitet):
            for j in range(len(self._niz[i])):
                yield self._niz[i][j][0]

    def vrednosti(self):
        for i in range(self._kapacitet):
            for j in range(len(self._niz[i])):
                yield self._niz[i][j][1]

    def parovi(self):
        for i in range(self._kapacitet):
            for j in range(len(self._niz[i])):
                yield self._niz[i][j]

class Stanje(Enum):
    SLOBODNO = 0
    ZAUZETO = 1
    OSLOBODJENO = 2

class LinearElement:
    def __init__(self, kljuc, vrednost):
        self._kljuc = kljuc
        self._vrednost = vrednost
        self._stanje=Stanje.SLOBODNO

    @property
    def kljuc(self):
        return self._kljuc
    
    @kljuc.setter
    def kljuc(self,kljuc):
        self._kljuc=kljuc

    @property
    def vrednost(self):
        return self._vrednost
    
    @vrednost.setter
    def vrednost(self,vrednost):
        self._vrednost=vrednost

    @property
    def stanje(self):
        return self._stanje
    
    @stanje.setter
    def stanje(self,stanje):
        self._stanje=stanje

    def __str__(self):
        return str(self.kljuc) + " : " + str(self.vrednost)

class HashMapLinear(HashMap):
    def __init__(self, kapacitet=8):
        super().__init__(kapacitet)
        for i in range(kapacitet):
            self._niz.append(LinearElement(None,None))

    def _hash(self, x):
        hashed_vrednost = (hash(x)*self._a + self._b) % self._broj_za_hash
        kompresovano = hashed_vrednost % self._kapacitet
        return kompresovano
    
    def __getitem__(self,kljuc):
        indeks = self._hash(kljuc)
        for _ in range(self._kapacitet):
            element = self._niz[indeks]
            if element.stanje == Stanje.SLOBODNO:
                break
            if element.stanje == Stanje.ZAUZETO and element.kljuc == kljuc:
                return element.vrednost
            indeks = (indeks+1) % self._kapacitet
        raise KeyError("Ključ nije pronađen")
    
    def __setitem__(self,kljuc,vrednost):
        indeks = self._hash(kljuc)
        prvo_obrisano = None
        for _ in range(self._kapacitet):
            element = self._niz[indeks]
            if element.stanje == Stanje.ZAUZETO:
                if element.kljuc == kljuc:
                    element.vrednost = vrednost
                    return
            elif element.stanje == Stanje.OSLOBODJENO:
                if prvo_obrisano is None:
                    prvo_obrisano = indeks
            else:
                if prvo_obrisano is not None:
                    indeks = prvo_obrisano
                break
            indeks = (indeks+1) % self._kapacitet
        else:
            if prvo_obrisano is None:
                raise KeyError("Nema mesta")
            indeks = prvo_obrisano
        element = self._niz[indeks]
        element.kljuc = kljuc
        element.vrednost = vrednost
        element.stanje = Stanje.ZAUZETO
        self._velicina += 1

    def __delitem__(self,kljuc):
        indeks = self._hash(kljuc)
        for _ in range(self._kapacitet):
            element = self._niz[indeks]
            if element.stanje == Stanje.SLOBODNO:
                break
            if element.stanje == Stanje.ZAUZETO and element.kljuc == kljuc:
                element.kljuc = None
                element.vrednost = None
                element.stanje = Stanje.OSLOBODJENO
                self._velicina -= 1
                return
            indeks = (indeks+1) % self._kapacitet
        raise KeyError("Ključ nije pronađen")
        
    def __len__(self):
        return self._velicina
    
    def __iter__(self):
        for i in range(self._kapacitet):
            if self._niz[i].stanje==Stanje.ZAUZETO:
                yield self._niz[i].kljuc

    def __contains__(self,kljuc):
        indeks=self._hash(kljuc)
        for i in range(self._kapacitet):
            if self._niz[indeks].kljuc==kljuc and self._niz[indeks].stanje==Stanje.ZAUZETO:
                return True
            if self._niz[indeks].stanje==Stanje.SLOBODNO:
                return False
            indeks=(indeks+1)%self._kapacitet
        return False
    
    def kljucevi(self):
        for i in range(self._kapacitet):
            if self._niz[i].stanje==Stanje.ZAUZETO:
                yield self._niz[i].kljuc

    def vrednosti(self):
        for i in range(self._kapacitet):
            if self._niz[i].stanje==Stanje.ZAUZETO:
                yield self._niz[i].vrednost

    def parovi(self):
        for i in range(self._kapacitet):
            if self._niz[i].stanje==Stanje.ZAUZETO:
                yield self._niz[i]

    

if __name__=="__main__":
    h=HashMapBucket()
    h["a"]=1
    h["b"]=2
    h["c"]=3
    h["d"]=4
    h["e"]=5
    h["f"]=6
    h["g"]=7
    h["h"]=8
    h["i"]=9
    h["j"]=10
    print(len(h))
    print("a" in h)
    print("z" in h)
    print(h["a"])
    #print(h["z"])
    del h["a"]
    print(len(h))
    print("a" in h)
    for i in h:
        print(i)
    for i in h.kljucevi():
        print(i)
    for i in h.vrednosti():
        print(i)
    for i in h.parovi():
        print(i)

    print("*********************************")

    h=HashMapLinear()
    h["a"]=1
    h["b"]=2
    h["c"]=3
    h["d"]=4
    h["e"]=5
    h["f"]=6
    h["g"]=7
    h["h"]=8
    #h["i"]=9
    print(len(h))
    print("a" in h)
    print("z" in h)
    print(h["a"])
    #print(h["z"])
    del h["a"]
    print(len(h))
    print("a" in h)
    for i in h:
        print(i)
    for i in h.kljucevi():
        print(i)
    for i in h.vrednosti():
        print(i)
    for i in h.parovi():
        print(i)