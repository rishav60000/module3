sum1=0
sum2=0
sum3=0
a=[[8,1,6],[3,5,7],[4,9,2]]
i=0
while i<3:
    j=0
    while j<3:
        if i==j:
            sum1+=a[i][j]
        else:
            sum2+=a[i][j]
            sum3+=a[j][i]
        j+=1
    i+=1
C=0
if sum1==sum2//2:
    C+=1
if sum1==sum3//2:
    C+=1
if sum2//2==sum3//2:
    C+=1
if C==3:
    print('Magic square')
else:
    print('Not magic square')