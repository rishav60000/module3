a=[1,2,3,4,5]
b=[4,5,6,7,8,9]
c=a+b
d=6
i=0
while i<d:
    j=i+1
    while j<d:
        if c[j]<c[i]:
            c[i],c[j]=c[j],c[i]
        j+=1
    i+=1
p=d//2
if d%2==0:
    print((p+(p-1))/2)
else:
    print(p)