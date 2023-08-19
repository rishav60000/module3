n=int(input('enter decimal number >>'))
s=' '
while n>0:
    a=n%2
    n=(n//2)
    s=str(a)+s
print(s)