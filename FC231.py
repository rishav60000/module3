a=[3,6,7,5,10]
i=0
k=3
l=5
gap=0
while i<l:
    if gap==k:
        if a[i]>0:
            print(a[i])
            a[i]=-1
            gap=0
        
    else:
        gap+=1
    i=(i+1)%l
