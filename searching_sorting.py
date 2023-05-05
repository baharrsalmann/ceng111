def binarysearch(x,L):
    if len(L)==0: 
        return False
    else:
        mid=len(L)//2
        if x==L[mid]:
            return True
        elif x<L[mid]:
            return binarysearch(x,L[0:mid])
        else:
            return binarysearch(x,L[mid+1:])

#insert an item into ordered list
def insert(x,L):
    if len(L)==0:
        return [x]
    else:
        mid=len(L)//2
        if x<L[mid]:
            return insert(x,L[:mid]) + L[mid:]
        elif x>L[mid]:
            return L[:mid+1] + insert(x,L[mid+1:])

print(insert(5,[1,2,3,6,7,8,10]))

#verilen listeyi bastan sona doğru yere koyarak gitme sortlama
def insertionsort(L):
    if len(L)<=1:
        return L
    else:
        return insert(L[0],insertionsort(L[1::]))

print(insertionsort([1,5,7,2,9,4,6,0]))

def lcs(s1,s2):
    if len(s1)==0 or len(s2)==0:
        return 0
    elif s1[0]==s2[0]:
        return 1+ lcs(s1[1:],s2[1:])
    else:
        return max(lcs(s1,s2[1:]),lcs(s1[1:],s2))
x=lcs("abcd","bd")
print(x)

def fib(n):
    results=[-1]*(n+1)
    results[0]=0
    results[1]=1
    return recursivefib(results,n)

def recursivefib(results,n):
    if results[n]<0:
        results[n]= recursivefib(results,n-1) + recursivefib (results,n-2)
    return results[n]

print(fib(6))

for i in range(1,10):
    print(i," : ")
    for j in range(1,i):
        print(j,"-",end="")
    
def selectionsort(L):
    length=len(L)
    result=[0]*length
    for i in range(0,length):
        result[i]=min(L)
        L.remove(min(L))
    return result

print(selectionsort([3,5,7,2,78,9,2]))

def f(L,m):
    i=0
    j=len(L)-1
    k=(i+j)/2
    while not (L[k]==m or i>j):
        if m>L[k]:
            i=k+1
        else:
            j=k-1
        k=i+(j-i)/2
    return k

x=f([14,21,12,38,7,8,10,-2,16,32,42,0,23],21)
print(x)

#trycallby
x=[4,5]
y=6
def func(a,b):
    a[1]=4
    b=2
    return(a,b)

func(x,y)
print(x,y)


def f(a, c):
    global b
    print(a, b)
    b = 7


def h(a, b):
    def g():
        f(a, b)
        print(a, b)
    print(a, b)
    g()


a = 25
b = 15
h(8, 4)
print(a, b)



