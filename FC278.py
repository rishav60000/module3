a=list(input('Enter String >>'))
b=list(input('Enter string >>'))
n=0
for p in a:
    n+=1
m=0
for q in b:
    m+=1
count=0
i=0
while i<n:
    j=0
    while j<m:
        if n==m:
            if a[i]==b[j]:
                count+=1
        j+=1
    i+=1
if count==n:
    print('Anagram')
else:
    print('Not Anagram')