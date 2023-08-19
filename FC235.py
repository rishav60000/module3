d=[6,4,9,2,4,8,16,11]
c=[1,3,5,8,11,9,6,17]
e=[0]*8
f=[0]*8
t=0
i = 0
while i < 8:
    count = 0
    j = 0
    while j < 8:
        if c[j] > 0:
            if d[i] == c[j]:
                count+=1
                c[j] =- 1   
        j += 1
    if count > 0:
        e[t]=d[i]
        t+=1
    i += 1
print(e)
f=d+c
d=[0]*16
i=0
while i<15:
    j=i+1
    while j<16:
        if f[i]>0:
            if f[i]==f[j]:
                f[j]=-1
            d[i]=f[i]
        j+=1
    i+=1
print(d)
