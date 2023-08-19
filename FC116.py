n=int(input('enter value >>'))
i=1
max=0
smax=0
tmax=0
while i<=n:
    m=int(input('enter value >>'))
    if m>max:
        tmax=smax
        smax=max
        max=m
    elif m>smax:
        tmax=smax
        smax=m
    else:
        tmax=m
    i+=1
print(tmax)
