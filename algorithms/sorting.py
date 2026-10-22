def merge_sort(niz):
    if len(niz)>1:
        leva_polovina = niz[:len(niz)//2]
        desna_polovina = niz[len(niz)//2:]

        levi_niz=merge_sort(leva_polovina)
        desni_niz=merge_sort(desna_polovina)

        pokazivac_levi = 0
        pokazivac_desni = 0

        kraj=False
        while not kraj:
            if pokazivac_levi==len(levi_niz):
                niz[pokazivac_levi+pokazivac_desni:]=desni_niz[pokazivac_desni:]
                kraj=True
            elif pokazivac_desni==len(desni_niz):
                niz[pokazivac_levi+pokazivac_desni:]=levi_niz[pokazivac_levi:]
                kraj=True
            elif levi_niz[pokazivac_levi]<desni_niz[pokazivac_desni]:
                niz[pokazivac_levi+pokazivac_desni]=levi_niz[pokazivac_levi]
                pokazivac_levi+=1
            elif levi_niz[pokazivac_levi]>=desni_niz[pokazivac_desni]:
                niz[pokazivac_levi+pokazivac_desni]=desni_niz[pokazivac_desni]
                pokazivac_desni+=1

        return niz
            
    else:
        return niz
    
def quick_sort(niz):
    if len(niz)>1:
        pivot=niz[0]

        pokazivac_levi=1
        pokazivac_desni=len(niz)-1

        while pokazivac_levi<=pokazivac_desni:
            if niz[pokazivac_levi]>pivot and niz[pokazivac_desni]<pivot:
                niz[pokazivac_levi],niz[pokazivac_desni]=niz[pokazivac_desni],niz[pokazivac_levi]
                pokazivac_levi+=1
                pokazivac_desni-=1
            elif niz[pokazivac_levi]<=pivot:
                pokazivac_levi+=1
            elif niz[pokazivac_desni]>=pivot:
                pokazivac_desni-=1
            
        niz[0],niz[pokazivac_desni]=niz[pokazivac_desni],niz[0]

        leva_polovina=quick_sort(niz[:pokazivac_desni])
        desna_polovina=quick_sort(niz[pokazivac_desni+1:])
        niz=leva_polovina+[niz[pokazivac_desni]]+desna_polovina

        return niz
    else:
        return niz
if __name__ == "__main__":
    niz=[]
    unos=""

    while unos != "kraj":
        unos = input("Unesite element niza: ")
        if unos != "kraj":
            niz.append(int(unos))
        else:
            break

    print("Niz pre sortiranja: ", niz)
    #merge_sort(niz)
    niz=quick_sort(niz)
    print("Niz posle sortiranja: ", niz)