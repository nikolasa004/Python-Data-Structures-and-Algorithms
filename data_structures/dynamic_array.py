class ObjectNotFound(Exception):
    pass

class DinamickiNiz:
    #pravi niz duzine c, ctypes omogucava rad sa C kodom, py_object znaci da se u C kodu pravi niz ciji su elementi pajton objekti
    #() stvara stvarno niz u memoriji, bez () to bi bio samo konstruktor za stvaranje nizova
    #zbog py_object moze bilo koji pajton objekat 
    def _make_array(self, c):
        import ctypes
        return (c * ctypes.py_object)()

    def __init__(self) :
        self._n=0
        self._kapacitet=1
        self._A=self._make_array(self._kapacitet)

    def __len__(self):
        return self._n
    
    def append(self,x):
        if(self._n==self._kapacitet):
            self._resize()
        self._A[self._n]=x
        self._n+=1

    def append_at(self,ind,x):
        if ind < 0 or ind > self._n:
            raise IndexError("indeks je van opsega")
        if self._n == self._kapacitet:
            self._resize()
        for i in range(self._n,ind,-1):
            self._A[i] = self._A[i-1]
        self._A[ind] = x
        self._n += 1

    def remove(self,x):
        for i in range(self._n):
            if self._A[i] == x:
                self.remove_at(i)
                return
        raise ObjectNotFound("nema objekta")
        
    def remove_at(self,ind):
        if ind < 0 or ind >= self._n:
            raise IndexError("indeks je van opsega")
        for i in range(ind+1,self._n):
            self._A[i-1] = self._A[i]
        self._n -= 1
        self._A[self._n] = None

    def index_of(self,x):
        for i in range(self._n):
            if(self._A[i]==x):
                return i

    def _resize(self):
        B=self._make_array(self._kapacitet*2)
        for i in range(self._kapacitet):
            B[i]=self._A[i]
        self._A=B
        self._kapacitet*=2

    def __getitem__(self,i):
        if 0 <= i < self._n:
            return self._A[i]
        raise IndexError("indeks je van opsega")
        
    def __str__(self):
        ispis="["
        for i in range(self._n):
            if(i==0):
                ispis+=str(self._A[i])
            else:
                ispis+=", "+str(self._A[i])
        ispis+="]"
        return ispis

if __name__ == "__main__":
    a=DinamickiNiz()
    a.append(4)
    a.append(1)
    a.append(7)
    print(len(a))
    print(a)
    a.append_at(1,5)
    print(a)
    a.remove(1)
    print(a)
    a.remove_at(1)
    print(a)
    print(a.index_of(7))
