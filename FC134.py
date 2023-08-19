n=int(input('enter value >>'))
i=1
while i<=n:
    c=''
    k=i
    while k>=1:
        c+='*'
        k-=1
    print(c)    
    i+=1
i=1
while i<=n:
    a=''
    j=n
    while j>1:
        a+='*'
        j-=1
    print(a)
    n-=1