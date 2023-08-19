a=[11,7,11,18,9,7,6,23,7]
i=0
b=9
while i<b:
    j=0
    while j<i:
        if a[j]>a[i]:
            a[i],a[j]=a[j],a[i]
        j+=1
    i+=1
print(a)
i=0
num=0
sum=0
m=0
while i<b:
    sum+=a[i]
    count=0
    j=i+1
    while j<b:
        if a[i]==a[j]:
            count+=1
        j+=1
    if count>=m:
        m=count
        num=a[i]
    i+=1
if b%2==0:
    x=b//2
    f=a[x]+a[(x-1)]/2
else:
    f=a[(b//2)]
print('mean =',sum//b)
print('median =',f)
print('mode =',num)