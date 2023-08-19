a=int(input('>>'))
b=int(input('>>'))
if a<b:
    a,b=b,a
hcf=0
i=1
while i<b:
    if b%i==0:
        if a%i==0:
            hcf=i
    i+=1
lcm=(a*b)//hcf
print('Hcf =',hcf,'\nLcm =',lcm)

