a=[1,2,3,3,5,3,5,5,6,7]
b=[0]*2
i=0
c=0
while i<10:
    count=0
    j=i+1
    while j<10:
        if a[j]>0:
            if a[i]>0:
                if a[i]==a[j]:
                    count+=1
                    a[j]=-1
        j+=1
    if count>=1:
        b[c]=a[i]
        c+=1
    i+=1
print(b)
