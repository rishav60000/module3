n=int(input('enter value >>'))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("It's prime number")
else:
    print("It's not prime number")