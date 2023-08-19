n=int(input('Enter number >>'))
i=0
a=[0]*n
while i<n:
    b=[0]*n
    j=0
    while j<n:
        b[j]=0
        j+=1
    a[i]=b
    i+=1
i=0
low=0
high=n-1
b=1
count=(n+1)//2
while i<count:
    j=low
    while j<=high:
        a[low][j]=b
        j+=1
        b+=1
    j=low+1
    while j<=high:
        a[j][high]=b
        j+=1
        b+=1
    j=high-1
    while j>=low:
        a[high][j]=b
        b+=1
        j-=1
    j=high-1
    while j>low:
        a[j][low]=b
        b+=1
        j-=1
    low=low+1
    high=high-1
    i+=1
for i in a:
    print(i)