n=int(input('enter value >>'))
i=1
f=0
sum=0
while i<=n: 
    j=1
    count=0
    while i>=j:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        sum+=i
    i+=1
print(sum)