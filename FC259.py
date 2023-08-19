a=[[1,0,0],[0,1,0],[0,0,1]]
sum=0
i=0
while i<3:
    j=0
    while j<3:
        if i==j:
            sum+=a[i][j]
        j+=1
    i+=1
print(sum)