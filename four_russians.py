import csv
import sys
name1=sys.argv[1]
#print(len(sys.argv))
if len(sys.argv)>2:
    name2=sys.argv[2]

def log2(x):
    guard=True
    k=0
    while guard:
        if 2**(k)>=x: 
            guard=False
        else:
            k=k+1
    return k

def inittable(rows,columns,table= []):
    zeros=[]
    for count in range(columns):
        zeros.append(0)
    for count in range(rows):
        table.append(zeros.copy())
    return table

def checkrows(table,rowsnum,check,n):
    zeros=[]
    for i in range(n):
        zeros.append(0)
    while check>rowsnum:
        table.append(zeros.copy())
        rowsnum=rowsnum+1
    if n==5:
        table.append(zeros.copy())
    return table

def Rowfrombottom(list1,a):
    c=len(list1)
    #print("a(k+1)=",a)
    line=list1[c-a]
    #print(line)
    return line 

def getBi(B,i,m):
    #print("i*3=",i*3)
    Bi=B[(i-1)*m:(i-1)*m+m]
    #print("i=",i)
    #print("Bi",Bi)
    return Bi

def converttoint(lista):
    for u in range(len(lista)):
        if lista[u]=='1' or lista[u]==1:
            lista[u]=1
        else:
            lista[u]=0
    return(lista)    



def modifyrs(j,k,i,m,rs1,n):
    t=0
    Bi=getBi(B,i,m)
    #print("Bi=",Bi)
    l=Rowfrombottom(Bi,k+1)
    l=converttoint(l)
    #print("l=",l)
    #print(rs1[0])
    #print("l=",l)
    #print("rs1[j-(2**k)]=",rs1[j-(2**k)])
    #print("j=",j)
    #print("rs1=",rs1)
    rs1[j]=[sum(x) for x in zip(l, rs1[j-(2**k)])]
    #print("rs1=",rs1)
    for r in range(len(rs1)):
        for t in range(n):
           #print(r)
            #print(t)
            #print(rs1)
            if rs1[r][t]>1:
                rs1[r][t]=1
    #print("AFTER",rs1)
    #print("k=",k)
    #print("k+1=",k+1)
    #print("l=",l)

def GetAi(Ai,n,u,A,m):
    #print("Ai at start is",Ai)
    #print("n=",n)
    #print("m=",m)
    #print("u=",u)
    if u <(2**m):
        for j in range(n):
            counter2=0
            t=0
            for i in range(u,u+m):   
               # print("i=",i)
                #print("j=",j)   
                p=int(A[i][j])
                #print(A)
                #print("A[i][j]=",A[i][j])
                #print("counter2=",counter2)
                if p==1:
                    if t==0:
                        t=t+1
                        #print("Ai=",Ai)
                        Ai[counter2][j]=(t*p)
                else:
                    Ai[counter2][j]=0
                counter2=counter2+1    
        #print("Ai=",Ai)
        return Ai

def GetSum(Ai,n,m):
    #print(Ai)
    F=[]
    S=inittable(1,n,F)
    for x in range(n):
        for y in range(len(Ai)):
            if Ai[y][x]==1:
                S[0][x]=S[0][x]+(2**(m-(1+y)))
    return S
                

def tablemult(A,B):
    #print(A)
    #print("BLA")
    n=len(A)
    m=int(log2(n))
    if n==5:
        m=m-1
    #print("Lenght of A is=",n)
    #print("Log(2)13 is",m)
    o=int(2**m)
    #print("2 to log13 is ",o)
    u=0
    F=[]
    C=inittable(n,n,F)
    varend=(n/m)
    checktab=(m)**2
    #print(varend)
    D=zip(*A)
    A=(list(D))
    B=checkrows(B,n,checktab,n)
    A=checkrows(A,n,checktab,n)
    #print("B=",B)
    #print("A(Swapped)=",A)
    F=[]
    for counter1 in range(1,int(varend)+2):
        #print("counter1=",counter1)
        F=[]
        d=0
        F=[]
        rs1=inittable(o,n,F)
        #print(len(rs1))
        bp=1
        k=0
        for j in range(1,2**m):
            modifyrs(j,k,counter1,m,rs1,n)
            if bp==1:
                bp=j+1
                k=k+1
            else:
                bp=bp-1
        #print(rs1)
        F=[]
        Ci=inittable(n,n,F)
        #print(Ci)
        #for counter in range(n):
        List=[]
        F=[]
        Ai=inittable(m,n,F)
        List=GetAi(Ai,n,u,A,m)
        u=u+m
        #print(List)
        Sum=GetSum(List,n,m)
        #print("Sum=",Sum)
        for counter3 in range(n):
            Ci[counter3]=rs1[Sum[0][counter3]]
        #print("Ci=",Ci)
        #print(len(Ci))
        del Ai[:]    
        for j in range(len(Ci)):
            for z in range(len(Ci)):
                if Ci[j][z]==1:
                    C[j][z]=1    
        #print("rs1=",rs1)
        del rs1[:]
        del F[:]
    return(C)    

if len(sys.argv)>2:
    A = []
    with open(name1, newline='') as inputfile:
        for row in csv.reader(inputfile):
            A.append(row)
    B = []
    with open(name2, newline='') as inputfile:
        for row in csv.reader(inputfile):
            B.append(row)
    inputfile.close()
    D=tablemult(A,B)
    for i in range(len(D)):
            print(D[i])  
    
else:
    A = []
    with open(name1, newline='') as inputfile:
        for row in csv.reader(inputfile):
            A.append(row)
    #print(A)
    inputfile.close()
    n=len(A)
    F=[]
    links=inittable(n,n,F)
    for i in range(n):
        x=A[i]
        c,d=x[0].split(' ')
        a=int(c)
        b=int(d)
        for j in range(n):
            if (i==j) or (i==a and j==b):
                links[i][j]=1    
    print(links)
    B=links[:]
    for k in range(len(links)):
        if k==0:
            D=tablemult(links,B)
        else:
            D=tablemult(D,links)
    for i in range(len(D)):
            print(D[i])
    #(Σπάμε τo D σε D[i][j] και πέρνουμε τα i,j και τα κάνουμε print)        




