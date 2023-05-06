def datum(tree):
    return tree[0]
def left(tree):
    return tree[1]
def right(tree):
    return tree[2]
def isempty(tree):
    return tree == []
def isleaf(tree):
    return (left(tree) == []) and (right(tree) == [])
def makenode(datum, left=[], right=[]):
    return [datum, left, right]

def count_leaves(tree):
    if isempty(tree):
        return 0
    elif isleaf(tree):
        return 1
    else:
        return count_leaves(left(tree)) + count_leaves(right(tree))

tree=[1, [2, [3, [], []], []], [5, [], [6, [], []]]]


def sum_tree(tree):
    if isempty(tree):
        return 0
    elif isleaf(tree):
        return datum(tree)
    else:
        return datum(tree) + sum_tree(left(tree))+ sum_tree(right(tree))


def inorder(tree):
    
    if isempty(tree):
        return []
    
    else:
        return inorder(left(tree)) + [(datum(tree))] + inorder(right(tree))

    

    
(inorder([1, [2, [3, [], []], [4, [], []]], [5, [6, [], []], [7, [], []]]]))

def isbinary(tree):
    if isempty(tree):
        return True
    elif len(tree)==3 and datum(tree)!=[]:
        return isbinary(right(tree)) and isbinary(left(tree))
    else:
        return False

((isbinary([1, [2, [20]], [3, [30]], [4, [40]]])))
(isbinary([[],[],[1,[],[]]]))

def maxdepth(tree):        #aslında height buluyorsun
    if isempty(tree):
        return 0
    else:
        return 1 + max(maxdepth(left(tree)),maxdepth(right(tree)))

(maxdepth([1, [2, [6, [], []], [7, [8, [], []], [9, [], []]]], [3, [4, [], []], [5, [], []]]]))

def numparts(n):
        if n==1:
            return [1]
        elif n%2==0:
            return makenode(n,numparts(int(n/2)),numparts(int(n/2)))
        else:
            return makenode(n,numparts(int((n-1)/2+1)),numparts((int((n-1)/2))))
    

def checkmul(tree):
    if isempty(tree):
        return True
    elif isleaf(tree):
        return True

    elif datum(left(tree))*datum(right(tree))==datum(tree):
        return checkmul(left(tree)) and checkmul(right(tree))
    else:
        return False

checkmul([7, [3, [], []], [5, [], []]])

def isordered(tree):
    if isempty(tree):
        return True
    elif isleaf(tree):
        return True
    elif datum(left(tree))<datum(tree)<datum(right(tree)):
        return isordered(left(tree)) and isordered(right(tree))
    else:
        return False
(isordered([2, [1, [], []], [3, [], []]]))


def path_exist(tree,stringim):
    
    if isempty(tree):
        return False
    elif stringim[0]==datum(tree):
        for x in range(len(stringim)-1):
            if not path_exist(left(tree),stringim[1::]) or path_exist(right(tree),stringim[1::]):
                return False           
    else:
        return path_exist(left(tree),stringim) or path_exist(right(tree),stringim)


    return True

(path_exist(['a', ['b', ['c', [], []], ['d', ['k', [], []], []]], ['e', [], []]], 'abe'))

def increasing_path(tree):
        if isleaf(tree):
            return True
        elif datum(tree)>datum(left(tree)) and datum(tree)>datum(right(tree)):
            return False
        else:
            for x in range(maxdepth(tree)-1):
                if not (datum(tree)>datum(left(tree)) and datum(tree)>datum(right(tree)) and increasing_path(left(tree)) and increasing_path(right(tree))):
                    return False
        
        return True
        

print((increasing_path([4, [5, [], [6, [], [10, [], []]]], [3, [1, [], []], [6, [], []]]])))
""""
def path_has_sum(tree,sayi,sum=0):
    a=0
    b=0
    if isleaf(tree):
        a= a+ datum(tree)
        b= b + datum(tree)
        if a==sayi or b==sayi:
            return True
        
        while not isleaf(tree):

            a= a+ datum(left(tree)) + datum(tree) 
            b= b+ datum(right(tree))+ datum(tree)
            if a==sayi or b==sayi:
                return True
            elif a<sayi and b<sayi:
        
        if not path_has_sum(right(tree)) or path_has_sum(left(tree)):
            return False

        else:
            return True

"""

            
                
     

# print(path_has_sum([1, [6, [3, [], []], []], [4, [], []]], 4))

def build(tree):

    if len(tree)==1:
        return datum(tree)
    elif  datum(tree)=="string":
        return "{}{}".format(build(left(tree)), build(right(tree)))
    elif  datum(tree)=="list":
        return [build(left(tree))] + [build(right(tree))]

                            
(build(['list', ['string', ['ali'], ['veli']], ['list', ['string', ['ali'], ['veli']], ['b']]]))
    

def postorder(tree):
    if isempty(tree):
        return []
    else:
        return postorder(left(tree)) + postorder(right(tree)) + [datum(tree)]

print(postorder([1, [6, [3, [], []], []], [4, [], []]]))
# "".replace(" ","")