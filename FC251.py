a=[[4,5],[6,7]]
b=[[1,2],[3,8]]
c=[[0,0],[0,0]]
i=0
while i<len(a):
    j=0
    while j<len(b):
        c[i][j]=a[i][j]+b[j][i]
        j+=1
    i+=1
for i in c:
    print(i)