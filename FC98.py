p=int(input('>>'))
q=int(input('>>'))
sum=0
for i in range(p,q):
    if i%p==0:
        if i%q!=0:
            sum+=i
print(sum)