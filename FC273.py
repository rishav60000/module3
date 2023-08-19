n=12
a=[]
i=1
while i<=n:
    b=[]
    j=1
    p=0
    while j<=i:
        if i%j==0:
            b+=[j]
        j+=1

    for k in b:
        if n%k==0:
            p+=1
    if p==1:
        a+=b
    i+=1        
c=[]
for k in a:
    if type(k)==list:
        for n in k:
            c+=(n)
    else:
        c+=[k]
k=[]
i=0
while i<7:
    j=i+1
    while j<7:
        if c[i]>0:
            if c[i]==c[j]:
                c[j]=-1
        j+=1
    i+=1
for i in c:
    if i>0:
        k+=[i]
print(k)
