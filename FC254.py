a=[[4,5],[6,7]]
b=[[0,0],[0,0]]
for i in a:
    print(i)
i=0
while i<2:
    j=0
    while j<2:
        b[i][j]=a[j][i]
        j+=1
    i+=1
for i in b:
    print(i)