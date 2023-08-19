n=int(input("Enter day's >>"))
hotday=0
coldday=0
mean1=0
mean2=0
max=0
i=1
while i<=n:
    m1=int(input(' Enter max Temperature >>'))
    m2=int(input(' Enter min Temperature >>'))
    mean1+=m1
    mean2+=m2
    if i==1:
        min=m2
        coldday=i
    if m1>max:
        max=m1
        hotday=i
    if min>m2:
        min=m2
        coldday=i
    i+=1
print('Mean max temp ',mean1/n)
print('Mean min temp ',mean2/n)
print('highest temp ',max)
print('lowest temp ',min)
print('hot temp day ',hotday,'th day')
print('cool temp day',coldday,'th day')