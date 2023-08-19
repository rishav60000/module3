a=[1,2,3,4,5,6,7,8,9,10]
i=1
ev=0
od=0
while i<10:
    if i%2==0:
        if a[i-1]%2==0:
            ev+=a[i-1]
    else:
        if a[i-1]%2==1:
            od+=a[i-1]
    i+=1
print(ev)
print(od)