n=int(input('>>'))
i=1
while i<n:
    count=0
    j=1
    while j<i:
        if i%j==0:
            count+=j
        j+=1
    if count==i:
        print(i)
    i+=1