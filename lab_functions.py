def codon(b):
    if b=="UUU":
        return "Phenylalainne"
    elif b=="UUA":
        return "Leucine" 
    elif b=="AUU" :
        return "Isoleucine"
    elif b=="GUU" :
        return "Valine"
    elif b=="UCU" :
        return "Serine"


def  translate(a):
    if a[:3]!="AUG":
        return "start codon not recognized"
    elif a[12:]!="UAA" and a[12:]!="UGA" and a[12:]!="UAG" :
        return "stop codon not recognized"
    else:
        sonuc=[codon(a[3:6]),codon(a[6:9]),codon(a[9:12])]
        print(sonuc)

(translate('AUGUCUGUUAUUUGA'))
print(translate('AAAUUUUUAAUUUGA'))
print(translate('AUGUUUUUAAUUUGG'))
translate('AUGUUUUUAAUUUAA')




def process_set(x,y,z):
    if x=="A":
        y.append(z)
        return y
    if x=="R" :
        y.remove(z)
        return(y)
    if x=="C" :
        if z in y :
            return True
        else:
            return False


def spell(x):
    x=str(x)
    a=x[0]
    b=x[1]
    if a=="1":
        first="on"
    elif a=="2":
        first="yirmi"
    
    if b=="1" :
        second="bir"
    elif b=="2":
        second="iki"
    
    c=[first,second]
    return c






def shapetype(x):
    if len(x)==3:
        top=x[0]+x[1]+x[2]
        if x[0]==x[1]==x[2]:
            return "equilateral triangle"
        elif x[0]==x[1] or x[1]==x[2] or x[2]==x[0] :
            return "isosceles" 
        elif (top/2)>=x[0] or (top/2)>=x[1] or (top/2)>=x[2]:
            return "not a triangle"
        else: 
            return "triangle"
    
    elif len(x)==4 :
        if x[0]==x[1]==x[2]==x[3]:
            return "square"
        elif x[0]==x[2] and x[1]==x[3]:
            return "rectangle"
        else:
            return "quad"
    
    else: 
        return "not a shape"





def tictactoe(x):
    first=x[0]
    second=x[1]
    third=x[2]
    if first=="XXX" or second=="XXX" or third=="XXX" :
        return "X"
    elif first=="OOO" or second=="OOO" or third=="OOO" :
        return "O"
    elif first[0]==second[0]==third[0]=="X" :
        return "X"
    elif first[1]==second[1]==third[1]=="O" :
        return "O"
    else:
        return "tie"




def processshape(x):
    shape=x[0]
    if shape=="S":
        b=x[1]
        return b*4
    elif shape=="R":
        b=x[1]
        c=x[2]
        return 2*(b+c)
    else:
        b=x[1]
        c=x[2]
        d=x[3]
        return b+c+d
    


def arithmetic(x):
    operator=x[0]
    op1=x[1]
    op2=x[2]
    if operator=="add":
        return op1+op2
    elif operator=="minus" :
        return op1-op2
    elif operator=="div":
        return op1/op2
    elif operator=="min" :
        if op1<op2:
            return op1
        else:
            return op2





def processvector(arg,listem):
    if arg=="SM":
        first=listem[0]
        second=listem[1]
        return first[0]*second[0]+first[1]*second[1]+first[2]*second[2]
    if arg=="M" :
        c=listem[0]
        magnitude=(c[0]**2+c[1]**2+c[2]**2)**0.5
        return magnitude



def absolute(y):
    if y<0:
        return -y
    else:
        return y



def oddeven(x):
    if type(x) != int :
        return "error"
    if x%2==0:
        return "even"
    if x%2==1:
        return "odd"
    



def pal(a):
    b=a[::-1]
    if "".join(a)=="".join(b) :
        return True
    else:
        return False






def root(a,b,c):
    x1=(-b+((b**2-4*a*c)**(1/2)))/(2*a)
    x2=(-b-((b*b-4*a*c)**0.5))/(2*a)
    return x1,x2