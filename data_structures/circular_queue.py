MAX_DUZINA=10
class CirkularniRed:

    def __init__(self) -> None:
        self._red = [None] * MAX_DUZINA
        self._velicina = 0
        self._pocetni = 0
    
    def dodaj(self,x):
        if self._velicina == len(self._red):
            self._povecaj()
        zadnji = (self._pocetni + self._velicina) % len(self._red)
        self._red[zadnji] = x
        self._velicina += 1
    
    def uzmi(self):
        if self.prazan():
            raise IndexError("prazan")
        vrednost = self._red[self._pocetni]
        self._red[self._pocetni] = None
        self._pocetni = (self._pocetni + 1) % len(self._red)
        self._velicina -= 1
        return vrednost

    def prvi(self):
        if(self.prazan()):
            raise IndexError("prazan")
        else:
            return self._red[self._pocetni]

    def prazan(self):
        return self._velicina==0
        
    def _povecaj(self):
        stari_kapacitet = len(self._red)
        novi_red = [None] * (stari_kapacitet * 2)
        for i in range(self._velicina):
            novi_red[i] = self._red[(self._pocetni + i) % stari_kapacitet]
        self._red = novi_red
        self._pocetni = 0

    def __len__(self):
        return self._velicina
    
    def __str__(self) -> str:
        return str(self._red)

if __name__ == "__main__":
    red=CirkularniRed()
    print(red.prazan())
    red.dodaj(1)
    red.dodaj(2)
    red.dodaj(3)
    red.dodaj(4)
    print(red)
    print(red.prazan())
    print(len(red))
    print(red.prvi())
    red.uzmi()
    print(red)
    print(red.prvi())
    red.dodaj(5)
    red.dodaj(6)
    red.dodaj(7)
    red.dodaj(8)
    red.dodaj(9)
    red.dodaj(10)
    red.uzmi()
    red.uzmi()
    print(red)
    red.dodaj(11)
    print(red)
    red.dodaj(12)
    print(red)
    red.dodaj(1)
    red.dodaj(1)
    red.dodaj(1)
    red.dodaj(1)
    print(red)
