m=int(input('Enter number >>'))
n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
i=2
count=0
while i<=m:
    j=0
    k=1
    count=i
    while j<20:
        if n[j]>0:
            if count!=k:
                k+=1
            else:
                n[j]=-1
                k=1
            j+=1
        else:
            j+=1
    i+=1
a=[0]*5
J=0
for i in n:
    if i>0:
        a[J]=i
        J+=1
print(a)