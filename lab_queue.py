def CreateQueue():
    return []

def PushQueue(item,Queue):
    Queue.append(item)

def PopQueue(Queue):
    p = Queue[0]
    del Queue[0]
    return p


def TopQueue(Queue):
    return Queue[0]

def IsEmptyQueue(Queue):
    return Queue==[]

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
"""
myqueue=CreateQueue()
PushQueue(1,myqueue)
PushQueue(2,myqueue)
PushQueue(3,myqueue)
PushQueue(4,myqueue)

for i in range(len(myqueue)):
    PopQueue(myqueue)
    print(myqueue)
"""

    
def schedule(q): 
    day=0
    result=[]
    days=len(q)
    while day<days:
        if IsEmptyQueue(q):
            break
        elif TopQueue(q)[0]>day:
            PopQueue(q)
            day=day+1
        else:
            result.append(q[0])
            PopQueue(q)
    return result

q = CreateQueue()
PushQueue((1,"John"),q)
PushQueue((5,"George"),q)
PushQueue((1,"Lucy"),q)
PushQueue((2,"Arnold"),q)
PushQueue((3,"William"),q)
PushQueue((4,"Claude"),q)
print(schedule(q))


