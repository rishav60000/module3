n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
m=int(input('enter term >>'))
i=0
while i<m:
    j=i+1
    while j<20:
        n[i],n[j]=n[j],n[i]
        j+=1
    i+=1
print(n)