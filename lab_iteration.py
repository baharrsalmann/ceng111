def buble_sort(listem):  
    for x in range(len(listem)):
        changed=False
        for i in range(len(listem)-1):
            if listem[i]>listem[i+1]:
                changed=True
                listem[i],listem[i+1]=listem[i+1],listem[i]
        if changed==False:
            return listem    

a=buble_sort([1,4,5,2,6])


def right_angle_triangle(h):
    for i in range(h):
        print((h-i-1)*" " + (i+1)*"*")


def triangle(h):
    for i in range(h):
        print((h-i-1)*" " + (2*i+1)*"*")



def perfect_numbers(N):
    mytuple=([],[],[])
    for n in range(1,N):
        
        total=0
        for i in range(1,n):
            if n%i==0:
                total=total+i
        if total==n:
            mytuple[0].append(n)
        if total>n:
            mytuple[1].append(n)
        if total<n:
            mytuple[2].append(n)
        
    return mytuple

c=perfect_numbers(5)

def split(stringim,listem):
    yeni=[]
    for i in range(len(stringim)):
        if stringim[i] in listem:
            for j in range(len(stringim[i+1::])):
                if stringim[i+1::][j] in listem:
                    yeni.append(stringim[i+1:i+j+1])
    return yeni
e=split('1,2,3:45,56:678,10000', [',', ':'])

def prime_factors(n):
    asallistem=[]
    for x in range(2,n):
        for a in range(2,x):
            if x%a==0:
                break
        else:
            asallistem.append(x)
    
    
    son=[]
    for asal in asallistem:
        if n%asal==0:
            son.append(asal)
            
    
    return son  

l=prime_factors(66)


def factorial(n):
    if n==0:
        return 1
    else:
        result=1
        for i in range(1,n+1):
            result=result*i
        return result

c=factorial(4)

def countdown(n):
    listem=[]
    for i in range(1,n+1):
        listem.append(i)
    sonuc=listem[::-1]
    return sonuc

f=countdown(8)

def the3N1P(n):
    counter=0
    while n!=1:
        if n%2==1:
            n=3*n+1
        else:
            n=n/2
        counter=counter+1
    else:
        counter=counter+1
    return counter
a=the3N1P(5)

def max3N1P(N):
    listem=[]
    for i in range(1,N):
        listem.append((the3N1P(i)))
    
    u=max(listem)
    a=listem.index(u)+1
    return  a,u


def isprime(n):
    if n==0 or n==1:
        return False
    for bölen in range(2,n):
        if n%bölen==0:
            return False
    else:
        return True

def triangle(n):
    listem=[]
    for i in range(1,n+1):
        a=" "*(n-i)+(2*i-1)*"*"
        listem.append(a)
    return listem

print("\n".join(triangle(3)))

def lis(L):
    olasilar=[]
    for x in range(len(L)-1):
        counter=1
        if x<len(L):
            while L[x-1]<=L[x]:
                print(x)
                counter=counter+1
                x=x+1
            else:
                olasilar.append(counter)
        
    return max(olasilar)


def palindromes(n):
    listem=[]
    for i in range(n+1):
        
        if bin(i)[2::]==bin(i)[-1:1:-1] and str(i)==str(i)[::-1]:
            listem.append(i)
    
    return listem

def triplets(N):
    sonuclar=[]
    for i in range(1,N):
        for j in range(1,N):
            for k in range(1,N):
                if i*i+j*j==k*k and i<j<k:
                    sonuclar.append((i,j,k))
    
    return sonuclar



def prime_factors(n):
    listem=[]
    for i in range(n+1):
        if isprime(i)==1 and n%i==0:
            listem.append(i)
    return listem


def lis(listem):
    olasilar=[]
    for x in range(len(listem)):
        counter=1
        for i in range(len(listem)-1):           0    
            if listem[i]<=listem[i+1]:
                counter=counter+1
                
            else:
                olasilar.append(counter)
                
    return(max(olasilar))

p=lis([3,2,1])
print(p)
