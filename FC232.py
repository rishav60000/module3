a = [11, 7, 11, 18, 9, 7, 9, 23, 7]
b = [0]*3
C=0
i = 0
while i < 9:
    count = 0
    j = i + 1
    while j < 9:
        if a[i] > 0:
            if a[i] == a[j]:
                count += 1
                a[j] =- 1
        j += 1
    if count > 0:
        b[C]=a[i]
        C+=1
    i += 1
print(b)
