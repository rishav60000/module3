n=int(input('enter value >>'))
i=1
max=0
smax=0
while i<=n:
    m=int(input('enter value >>'))
    if m>max:
        smax=max
        max=m
    else:
        if m>smax:
            smax=m
    i+=1
print(smax)