m=int(input('enter number >>'))
n=m
count=0
while m>0:
    a=m%10
    count+=1
    m=m//10
i=1
num=0
count=(count//2)+1
while i<=count:
    a=n%(10)
    b=n%(100)
    b=b//10
    n=n//10
    if a-b==1:
        num+=1
    elif b-a==1:
        num+=1
    i+=1
if num==count:
    print('True')
else:
    print('False')