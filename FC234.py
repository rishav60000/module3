a=[3,6,7,5,10]
b=[0]*1
C=0
k=12
i=0
while i<len(a)-1:
    j=i+1
    if a[i]+a[j]==12:
        b[C]=a[i],a[j]
        C+=1
    i+=1
print(b)