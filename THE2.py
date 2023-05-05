coordinates=eval(input())
V0=coordinates[0]
V1=coordinates[1]
V2=coordinates[2]
V3=coordinates[3]
V0X=V0[0]
V0Y=V0[1]
V1X=V1[0]
V1Y=V1[1]
V2X=V2[0]
V2Y=V2[1]
V3X=V3[0]
V3Y=V3[1]

a=min(V0X,V1X,V2X,V3X)

if a==V0X and a==V1X :
    V0=coordinates[0]
    V1=coordinates[1]
    V2=coordinates[2]
    V3=coordinates[3]

elif a==V1X and a==V2X :
    V0=coordinates[1]
    V1=coordinates[2]
    V2=coordinates[3]
    V3=coordinates[0]
    
elif a==V2X and a==V3X :
    V0=coordinates[2]
    V1=coordinates[3]
    V2=coordinates[0]
    V3=coordinates[1]

elif a==V3X and a==V0X :
    V0=coordinates[3]
    V1=coordinates[0]
    V2=coordinates[1]
    V3=coordinates[2]

elif (a==V0X and a==V2X) and (V0Y<V2Y) :
    V0=coordinates[0]
    V1=coordinates[1]
    V2=coordinates[2]
    V3=coordinates[3]

elif (a==V0X and a==V2X) and (V0Y>V2Y) :
    V0=coordinates[2]
    V1=coordinates[3]
    V2=coordinates[0]
    V3=coordinates[1]

elif (a==V1X and a==V3X) and (V1Y<V3Y) :
    V0=coordinates[1]
    V1=coordinates[2]
    V2=coordinates[3]
    V3=coordinates[0]
elif (a==V1X and a==V3X) and (V1Y>V3Y) :
    V0=coordinates[3]
    V1=coordinates[0]
    V2=coordinates[1]
    V3=coordinates[2]

elif min(V0X,V1X,V2X,V3X)==V1X :
    V0=coordinates[1]
    V1=coordinates[2]
    V2=coordinates[3]
    V3=coordinates[0]
elif min(V0X,V1X,V2X,V3X)==V2X :
    V0=coordinates[2]
    V1=coordinates[3]
    V2=coordinates[0]
    V3=coordinates[1]
elif min(V0X,V1X,V2X,V3X)==V3X :
    V0=coordinates[3]
    V1=coordinates[0]
    V2=coordinates[1]
    V3=coordinates[2]
else:                           #V0X minimum durumu
    V0=coordinates[0]
    V1=coordinates[1]
    V2=coordinates[2]
    V3=coordinates[3]
V0X=V0[0]
V0Y=V0[1]
V1X=V1[0]
V1Y=V1[1]
V2X=V2[0]
V2Y=V2[1]
V3X=V3[0]
V3Y=V3[1]

b=max(V0X,V1X,V2X,V3X)

if b==V1X and b==V2X and V0Y<=0 and V1Y<=0 and V2Y<=0 and V3Y<=0 :
    alan=(-V0Y-V1Y)/2*(V1X-V0X)
    
elif b==V2X and b==V3X and V0Y<=0 and V1Y<=0 and V2Y<=0 and V3Y<=0 :     #kare durumu da buraya dahil
    alan=(-V0Y-V1Y)/2*(V1X-V0X)+(-V1Y-V2Y)/2*(V2X-V1X)

elif b==V1X and b==V3X and (V1Y>V3Y) and V0Y<=0 and V1Y<=0 and V2Y<=0 and V3Y<=0 :
    alan=(-V0Y-V1Y)/2*(V1X-V0X)

elif b==V1X and b==V3X and (V1Y<V3Y) and V0Y<=0 and V1Y<=0 and V2Y<=0 and V3Y<=0 :
    alan=(-V0Y-V3Y)/2*(V3X-V0X)

elif max(V0X,V1X,V2X,V3X)==V3X and (V0X==V2X) and V0Y<=0 and V1Y<=0 and V2Y<=0 and V3Y<=0 :  #sola bakan eşit xminli bumerang y ekseni altında
    alan=(-V2Y-V3Y)/2*(V3X-V2X)

elif max(V0X,V1X,V2X,V3X)==V3X and V0Y<=0 and V1Y<=0 and V2Y<=0 and V3Y<=0 :
    alan=(-V0Y-V3Y)/2*(V3X-V0X)-((V1X*V0Y+V0X*V3Y+V3X*V2Y+V2X*V1Y)-(V0X*V1Y+V3X*V0Y+V2X*V3Y+V1X*V2Y))/2

elif max(V0X,V1X,V2X,V3X)==V1X and V0Y<=0 and V1Y<=0 and V2Y<=0 and V3Y<=0 :
    alan=(-V0Y-V1Y)/2*(V1X-V0X)

elif max(V0X,V1X,V2X,V3X)==V2X and V0Y<=0 and V1Y<=0 and V2Y<=0 and V3Y<=0 :
    alan=(-V0Y-V1Y)/2*(V1X-V0X)+(-V1Y-V2Y)/2*(V2X-V1X)

elif (b==V1X and b==V3X) and (V1Y>V3Y) :
    alan=(V0Y+V3Y)/2*(V3X-V0X)

elif (b==V1X and b==V3X) and (V1Y<V3Y) :
    alan=(V0Y+V1Y)/2*(V1X-V0X)

elif b==V1X and b==V2X :
    alan=(V0Y+V3Y)/2*(V3X-V0X)+(V3Y+V2Y)/2*(V2X-V3X)
    
elif (b==V2X and b==V3X) :                  #kare durumu da buraya dahil
    alan=(V0Y+V3Y)/2*(V3X-V0X)
    
elif max(V0X,V1X,V2X,V3X)==V2X :
    alan=(V0Y+V3Y)/2*(V3X-V0X)+(V3Y+V2Y)/2*(V2X-V3X)
    
elif max(V0X,V1X,V2X,V3X)==V3X :
    alan=(V0Y+V3Y)/2*(V3X-V0X)

else :                                       #max(V0X,V1X,V2X,V3X)==V1X
    alan=((V0Y+V1Y)/2*(V1X-V0X))-((V1X*V0Y+V0X*V3Y+V3X*V2Y+V2X*V1Y)-(V0X*V1Y+V3X*V0Y+V2X*V3Y+V1X*V2Y))/2

print("{p:.2f}".format(p=alan))
