# 1). Selection sort
n=[5,7,2,8,3,7,5]
l=7
i=0
while i<l:
    j=0
    while j<l:
        if n[j]>n[i]:
            n[j],n[i]=n[i],n[j]
        j+=1
    i+=1
print(n)



# 2). Insertion sort
n=[5,7,2,8,3,7,5]
l=7
i=0
while i<l:
    j=0
    while j<=i:
        if n[j]>n[i]:
            n[i],n[j]=n[j],n[i]
        j+=1
    i+=1
print(n)



# 3). Bubble sort
n=[5,7,2,8,3,7,5]
i=0
l=7
while i<l:
    j=0
    while j<l-1:
        if n[j]>n[j+1]:
            n[j],n[j+1]=n[j+1],n[j]
        j+=1
    i+=1
print(n)