def ayirmaca(t):    
    for i in range(len(t)):
        if t[i]=="+" or t[i]=="-" or t[i]=="*" or t[i]=="^" :
            func=t[0]
            opr=t[i]
            term1=t[5:i]
            term2=t[i+1:]
            return func,opr,term1,term2


def tree(t,L):
    func,opr,term1,term2 = ayirmaca(t)
    
    if term1[0].isalpha() and term2[0].isalpha() and term1[0]!="x" and term2[0]!="x" :
        
        for i in L:                                   #içteki fonksiyonları aramaya gidiyor,yerine koyuyor.
            if term1[0]==i[0]:
                for j in L:
                    if term2[0]==j[0]:
                        return [func,opr,tree(i,L),tree(j,L)]

    elif term1[0].isalpha() and term1[0]!="x":
        
        for i in L:
            if term1[0]==i[0]:
                return [func,opr,tree(i,L),[term2]]
            
    elif term2[0].isalpha() and term2[0]!="x":
        
        for i in L:
            if term2[0]==i[0]:
                return [func,opr,[term1],tree(i,L)]
    
    else: #iç içe fonksiyon olmadığı durum
        
        return [func,opr,[term1],[term2]]


def construct_forest(Defs):   
    L=[]
    for function in Defs:         #verilen Defs'teki boslukları kapatır, L listesi bosluksuz fonksiyonlardan olusur.
        new=""
        for s in function:
            if s==" ":
                continue
            else:
                new=new+s
        L.append(new)
    terms=[]
    for t in L:
        func,opr,term1,term2 = ayirmaca(t)
        if term1[0].isalpha() and term2[0].isalpha() and term1[0]!="x" and term2[0]!="x" :
            terms=terms+[term1[0]]+[term2[0]]
        elif term1[0].isalpha() and term1[0]!="x":
            terms=terms+[term1[0]]
        elif term2[0].isalpha() and term2[0]!="x":
            terms=terms+[term2[0]]
        
    
    result=[]
    for t in L:
        if t[0] not in terms:
            result.append(tree(t,L))
        

    return result

    

