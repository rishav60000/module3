n=int(input("No of beby's >>"))
sum=0
count=0
max=0
b=[0]*n
p=0
i=1
while i<=n:
    m=int(input('Enter Waigth of baby >>'))
    b[p]=m
    sum+=m
    count+=1
    if i==1:
        min=m
    if m>max:
        max=m
        if max<min:
            min=max
    else:
        if min>m:
            min=m
    i+=1
    p+=1
print('Mean =',sum/count)
print('Max =',max)
print('Min =',min)