n=int(input('enter number >>'))
sum=0
while n>0:
    a=n%10
    sum+=a
    n=n//10
    if n==0 and sum>10:
        n=sum
        sum=0
print(sum)