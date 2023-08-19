n=int(input('enter value >>'))
i=1
while i<=n:
    if n%i==0:
        count=0
        j=1
        while j<=i:
            if i%j==0:
                count+=1
            j+=1
        if count==2:
            print(i)
    i+=1