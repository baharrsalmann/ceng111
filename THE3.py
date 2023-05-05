def reverse(listem):
    if listem==[]:
        return []
    else:
        return [listem[-1][::-1]] + reverse(listem[:-1])

def dik(P):
    listecik=[]
    for uzunluk in range(len(P[0])):
        for i in P[::-1]:
            listecik.append(i[uzunluk])
    x="".join(listecik)
    length=len(x)//len(P[0])
    return ayirma(x,length) 

def ayirma(stringcik,length):
    if len(stringcik)<length:
        return []
    else:
        return [stringcik[0:length]]+ ayirma(stringcik[length::],length)


def helper(P,I):
   
    for sütun in range(len(I[0])-len(P[0])+1):
        for satir in range(0,len(I)-len(P)+1):
            pattern=[]
            for i in range(satir,satir+len(P)):  
                pattern.append(I[i][sütun:sütun+len(P[0])])
            if pattern==P:
                return satir,sütun
    return False


def pattern_search(P,I):
    P0=P
    P90=dik(P)
    P180=reverse(P)
    P270=reverse(dik(P))
    
    if helper(P0,I)!=False:
        satir,sütun=helper(P0,I)
        return satir,sütun,0

    elif helper(P90,I)!=False:
        satir,sütun=helper(P90,I)
        return satir,sütun,90

    elif helper(P180,I)!=False:
        satir,sütun=helper(P180,I)
        return satir,sütun,180

    elif helper(P270,I)!=False:
        satir,sütun=helper(P270,I)
        return satir,sütun,270

    else:
        return False



