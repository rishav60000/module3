# (1)
x=int(input('enter the value of x >>'))
n=int(input('enter the value of n >> '))
i=1
sum=0
while i<=n:
    sum+=((x**i)/i)
    i+=1
print(sum)



# (2)
x=int(input('enter the value of x >>'))
n=int(input('enter the value of n >> '))
i=1
j=1
sum=0
while i<=n:
    if i%2!=0:
        sum+=((x**j)/j)
    else:
        sum-=((x**j)/j)
    i+=1
    j+=2
print(sum)



# (3)
x=int(input('enter the value of x >>'))
n=int(input('enter the value of n >> '))
i=1
j=1
sum=0
while i<=n:
    k=j
    m=1
    while k>=1:
        m*=k
        k-=1
    if i%2!=0:
        sum+=((x**j)/m)
    else:
        sum-=((x**j)/m)
    i+=1
    j+=2
print(sum)