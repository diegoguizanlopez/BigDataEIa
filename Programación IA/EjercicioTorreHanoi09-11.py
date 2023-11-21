# Torre de Hanobi realizado con recursividad

TorreA = []
TorreB = []
TorreC = []

def TorresPrint(A, B, C):
    for i in range(10):
        if len(A) >= (10-i): la = A[10-i-1]
        else: la = 0
        if len(B) >= (10-i): lb = B[10-i-1]
        else: lb = 0
        if len(C) >= (10-i): lc = C[10-i-1]
        else: lc = 0

        sa = " "*(10 - la) + "*"*la + "|" + "*"*la + " "*(10 - la) + " "
        sb = " "*(10 - lb) + "*"*lb + "|" + "*"*lb + " "*(10 - lb) + " "
        sc = " "*(10 - lc) + "*"*lc + "|" + "*"*lc + " "*(10 - lc) + " "
        s = sa + sb + sc

        print(s)
    s = "="*(10 + 1 + 10) + " " + "="*(10 + 1 + 10) + " " + "="*(10 + 1 + 10)
    print(s)
    print()

ndiscos = 15

def mueve(org, dst, aux, ndiscos):
    if ndiscos == 0: return
    mueve(org, aux, dst, ndiscos-1)
    disco = org.pop()
    dst.append(disco)
    TorresPrint(TorreA,TorreB,TorreC)
    mueve(aux, dst, org, ndiscos-1)

for i in range(ndiscos):
    TorreA.append(ndiscos-i)
    
TorresPrint(TorreA,TorreB,TorreC)
mueve(TorreA,TorreB,TorreC, ndiscos)