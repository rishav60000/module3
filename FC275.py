m=int(input('enter number >>'))
n=m
count=0
b=0
while m>0:
    a=m%10
    b=(b*10)+a
    count+=1
    m=m//10
co=0
num=0
i=1
while i<=n:
    if n%i==0:
        co+=1
    i+=1
j=1
while j<=b:
    if b%j==0:
        num+=1
    j+=1
if num+co==4:
    print('Twisted prime ')
else:
    print('Not Twisted prime')