a=[1,2,3,4,5,6,7]
c=0
n=int(input('enter the number >>'))
for i in a:
    if i==n:
        c+=1
if c>0:
    print('Yes')
else:
    print('No')