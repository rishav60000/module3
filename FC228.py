n=int(input('Enter number >>'))
ro=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','III','II','I']
de=[1000,900,500,400,100,90,50,40,10,9,5,4,3,2,1]
row=''
i=0
while i<15:
    m=n//de[i]
    j=0
    while j<m:
        row+=ro[i]
        n=n%de[i]
        j+=1
    i+=1
print(row)
