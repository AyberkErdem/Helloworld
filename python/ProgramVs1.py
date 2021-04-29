import xlrd
from plxscripting.easy import *
# Give the location of the file
loc = ("C:\\Users\\tospaga\\Desktop\\calisma2.xlsx")
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
s_i, g_i = new_server('localhost', 10000, password='123456789')
s_o, g_o = new_server('localhost', 10001, password='123456789')
index=0
x=[]
y=[]
z=[]
h=[]
a=[]
x1=[]
z1=[]
pre1=0
pre2=0
pre3=0
pre4=0
i=1
while i<(sheet.nrows-1):
    k=int(sheet.cell_value(i,13)*100)
    if k>=68:
        x.append(sheet.cell_value(i,0))
        y.append(sheet.cell_value(i,1))
        z.append(sheet.cell_value(i,2))
        a.append(sheet.cell_value(i,13))
        h.append(k)
    #    print(sheet.cell_value(i, 13))
    i += 1
#print("------", "[i]","-------------","[x]","--------------","[y]","--------------","[z]")
i=0

m=0
while i<len(h):
    if float(h[i])>=m:
            m=float(h[i])
            index=i
    i+=1
x1.append(x[index])
z1.append(z[index])
a=1
flag=0
while 1==1:
    try:
        if flag==0:#initiliazing data
            s_i, g_i = new_server('localhost', 10000, password='123456789')
            s_o, g_o = new_server('localhost', 10001, password='123456789')
            j=0
            k=float(6.15)
            m=float(0.0)
            k1=float(6.15)
            m1=float(0.10)
            k2=float(x1[j])
            m2=float(z1[j])
            point1=g_i.point(k,0,m)
            point2=g_i.point(k1,0,m1)
            point3=g_i.point(k2,0,m2)
            surface_g = g_i.surface(point1,point2,point3)
            line_g=g_i.line((0,0,0),(0,1,0))[-1]
            volume_g=g_i.extrude(surface_g,line_g)
            g_i.delete(line_g)
            g_i.delete(g_i.Point_1)
            g_i.delete(g_i.Point_2)
            g_i.delete(g_i.Point_3)
            g_i.delete(g_i.Point_4)
            g_i.delete(g_i.Point_5)
            g_i.delete(g_i.Polygon_1)
            g_i.Volume_3.Soil.setmaterial(g_i.LooseSoil)
            g_i.combine(g_i.Volume_2,g_i.Volume_3)
            g_i.Volume_4.Soil.setmaterial(g_i.LooseSoil)
            g_i.gotostructures()
            flag=1
            g_i.gotomesh()#mesh
            g_i.mesh(0.01,4)
            g_i.gotostructures()
            g_i.gotostages()
            g_i.calculate()
            g_i.gotostructures()
            pre1=float(k1)
            pre2=float(m1)
            pre3=float(k2)
            pre4=float(m2)
        else:#continious data
            s_o, g_o = new_server('localhost', 10001, password='123456789')
            x1=[]
            z1=[]
            x1.append(pre1)#0
            x1.append(pre3)#1
            z1.append(pre2)#0
            z1.append(pre4)#1
            Hgt = g_o.getresults(g_o.Phases[-1], g_o.ResultTypes.Soil.HydraulicGradientTot, 'node')
            x = g_o.getresults(g_o.Phases[-1], g_o.ResultTypes.Soil.X, 'node')
            z=g_o.getresults(g_o.Phases[-1], g_o.ResultTypes.Soil.Z, 'node')
            i=0
            g1=[]
            m=0
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
            s_i, g_i = new_server('localhost', 10000, password='123456789')
            point1=g_i.point(k,0,m)
            point2=g_i.point(k1,0,m1)
            point3=g_i.point(k2,0,m2)
            surface_g = g_i.surface(point1,point2,point3)
            line_g=g_i.line((0,0,0),(0,1,0))[-1]
            volume_g=g_i.extrude(surface_g,line_g)
            g_i.Volume_2.Soil.setmaterial(g_i.LooseSoil)
            g_i.delete(line_g)
            g_i.delete(g_i.Point_1)
            g_i.delete(g_i.Point_2)
            g_i.delete(g_i.Point_3)
            g_i.delete(g_i.Point_4)
            g_i.delete(g_i.Point_5)
            g_i.delete(g_i.Polygon_1)
            if a==1:
                g_i.combine(g_i.Volume_2,g_i.Volume_4)
                g_i.Volume_3.Soil.setmaterial(g_i.LooseSoil)
                a=2
            else:
                g_i.combine(g_i.Volume_2,g_i.Volume_3)
                g_i.Volume_4.Soil.setmaterial(g_i.LooseSoil)
                a=1
            g_i.gotomesh()#mesh
            g_i.mesh(0.5,4)
            g_i.gotostages()
            g_i.calculate()
            g_i.gotostructures()
            pre1=float(k1)
            pre2=float(m1)
            pre3=float(k2)
            pre4=float(m2)
    except Exception as e:
        print(e)
        sys.exit()

        #analiz
#int("STR"
