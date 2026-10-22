import tokenizer

#greska vezana za stek
class StackError(Exception):
    pass

#stek
class Stack(object):
    #konstruktor
    def __init__(self):
        self._data = []
    
    #vraca broj elemenata na steku
    def __len__(self):
        return len(self._data)

    #proverava da li je stek prazan
    def is_empty(self):
        if(len(self._data)==0):
            return True
        else:
            return False

    #dodaje element na stek
    def push(self, element):
        self._data.append(element)

    #vraca element sa vrha steka ako stek nije prazan, ako jeste baca gresku
    def top(self):
        if(self.is_empty()):
            raise StackError("Stek je prazan")
        return self._data[-1]

    #vraca i izbacuje element sa vrha steka ako stek nije prazan, ako jeste baca gresku
    def pop(self):
        if(self.is_empty()):
            raise StackError("Stek je prazan")
        return self._data.pop()

#greska za nevalidan izraz
class InvalidExpression(Exception):
    pass

#podela prioriteta znakovima
prioriteti_znakova={
    "+":1,
    "-":1,
    "*":2,
    "/":2,
    "^":3,
    "(":0,
    ")":0,
    "_":1
}

#funkcija konvertuje izraz iz infiksne u postfiksnu notaciju, vraca listu tokena koji predstavljaju izraz expression zapisan u postfiksnoj notaciji
def infix_to_postfix(expression):
    #podela izraza na tokene(ako nije string ili ako sadrzi nevalidne znakove baci se greska)
    tokeni=tokenizer.tokenize(expression)

    #provera da li je izraz validan:

    #provera za specijalni slucaj "", tacnije kada se nista ne unese
    if(len(tokeni)==0):
        raise InvalidExpression("Niste nista uneli")

    #provera za specijalan slucaj ()
    for i in range(1,len(tokeni)):
        if(tokeni[i-1]=="(" and tokeni[i]==")"):
            raise InvalidExpression("Dati izraz nije validan, proverite zagrade")

    #provera da nisu napisana dva broja jedan do drugog(npr. za slucaj kao sto je 123.1234.13 ovo baca gresku)
    for i in range(1,len(tokeni)):
        if(tokeni[i] not in prioriteti_znakova.keys() and tokeni[i-1] not in prioriteti_znakova.keys()):
            raise InvalidExpression("Dati izraz nije validan, postoje susedni brojevi bez operacije izmedju")
                
    #provera da nisu napisana dva znaka jedan do drugog
    for i in range(1,len(tokeni)):
        if(tokeni[i] in prioriteti_znakova.keys() and tokeni[i-1] in prioriteti_znakova.keys() and tokeni[i] not in "()" and tokeni[i-1] not in "()"):
            raise InvalidExpression("Dati izraz nije validan, postoje operacije koje se nalaze jedna do druge")

    #provera da nije unet 'unarni' plus, puta, podeljeno ili stepen na pocetku izraza kao i da nije uneta sama operacija na kraju izraza
    if(tokeni[0] in "+*/^" or tokeni[-1] in "+*/^-"):
        raise InvalidExpression("Dati izraz nije validan, operacije su pogresne")
    
    #provera da li su zagrade unete pravilno, tacnije da li uvek ide prvo ( i da li svaka ( ima odgovarajucu )
    broj_nezatvorenih_zagrada=0
    for i in range(len(tokeni)):
        if(tokeni[i]=="("):
            broj_nezatvorenih_zagrada+=1
        if(tokeni[i]==")"):
            if(broj_nezatvorenih_zagrada==0):
                raise InvalidExpression("Dati izraz nije validan, provetite zagrade")
            else:
                broj_nezatvorenih_zagrada-=1
    if(broj_nezatvorenih_zagrada!=0):
        raise InvalidExpression("Dati izraz nije validan, provetite zagrade")

    #provera da nije unet 'unarni' plus, puta, podeljeno ili stepen na pocetku izraza u zagradi kao i da nije uneta sama operacija na kraju izraza u zagradi
    for i in range(len(tokeni)):
        if(tokeni[i]=="(" and tokeni[i+1] in "+*/^"):
            raise InvalidExpression("Dati izraz nije validan, operacije su pogresne")
        if(tokeni[i]==")" and tokeni[i-1] in "+*/^-"):
            raise InvalidExpression("Dati izraz nije validan, operacije su pogresne")

    #dodatna podesavanja:
    
    #namestanje unarnog minusa
    for i in range(len(tokeni)):
        if(tokeni[i]=="-" and tokeni[i+1]=="("):
            if(i==0):
                tokeni[i]="_"
            elif(tokeni[i-1]=="("):
                tokeni[i]="_"

    #podesavanje da minus koji nije operacija vec deo negativnih brojeva bude deo njih a ne odvojen
    za_brisanje=[]
    for i in range(len(tokeni)):
        if(tokeni[i]=="-" and tokeni[i+1] not in prioriteti_znakova.keys()):
            if((len(tokeni)>i+3 and tokeni[i+2]!="^") or len(tokeni)<=i+3): #ako je posle minusa stepen onda se taj minus racuna kao unarni a ne kao deo negativnog broja jer npr. -2^2=-4 a (-2)^2=4
                if(i==0):
                    tokeni[i+1]="-"+tokeni[i+1]
                    za_brisanje.append(i)
                elif(tokeni[i-1]=="("):
                    tokeni[i+1]="-"+tokeni[i+1]
                    za_brisanje.append(i)
            else:
                if(i==0):
                    tokeni[i]="_"
                elif(tokeni[i-1]=="("):
                    tokeni[i]="_"
    #brisanje viska minuseva
    if(len(za_brisanje)>0):
        for i in range(len(za_brisanje)-1,-1,-1):
            del tokeni[za_brisanje[i]]
            
    stek=Stack()
    izlaz=[]

    #konverzija iz infiksne u postfiksnu notaciju
    for i in range(len(tokeni)):
        if(tokeni[i] in prioriteti_znakova.keys()): #ako je znak
            if(tokeni[i]=="("):
                stek.push(tokeni[i])
            elif(tokeni[i]==")"):
                while(stek.top()!="("):
                    izlaz.append(stek.pop())
                stek.pop()
            else: #ako nisu zagrade vec neka operacija
                if(stek.is_empty() or prioriteti_znakova[tokeni[i]]>prioriteti_znakova[stek.top()]): #ako je zadnji znak na steku manjeg prioriteta 
                    stek.push(tokeni[i])
                else: #ako je zadnji znak na steku veceg ili jednakog prioriteta
                    while(stek.is_empty()==False and prioriteti_znakova[tokeni[i]]<=prioriteti_znakova[stek.top()]):
                        izlaz.append(stek.pop())
                    stek.push(tokeni[i])
        else: #ako je broj
            izlaz.append(tokeni[i])

    #praznjenje steka
    for i in range(len(stek)):
        izlaz.append(stek.pop())

    return izlaz

