def binarna_pretraga(niz,element):
    if len(niz) == 0:
        return False
    if element == niz[len(niz)//2]:
        return True
    if len(niz) == 1:
        return False
    if element < niz[len(niz)//2]:
        return binarna_pretraga(niz[:len(niz)//2],element)
    return binarna_pretraga(niz[len(niz)//2:],element)

if __name__ == "__main__":
    print(binarna_pretraga([1,3,5,7,9,11,13,15,17,19],5))
    print(binarna_pretraga([1,3,5,7,9,11,13,15,17,19],17))
    print(binarna_pretraga([1,3,5,7,9,11,13,15,17,19],8))
