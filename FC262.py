a=[[6,5,4],[7,2,3],[9,1,8]]
n=int(input('Enter value >>'))
i=0
while i<3:
    j=0
    while j<3:
        if a[i][j]==n:
            print([i],[j])
        j+=1
    i+=1