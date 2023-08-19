a=list(input('Enter string >>'))
b=list(input('Enter string >>'))
n=0
for p in a:
    n+=1
m=0
for q in b:
    m+=1
c=''
k=0
while k<2:
    i=0
    while i<n:
        count=0
        j=0
        while j<m:
            if a[i]==b[j]:
                count+=1
            j+=1
        if count==0:
            c+=a[i]
        i+=1
    k+=1
    a,b=b,a       
    i+=1
print(c)