a=[1,2,3,4,5,6,7]
b=[2,4,6,8,10,12]
c=a+b
i=0
while i<13:
    j=i+1
    while j<13:
        if c[j]<c[i]:
            c[i],c[j]=c[j],c[i]
        j+=1
    i+=1
print(c)
