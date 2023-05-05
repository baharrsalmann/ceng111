
def fibonacci(N):
    if N==0:
        return 0
    elif N<=2:
        return 1
    else:
        return fibonacci(N-1)+fibonacci(N-2)


def fibseries(N):
    if N==0 :
        return [0]
   
    else :
        return fibseries(N-1)+[fibonacci(N)]



def sum_all(listem):
    if listem==[]:
        return 0
    elif type(listem[0])==list:
        return sum_all(listem[1::])+ sum_all(listem[0])
    else:
        return listem[0]+ sum_all(listem[1::])
X=sum_all([1,2,3,[3,5],4])

def reverse(listem):
    if listem==[]:
        return []
    
    elif type(listem)!=list :
        return listem
    else:
        return [listem[-1]] + reverse(listem[:-1])
        

X=reverse([[1,2],[4,5,6,7],[6,7,8,9],["h","g","t"],5])



def reverse_list(listem):
    if listem==[]:
        return []
    elif type(listem)!=list :
        return listem
    else:
        a= [reverse(listem[-1])] + reverse_list(listem[:-1]) 
        return a

X=reverse_list([8,[1,2],[4,5,6,7],[6,7,8,9],["h","g","t"],5,6])




def append_element(e,listem):
    if listem==[]:
        return []
    else:
        return [listem[0]+[e]] + append_element(e,listem[1:])


def power_set(listem):
    if listem==[] :
        return [[]]
    else:
        return power_set(listem[1::])+append_element(listem[0],power_set(listem[1::]))


def numbers_between(x,y):
    if x>y:
        a=numbers_between(y,x)
        return a[::-1]
    if x==y :
        return [x]
    else:
        return numbers_between(x,y-1)+ [y]

"""print(numbers_between(0,8))
print(numbers_between(-2,5))"""



def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n

def every(fonksiyonum,listem):
    if listem==[]:
        return []
    else:
        return every(fonksiyonum,listem[:-1])+fonksiyonum(listem[-1])



def even(num):
    if num==0:
        return "even"
    else:
        return odd(num-1)

def odd(num):
    if num==0:
        return "odd"
    else:
        return even(num-1)



def even_indices(listem):
    if listem==[]:
        return []
    elif len(listem)%2==0:
        return even_indices(L[:-1])
    else:
        return even_indices(L[:-1])+[L[-1]]




def myrange(basla,bitis,aralik):
    if basla>bitis:                         #if basla==bitis:                                      
        return []                               #return []
    if basla==bitis:                        #if bitis-basla==1:
        return [basla]                          #return [basla]
    else:
        return [basla]+ myrange(basla+aralik,bitis,aralik)

def count_item(e,listem):
    if listem==[]:
        return 0
    elif listem[0]==e:   
        return count_item(e,listem[1::])+1
    else:
        return count_item(e,listem[1::])


def keep_numbers(listem):
    if listem==[]:
        return []
    elif type(listem[0])==int or type(listem[0])==float:
        return [listem[0]]+ keep_numbers(listem[1::])
    else:
        return keep_numbers(listem[1::])

def keep(fonksiyonum,listem):
    if listem==[]:
        return []
    elif fonksiyonum(listem[0])==True:
         return [listem[0]] + keep(fonksiyonum,listem[1::])
    else:
        return keep(fonksiyonum,listem[1::])

def every(fonksiyonum,listem):
    if listem==[]:
        return []
    else:
        return [fonksiyonum(listem[0])] + every(fonksiyonum,listem[1::])



def new_list(listem,start,end):
    if listem==[]:
        return []
    elif start<0:
        return listem[::-1][end:start]
    else:
        return listem[start:end]

def yeni(listem,step):
    if len(listem)==0:
        return []
    else:
        return [listem[0]] + yeni(listem[step::],step)

def slice(listem,start,end,step):
    a=new_list(listem,start,end)
    return yeni(a,abs(step))


"""x=slice([1,2,3,4], -1,0,-1)
y=slice([1,2,3,4,5,6,7], 1, 8, 2)
z=slice([1,2,3,4], 1, 5, 1)
t=slice([1,2,3,4,], 1, 3, 1)"""

def branch(args,listem):
    if len(args)==1:
        return listem[args[0]]
    else:
        return branch(args[1::],listem[args[0]])

#print(branch([1, 2, 0, 1], [['a', 'b'], [['c', 'd'], ['e', 'f'], [['g', 'h'], ['i', 'j']], 'k'], ['l', 'm']]))
#print(branch([2], [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]) )
#print(branch([2, 1], [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g', 'h']]))

def flatten(listem):
    if listem==[]:
        return []
    elif type(listem[0])!=list:
       return [listem[0]]+ flatten(listem[1::])
    else:       
        return flatten(listem[0]) +flatten(listem[1::])
        
"""print(flatten([1,[2],3,4]))
print(flatten([1,[[2],3],[[[4]]]]))
print(flatten([1,[[2],3],4]))"""


def keep(function,liste):
    if liste==[]:
        return []
    if function(liste[0])==True:
        return [liste[0]]+keep(function,liste[1::])
    else:
        return keep(function,liste[1::])


def remove_item(e,liste):
    if liste==[]:
        return []
    elif e!=liste[0]:
        return [liste[0]]+remove_item(e,liste[1::])
    else:
        return remove_item(e,liste[1::])

#print(remove_item(1, [11,2,2,1,1,1,1]))

x=0
y=0
while y<10 and x<10:
    if x<5:
        x=x+1
        y=y+1
        print("cici")
    else:
        break
else:
    print("noldu1")
    