#greska ako se desi korenovanje negativnog broja
class ComplexNumberError(Exception):
    pass

#provera da li je neki string broj
def da_li_float(broj):
    try:
        float(broj)
    except:
        return False
    return True
    
#funkcija izračunava vrednost izraza zapisanog u postfiksnoj notaciji, vraca broj koji reprezentuje konačnu vrednost izraza
def calculate_postfix(token_list):
    #kada se postfix oblik dobija od infixa pomocu prve metode on ce biti dobrog oblika ili ce naici na problem i baciti gresku pri samoj konverziji u postfix
    #ali ako mi direktno unosimo postfix izraz onda moze doci do problema, postoje cetiri glavna problema: nije unet niz stringova kao ulaz, nevalidni znakovi, pogresan redosled ili broj operanada i pogresan broj ili redosled operacija

    #provera da li je ulazni parametar niz tipa string
    if(isinstance(token_list,list)==False):
        raise tokenizer.ExpressionNotStringError("Uneti izraz mora da bude niz tipa string")
    else:
        for i in range(len(token_list)):
            if(isinstance(token_list[i],str)==False):
                raise tokenizer.ExpressionNotStringError("Uneti izraz mora da bude niz tipa string")

    #validacija znakova 
    for i in range(len(token_list)):
        if(token_list[i] not in "+-*/^_" and da_li_float(token_list[i])==False):
            raise InvalidExpression("Uneti izraz je nevalidan, sadrzi pogresne znakove")

    stek=Stack()
    
    #racun
    for i in range(len(token_list)):
        try:
            if(token_list[i] not in prioriteti_znakova.keys()): #ako je broj ide na stek
                stek.push(token_list[i])
            elif(token_list[i]=="_"):   #ako je unarni minus skida se samo jedan broj sa steka, negira se i vraca na stek
                if("." in str(stek.top())):
                    x=float(stek.pop())
                else:
                    x=int(stek.pop())
                stek.push(-x)
            else:   #ako je neka od drugih operacija, uzimaju se dva broja sa steka, racunaju se i rezultat se vraca na stek
                if("." in str(stek.top())):
                    y=float(stek.pop())
                else:                       #radilo bi i da samo pretvaram u float ali radi pravilnosti razdvajam decimalne od celih brojeva
                    y=int(stek.pop())

                if("." in str(stek.top())):
                    x=float(stek.pop())
                else:
                    x=int(stek.pop())

                if(token_list[i]=="+"):
                    stek.push(x+y)
                elif(token_list[i]=="-"):
                    stek.push(x-y)
                elif(token_list[i]=="*"):
                    stek.push(x*y)
                elif(token_list[i]=="/"): #greska koja moze da se desi sa deljenjem je deljene sa 0 ali kako je ta greska vec ugradjena samo cemo nju baciti
                    if(y==0):
                        raise ZeroDivisionError("Doslo je do deljenja sa nulom")
                    else:
                        stek.push(x/y)
                else:
                    if(x<0 and int(y)!=y): #ako je u pitanju korenovanje negativnog broja baciti gresku jer je to kompleksan broj
                        raise ComplexNumberError("Koren negativnog broja je kompleksan broj")
                    else:
                        stek.push(x**y)
        except StackError:  #ako dodje do problema sa stekom znaci da je prazan a to moze da se desi samo ako postoji problem sa operacijama
            raise InvalidExpression("Uneti izraz je nevalidan, proverite operacije")

    #na samom kraju na steku ostaje samo resenje ali ako je ostalo vise brojeva na steku znaci da je uneti izraz pogresan, tacnije njegovi operandi
    resenje=stek.pop()
    if(stek.is_empty()):
        return resenje
    else:
        raise InvalidExpression("Uneti izraz je pogresan, proverite operande")

#funkcija izračunava vrednost izraza zapisanog u infiksnoj notaciji, vraca broj koji predstavlja vrednost izraza
def calculate_infix(expression):
    #prebacujemo infix u postfix
    postfix_izraz=infix_to_postfix(expression)
    #racunamo vrednost postfixa i to vracamo
    return calculate_postfix(postfix_izraz)
   
if __name__ == "__main__":
    izraz=input("Unesite izraz: ")
    izlaz=infix_to_postfix(izraz)
    print(izlaz)
    print(calculate_postfix(izlaz))
    print(calculate_infix(izraz))