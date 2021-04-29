s_o, g_o = new_server('localhost', 10001, password='123456789')
index=0
x1=[]
z1=[]
x1.append(6.15)#0
x1.append(6.0)#1
z1.append(0.1)#0
z1.append(0.0)#1
Hgt = g_o.getresults(g_o.Phases[-1], g_o.ResultTypes.Soil.HydraulicGradientTot, 'node')
x = g_o.getresults(g_o.Phases[-1], g_o.ResultTypes.Soil.X, 'node')
z=g_o.getresults(g_o.Phases[-1], g_o.ResultTypes.Soil.Z, 'node')
i=0
g1=[]
g1.append(0)
m=0
h=0
j=0
while j!=10:
    while i<len(Hgt):
        exists = Hgt[i] in g1
        if exists==True:
            m=0
        if exists==False:
            if float(Hgt[i])>=m:
                m=float(Hgt[i])
                index=i
        i+=1
    print("TabloSatırNo:",index,"Hgt:",Hgt[index],"x:",x[index],"z:",z[index])
    exists1=x[index] in x1
    exists2=z[index] in z1
    if exists1==False:
        break
    elif exists2==False:
        break
    else:
        i=0
        j+=1
        g1.append(Hgt[index])
        h+=1
x1.append(x[index])#2,3
z1.append(z[index])#2,3
k=float(x1[0])
m=float(z1[0])
k1=float(x1[1])
m1=float(z1[1])
k2=float(x1[2])
m2=float(z1[2])
print("|",k,"|",m)
print("|",k1,"|",m1)
print("|",k2,"|",m2)
