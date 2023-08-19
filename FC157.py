a=int(input('>>'))
b=int(input('>>'))
count=0
i=1
while (i**2)<=b:
    if (i**2)>=a:
        count+=1
    i+=1
print(count)