class InfiniteLoop(Exception):
    pass

class MojRange:
    def __init__(self,pocetak,kraj=None,korak=1):
        if(korak==0):
            raise InfiniteLoop("Korak ne moze da bude 0")
        else:
            self.__korak=korak
        if(kraj==None):
            self.__pocetak,self.__kraj=0,pocetak
        else:
            self.__pocetak=pocetak
            self.__kraj=kraj

    def __len__(self):
        if((self.__kraj-self.__pocetak)%self.__korak==0):
            duzina=(self.__kraj-self.__pocetak)//self.__korak
        else:
            duzina=(self.__kraj-self.__pocetak)//self.__korak+1
        if(duzina<0):
            return 0
        else:
            return duzina

    def __getitem__(self,i):
        if(0<=i<len(self)):
            return self.__pocetak+self.__korak*i
        else:
            raise IndexError("Indeks je van opsega")
        
if __name__ == "__main__":
    for i in MojRange(2,10,3):
        print(i)
    print()
    r=MojRange(3,12)
    print(r[2])