n=int(input('enter value >>'))
max=0
i=1
while i<=n:
    m=int(input('enter value >>'))
    if i==1:
        min=m
    if m>max:
        max=min
    elif m<min:
        min=m
    i+=1
print(max,min)
