n=5
x=[0]*(n+1)
i,a,b,c=0,0,1,0
while i<=n:
    x[i]=c
    a=b
    b=c
    c=a+b
    i+=1
print(x)
z=6
m=z//2
k=0
while k<m:
    x[k],x[z-k-1]=x[z-k-1],x[k]
    k+=1
a=[0]*2
for i in range(6):
    if x[i]<=n:
        if x[i]>0:
            n=n-x[i]
            a[i]=x[i]
print(a)
