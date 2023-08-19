
# 1)
n= int(input('enter value >>'))
i=1
while i<=n:
    a=''
    j=1
    while j<=n:
        if (i==1):
            a+='*'
            if i==n:
                a+='*'
        elif i==n:
            a+='*'
        else:
            if j==1:
                a+='*'
            elif j==n:
                a+='*'
            else:
                a+=' '
        j+=1
    i+=1
    print(a)



# 2)
n=int(input('enter value >>'))
i=1
while i<=n:
    j=1
    a=''
    while j<=i:
        if (i<3):
            a+='*'
        if i==n:
            a+='*'
        if i<n:
            if i>2:
                if j==1:
                    a+='*'
                elif i==j:
                    a+='*'
                else:
                    a+=' '
        j+=1
    print(a)
    i+=1