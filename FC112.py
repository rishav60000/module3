# 1)
n=int(input('enter value >>'))
i=1
while i<=n:
    a=''
    j=n-i
    while j>0:
        a+=' '
        j-=1
    k=i
    b=''
    while k>=1:
        b+='*'
        k-=1
    print(a,b)    
    i+=1



# 2)
n=int(input('enter value >>'))
i=1
while i<=n:
    a=''
    j=n
    while j>0:
        a+='*'
        j-=1
    print(a)
    n-=1



# 3)
n=int(input('enter value >>'))
i=1
s=1
while i<=n:
    a=''
    j=n-i
    while j>0:
        a+=' '
        j-=1
    p=s
    b=''
    while p>=1:
        b+='*'
        p-=1
    print(a,b)
    s+=2
    i+=1



# 4)
n=int(input('enter value >>'))
i=1
s=1
while i<=n:
    a=''
    j=n-i
    while j>0:
        a+=' '
        j-=1
    p=s
    b=''
    while p>=1:
        b+='*'
        p-=1
    print(a,b)
    s+=2
    i+=1
s=s-2
m=1
j=n-1
while j>=1:
    c=''
    i=1
    while i<=m:
        c+=' '
        i+=1
    m+=1
    d=''
    p=1
    while p<=s-2:
        d+='*'
        p+=1
    s=s-2
    print(c,d)
    j-=1








