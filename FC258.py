a=[[1,0,0],[0,1,0],[0,0,1]]
count=0
num=0
i=0
while i<3:
    j=0
    while j<3:
        if i==j:
            if a[i][j]!=0:
                count+=1
        else:
            if a[i][j]!=0:
                num+=1
        j+=1
    i+=1
if num==0:
    if  count==3:
        print('Diagonal')
else:
    print('Not Diagonal')
