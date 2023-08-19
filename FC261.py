a=[[6,5,4],[7,5,3],[9,6,8]]
min=a[0][0]
i=0
while i<3:
    j=0
    while j<3:
        if a[i][j]<min:
            min=a[i][j]
        j+=1
    i+=1
print(min) 
