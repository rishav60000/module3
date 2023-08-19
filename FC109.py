n=int(input('enter the value of n >>'))
i=1
sum=0
while i<=n:
    m=1
    j=i
    while j>=1:
        m*=j
        j-=1
    sum+=m
    i+=1
print(sum)