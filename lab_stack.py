def Create_Stack():
    return []

def PushStack(item,Stack):
    Stack.append(item)

def PopStack(Stack):
    return Stack.pop()

def TopStack(Stack):
    return Stack[-1]

def IsEmptyStack(Stack):
    return Stack==[]

"""mystack=Create_Stack()
PushStack(1,mystack)
PushStack(2,mystack)
PushStack(3,mystack)
PushStack(4,mystack)
for i in range(len(mystack)):
    PopStack(mystack)
    print(mystack)"""

def fixsorted(l): 
    s=Create_Stack() 
    ek=Create_Stack()
    for i in range(len(l)-1):
        if l[i+1]<l[i]:
            PushStack(l[i],ek)
        else:
            PushStack(l[i],s)
            for x in range(len(ek)):
                PushStack(PopStack(ek),s)

    PushStack(l[-1],s)
    for x in range(len(ek)):
        PushStack(PopStack(ek),s)
        


    return s

print(fixsorted([1,2,6,5,4,3,10,15,14,13,16,17]))


        
def parantez(stringim):
    chropen=["(","[","{"]
    chrclose=[")","]","}"]
    stackim=Create_Stack()
    for x in stringim:
        if x in chropen:
            PushStack(x,stackim)
        elif x in chrclose:
            if IsEmptyStack(stackim):
                return False
            a=PopStack(stackim)
            if chrclose.index(x)!=chropen.index(a):
                return False
        
    if IsEmptyStack(stackim):
        return True

y=parantez("a(dksl)dlskdl(((kfdlfk]")
print(y)

