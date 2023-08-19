n=int(input('enter  binary number >>'))
m=n
count=0
while n>0:
    a=n%10
    count+=1
    n=n//10
i=0
sum=0
while i<=count:
    a=(m%10)
    if a!=0:
        a=2**i
        sum+=a
    m=m//10
    i+=1
print(sum)