# Q1. FC90
# n=int(input('>>'))
# i=0
# sum=0
# while 0<n:
#     sum+=n
#     n-=1
# print(sum)


# Q2.FC135
# n=int(input('>>'))
# i=0
# sum=1
# while 0<n:
#     sum*=n
#     n-=1
# print(sum)


# Q3.FC98
# p=int(input('>>'))
# q=int(input('>>'))
# sum=0
# for i in range(p,q):
#     if i%p==0 and i%q!=0:
#         sum+=i
# print(sum)


# Q4.FC157
# a=int(input('>>'))
# b=int(input('>>'))
# count=0
# i=1
# while (i**2)<=b:
#     if (i**2)>=a:
#         count+=1
#     i+=1
# print(count)


# Q5.FC129
# n=int(input('>>'))
# for i in range(n):
#     a=int(input('>>'))
#     print(a)


# Q6.FC100
# n=int(input('>>'))
# sum=0
# while n>0:
#     a=n%10
#     sum+=a
#     n=n//10
# print(sum)


# Q6.FC92
# sum=0
# count=0
# i=2
# while sum<=1000:
#     sum=sum+i
#     b=i
#     count+=1
#     i+=2
# print(sum-b)
# print(count-1)


# Q7.FC101
# n=int(input('>>'))
# count=0
# b=0
# while n>0:
#     a=n%10
#     b=(b*10)+a
#     n=n//10
# print(b)


# Q7.FC102
# n=int(input('>>'))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i+=1


# Q8.FC103
# n=int(input('>>'))
# i=1
# sum=0
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print('Perfect number')
# else:
#     print('Not perfect number')


# Q9.FC108
# n=int(input('>>'))
# i=1
# while i<n:
#     count=0
#     j=1
#     while j<i:
#         if i%j==0:
#             count+=j
#         j+=1
#     if count==i:
#         print(i)
#     i+=1


# Q10.FC99  
# a=int(input('>>'))
# b=int(input('>>'))
# if a<b:
#     a,b=b,a
# hcf=0
# i=1
# while i<b:
#     if b%i==0:
#         if a%i==0:
#             hcf=i
#     i+=1
# lcm=(a*b)//hcf
# print('Hcf =',hcf,'\nLcm =',lcm)


# Q11.FC113
# num=int(input('>>'))
# b=[]
# n=0
# for i in range(num):
#     a=int(input('>>'))
#     b.append(a)
#     n+=1
# hcf=0
# c=min(b)
# for x in range(1,c+1):
#     count=0
#     for y in b:
#         if y%x==0:
#             count+=1 
#     if count==n:
#         hcf=x
# print(hcf)


# Q12.FC105

# (1)
# x=int(input('enter the value of x >>'))
# n=int(input('enter the value of n >> '))
# i=1
# sum=0
# while i<=n:
#     sum+=((x**i)/i)
#     i+=1
# print(sum)


# (2)
# x=int(input('enter the value of x >>'))
# n=int(input('enter the value of n >> '))
# i=1
# j=1
# sum=0
# while i<=n:
#     if i%2!=0:
#         sum+=((x**j)/j)
#     else:
#         sum-=((x**j)/j)
#     i+=1
#     j+=2
# print(sum)

# (3)
# x=int(input('enter the value of x >>'))
# n=int(input('enter the value of n >> '))
# i=1
# j=1
# sum=0
# while i<=n:
#     k=j
#     m=1
#     while k>=1:
#         m*=k
#         k-=1
#     if i%2!=0:
#         sum+=((x**j)/m)
#     else:
#         sum-=((x**j)/m)
#     i+=1
#     j+=2
# print(sum)


# Q13.FC109
# n=int(input('enter the value of n >>'))
# i=1
# sum=0
# while i<=n:
#     m=1
#     j=i
#     while j>=1:
#         m*=j
#         j-=1
#     sum+=m
#     i+=1
# print(sum)


# Q14.FC112
# n=int(input('enter value >>'))
# i=1
# while i<=n:
#     j=n-i
#     while j>0:
#         print(' ',end='')
#         j-=1
#     k=i
#     while k>=1:
#         print('*',end='')
#         k-=1
#     print()    
#     i+=1


# Q15.FC112
# n=int(input('enter value >>'))
# i=1
# while i<=n:
#     j=n
#     while j>0:
#         print('*',end='')
#         j-=1
#     print()
#     n-=1



# Q16.FC112
# n=int(input('enter value >>'))
# i=1
# s=1
# while i<=n:
#     j=n-i
#     while j>0:
#         print(' ',end='')
#         j-=1
#     p=s
#     while p>=1:
#         print('*',end='')
#         p-=1
#     print()
#     s+=2
#     i+=1




# Q17.FC112
# n=int(input('enter value >>'))
# i=1
# s=1
# while i<=n:
#     j=n-i
#     while j>0:
#         print(' ',end='')
#         j-=1
#     p=s
#     while p>=1:
#         print('*',end='')
#         p-=1
#     print()
#     s+=2
#     i+=1
# s=s-2
# m=1
# j=n-1
# while j>=1:
#     i=1
#     while i<=m:
#         print(' ',end='')
#         i+=1
#     m+=1
#     p=1
#     while p<=s-2:
#         print('*',end='')
#         p+=1
#     s=s-2
#     print()
#     j-=1
        


# Q18.FC134
# n=int(input('enter value >>'))
# i=1
# while i<=n:
#     j=n-i
#     while j>0:
#         print('',end='')
#         j-=1
#     k=i
#     while k>=1:
#         print('*',end='')
#         k-=1
#     print()    
#     i+=1
# i=1
# while i<=n:
#     j=n
#     while j>1:
#         print('*',end='')
#         j-=1
#     print()
#     n-=1


# Q19.FC155
# n= int(input('enter value >>'))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         if (i==1 or i==n) or (j==1 or j==n):
#             print('*',end='')
#         else:
#             print(' ',end='')
#         j+=1
#     print()
#     i+=1



# Q20.FC155
# n=int(input('enter value >>'))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if (i==1 or i==5) or (j==1 or j==i):
#             print('*',end='')
#         else:
#             print(' ',end='')
#         j+=1
#     print()
#     i+=1



# Q21.FC111
# n=int(input('enter value >>'))
# i=1
# s=n-1
# while i<=n:
#     m=10**i
#     j=m//9
#     k=j**2
#     print(''*s,k)
#     s-=1
#     i+=1


# Q22.FC114
# n=int(input('enter value >>'))
# max=0
# i=1
# while i<=n:
#     m=int(input('enter value >>'))
#     if i==1:
#         min=m
#     if m>max:
#         max=min
#     elif m<min:
#         min=m
#     i+=1
# print(max,min)



# Q22.FC115
# n=int(input('enter value >>'))
# i=1
# max=0
# smax=0
# while i<=n:
#     m=int(input('enter value >>'))
#     if m>max:
#         smax=max
#         max=m
#     else:
#         if m>smax:
#             smax=m
#     i+=1
# print(smax)




# Q23.FC116
# n=int(input('enter value >>'))
# i=1
# max=0
# smax=0
# tmax=0
# while i<=n:
#     m=int(input('enter value >>'))
#     if m>max:
#         tmax=smax
#         smax=max
#         max=m
#     elif m>smax:
#         tmax=smax
#         smax=m
#     else:
#         tmax=m
#     i+=1
# print(tmax)




# Q24.FC104
# n=int(input('enter value >>'))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("It's prime number")
# else:
#     print("It's not prime number")



# Q25.FC117
# n=int(input('enter value >>'))
# i=1
# f=0
# while i>0 and f!=n:
#     j=1
#     count=0
#     while i>=j:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         f+=1
#         print(i)
#     i+=1



# Q26.FC118
# n=int(input('enter value >>'))
# i=1
# f=0
# sum=0
# while i<=n: 
#     j=1
#     count=0
#     while i>=j:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         sum+=i
#     i+=1
# print(sum)




# Q27.FC119
# n=int(input('enter value >>'))
# i=1
# while i<=n:
#     if n%i==0:
#         count=0
#         j=1
#         while j<=i:
#             if i%j==0:
#                 count+=1
#             j+=1
#         if count==2:
#             print(i)
#     i+=1


# Q28.FC120
# n=int(input('enter value >>'))
# i=0
# a=0
# c=0
# b=1
# while i<n-1:
#     if i<=1:
#         c=i
#     else:
#         c=a+b
#         a=b
#         b=c
#     print(c)
#     i+=1


# Q29.FC265
# n=int(input('enter  binary number >>'))
# m=n
# count=0
# while n>0:
#     a=n%10
#     count+=1
#     n=n//10
# i=0
# sum=0
# while i<=count:
#     a=(m%10)
#     if a!=0:
#         a=2**i
#         sum+=a
#     m=m//10
#     i+=1
# print(sum)



# Q30.FC266
# n=int(input('enter decimal number >>'))
# s=' '
# while n>0:
#     a=n%2
#     n=(n//2)
#     s=str(a)+s
# print(s)


# Q31.FC267
# n=int(input('enter number >>'))
# sum=0
# while n>0:
#     a=n%10
#     sum+=a
#     n=n//10
#     if n==0 and sum>10:
#         n=sum
#         sum=0
# print(sum)


# Q32.FC270
# m=int(input('enter number >>'))
# n=m
# count=0
# while m>0:
#     a=m%10
#     count+=1
#     m=m//10
# i=1
# num=0
# count=(count//2)+1
# while i<=count:
#     a=n%(10)
#     b=n%(100)
#     b=b//10
#     n=n//10
#     if a-b==1 or b-a==1:
#         num+=1
#     i+=1
# if num==count:
#     print('True')
# else:
#     print('False')

    

# Q33.FC275
# m=int(input('enter number >>'))
# n=m
# count=0
# b=0
# while m>0:
#     a=m%10
#     b=(b*10)+a
#     count+=1
#     m=m//10
# co=0
# num=0
# i=1
# while i<=n:
#     if n%i==0:
#         co+=1
#     i+=1
# j=1
# while j<=b:
#     if b%j==0:
#         num+=1
#     j+=1
# if num+co==4:
#     print('Twisted prime ')
# else:
#     print('Not Twisted prime')
    






# [LIST]


# Q34.FC203
# a=[1,2,3,4,5,6,7]
# c=0
# n=int(input('enter the number >>'))
# for i in a:
#     if i==n:
#         c+=1
# if c>0:
#     print('Yes')
# else:
#     print('No')



# Q35.FC206
# a=[1,2,3,3,5,3,5,5,6,7]
# c=0
# n=int(input('enter the number >>'))
# for i in a:
#     if i==n:
#         c+=1
# print(c)



# Q36.FC208
# a=[1,2,3,3,5,3,5,5,6,7]
# b=[]
# i=0
# while i<len(a):
#     count=0
#     j=i+1
#     while j<len(a):
#         if a[j]>0 and a[i]>0:
#             if a[i]==a[j]:
#                 count+=1
#                 a[j]=-1
#         j+=1
#     if count>=1:
#         b+=[a[i]]
#     i+=1
# print(b)



# Q37.FC217
# a=[1,2,3,4,5,6,7,8,9,10]
# i=1
# ev=0
# od=0
# while i<=len(a):
#     if i%2==0:
#         if a[i-1]%2==0:
#             ev+=a[i-1]
#     else:
#         if a[i-1]%2==1:
#             od+=a[i-1]
#     i+=1
# print(ev)
# print(od)



# Q38.FC223
# n=int(input("No of beby's >>"))
# sum=0
# count=0
# max=0
# b=[]
# i=1
# while i<=n:
#     m=int(input('Enter Waigth of baby >>'))
#     b.append(m)
#     sum+=m
#     count+=1
#     if i==1:
#         min=m
#     if m>max:
#         max=m
#         if max<min:
#             min=max
#     else:
#         if min>m:
#             min=m
#     i+=1
# print('Mean =',sum/count)
# print('Max =',max)
# print('Min =',min)


# Q39.FC224
# n=int(input("Enter day's >>"))
# hotday=0
# coldday=0
# mean1=0
# mean2=0
# max=0
# i=1
# while i<=n:
#     m1=int(input(' Enter max Temperature >>'))
#     m2=int(input(' Enter min Temperature >>'))
#     mean1+=m1
#     mean2+=m2
#     if i==1:
#         min=m2
#         coldday=i
#     if m1>max:
#         max=m1
#         hotday=i
#     if min>m2:
#         min=m2
#         coldday=i
#     i+=1
# print('Mean max temp ',mean1/n)
# print('Mean min temp ',mean2/n)
# print('highest temp ',max)
# print('lowest temp ',min)
# print('hot temp day ',hotday,'th day')
# print('cool temp day',coldday,'th day')



# Q40.FC228
# n=int(input('Enter number >>'))
# ro=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','III','II','I']
# de=[1000,900,500,400,100,90,50,40,10,9,5,4,3,2,1]
# row=''
# i=0
# while i<len(ro):
#     m=n//de[i]
#     j=0
#     while j<m:
#         row+=ro[i]
#         n=n%de[i]
#         j+=1
#     i+=1
# print(row)


# Q41.FC229
# a=[1,2,3,4,5,6,7,8,9,10]
# print(a)
# b=len(a)
# c=b//2
# i=0
# while i<c:
#     a[i],a[b-i-1]=a[b-i-1],a[i]
#     i+=1
# print(a)


# Q42.FC230
# a=[11,7,11,18,9,7,6,23,7]
# i=0
# b=len(a)
# while i<b:
#     j=0
#     while j<i:
#         if a[j]>a[i]:
#             a[i],a[j]=a[j],a[i]
#         j+=1
#     i+=1
# print(a)
# i=0
# num=0
# sum=0
# m=0
# while i<b:
#     sum+=a[i]
#     count=0
#     j=i+1
#     while j<b:
#         if a[i]==a[j]:
#             count+=1
#         j+=1
#     if count>=m:
#         m=count
#         num=a[i]
#     i+=1
# if b%2==0:
#     x=b//2
#     f=a[x]+a[(x-1)]/2
# else:
#     f=a[(b//2)]
# print('mean =',sum//b)
# print('median =',f)
# print('mode =',num)



# Q43.FC231
# a=[3,6,7,5,10]
# i=0
# k=3
# l=len(a)
# gap=0
# while i<l:
#     if gap==k:
#         if a[i]>0:
#             print(a[i])
#             a[i]=-1
#             gap=0
        
#     else:
#         gap+=1
#     i=(i+1)%l




# Q44.FC232
# a = [11, 7, 11, 18, 9, 7, 9, 23, 7]
# b = []
# i = 0
# while i < len(a):
#     count = 0
#     j = i + 1
#     while j < len(a):
#         if a[i] > 0:
#             if a[i] == a[j]:
#                 count += 1
#                 a[j] =- 1
#         j += 1
#     if count > 0:
#         b.append(a[i])
#     i += 1
# print(b)


# Q45.FC233
# a=[1,2,3,4,5,6,7]
# b=[2,4,6,8,10,12]
# c=a+b
# i=0
# while i<len(c):
#     j=i+1
#     while j<len(c):
#         if c[j]<c[i]:
#             c[i],c[j]=c[j],c[i]
#         j+=1
#     i+=1
# print(c)



# Q46.FC234
# a=[3,6,7,5,10]
# b=[]
# k=12
# i=0
# while i<len(a)-1:
#     j=i+1
#     if a[i]+a[j]==12:
#         b+=a[i],a[j]
#     i+=1
# print(b)



# Q47.FC235
# d=[6,4,9,2,4,8,16,11]
# c=[1,3,5,8,11,9,6,17]
# e=[]
# f=[]
# i = 0
# while i < len(d):
#     count = 0
#     j = 0
#     while j < len(c):
#         if c[j] > 0:
#             if d[i] == c[j]:
#                 count+=1
#                 c[j] =- 1   
#         j += 1
#     if count > 0:
#         e.append(d[i])
#     else:
#         f.append(d[i])
#     i += 1
# print(e)



# Q48.FC236
# a=[1,2,3,4,5]
# b=[4,5,6,7,8,9]
# c=a+b
# d=len(c)
# i=0
# while i<d:
#     j=i+1
#     while j<d:
#         if c[j]<c[i]:
#             c[i],c[j]=c[j],c[i]
#         j+=1
#     i+=1
# p=d//2
# if d%2==0:
#     print((p+(p-1))/2)
# else:
#     print(p)



# Q49.FC237
# n=[1,2,3,4,5,6,7,9,10]
# r=len(n)-1
# key=12
# l=0
# flag=0
# while l<=r and flag==0:
#     m=(l+r)//2
#     if n[m]==key:
#         flag+=1
#     elif n[m]>key:
#         r=m-1
#     else:
#         l=m+1
# if flag>0:
#     print('Exist')
# else:
#     print('Not exist')



# Q50.FC238
#1). Selection sort
# n=[5,7,2,8,3,7,5]
# l=len(n)
# i=0
# while i<l:
#     j=0
#     while j<l:
#         if n[j]>n[i]:
#             n[j],n[i]=n[i],n[j]
#         j+=1
#     i+=1
# print(n)

#2). Insertion sort
# n=[5,7,2,8,3,7,5]
# l=len(n)
# i=0
# while i<l:
#     j=0
#     while j<=i:
#         if n[j]>n[i]:
#             n[i],n[j]=n[j],n[i]
#         j+=1
#     i+=1
# print(n)

#3). Bubble sort
# n=[5,7,2,8,3,7,5]
# i=0
# l=len(n)
# while i<l:
#     j=0
#     while j<l-1:
#         if n[j]>n[j+1]:
#             n[j],n[j+1]=n[j+1],n[j]
#         j+=1
#     i+=1
# print(n)


#Q51.FC251
# a=[[4,5],[6,7]]
# b=[[1,2],[3,8]]
# c=[[0,0],[0,0]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         c[i][j]=a[i][j]+b[j][i]
#         j+=1
#     i+=1
# for i in c:
#     print(i)



#Q52.FC252
# a=[[4,5],[9,7]]
# b=[[1,7],[2,3]]
# c=[[0,0],[0,0]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         c[i][j]=a[i][j]-b[j][i]
#         j+=1
#     i+=1
# for i in c:
#     print(i)


#Q53.FC253
# a=[[4,5],[6,7]]
# b=[[1,2],[3,8]]
# c=[[0,0],[0,0]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         c[i][j]=a[i][j]*b[j][i]
#         j+=1
#     i+=1
# for i in c:
#     print(i)


#Q54.FC254
# a=[[4,5],[6,7]]
# b=[[0,0],[0,0]]
# for i in a:
#     print(i)
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[0]):
#         b[i][j]=a[j][i]
#         j+=1
#     i+=1
# for i in b:
#     print(i)


#Q55.FC256
# n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# m=int(input('enter term >>'))
# i=0
# while i<m:
#     j=i+1
#     while j<len(n):
#         n[i],n[j]=n[j],n[i]
#         j+=1
#     i+=1
# print(n)



# Q56.FC257
# a=[[1,0,0],[0,1,0],[0,0,1]]
# count=0
# num=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[0]):
#         if i==j:
#             if a[i][j]==1:
#                 count+=1
#         else:
#             if a[i][j]!=0:
#                 num+=1
#         j+=1
#     i+=1
# if num==0:
#     if  count==len(a):
#         print('Identity')
# else:
#     print('Not Identity')


# Q57.FC258
# a=[[1,0,0],[0,1,0],[0,0,1]]
# count=0
# num=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[0]):
#         if i==j:
#             if a[i][j]!=0:
#                 count+=1
#         else:
#             if a[i][j]!=0:
#                 num+=1
#         j+=1
#     i+=1
# if num==0:
#     if  count==len(a):
#         print('Diagonal')
# else:
#     print('Not Diagonal')



# Q58.FC259
# a=[[1,0,0],[0,1,0],[0,0,1]]
# sum=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[0]):
#         if i==j:
#             sum+=a[i][j]
#         j+=1
#     i+=1
# print(sum)

    
# Q59.FC261
# a=[[6,5,4],[7,5,3],[9,6,8]]
# min=a[0][0]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[0]):
#         if a[i][j]<min:
#             min=a[i][j]
#         j+=1
#     i+=1
# print(min) 


# Q60.FC262
# a=[[6,5,4],[7,2,3],[9,1,8]]
# n=int(input('Enter value >>'))
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[0]):
#         if a[i][j]==n:
#             print([i],[j])
#         j+=1
#     i+=1



# Q61.FC264
# n=int(input('Enter number >>'))
# i=0
# a=[]
# while i<n:
#     b=[]
#     j=0
#     while j<n:
#         b.append(0)
#         j+=1
#     a.append(b)
#     i+=1
# i=0
# low=0
# high=n-1
# b=1
# count=(n+1)//2
# print(count)
# while i<count:
#     j=low
#     while j<=high:
#         a[low][j]=b
#         j+=1
#         b+=1
#     j=low+1
#     while j<=high:
#         a[j][high]=b
#         j+=1
#         b+=1
#     j=high-1
#     while j>=low:
#         a[high][j]=b
#         b+=1
#         j-=1
#     j=high-1
#     while j>low:
#         a[j][low]=b
#         b+=1
#         j-=1
#     low=low+1
#     high=high-1
#     i+=1
# for i in a:
#     print(i)




# Q62.FC279
# m=int(input('Enter number >>'))
# n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# i=2
# count=0
# while i<=m:
#     j=0
#     k=1
#     count=i
#     while j<len(n):
#         if n[j]>0:
#             if count!=k:
#                 k+=1
#             else:
#                 n[j]=-1
#                 k=1
#             j+=1
#         else:
#             j+=1
#     i+=1
# a=[]
# for i in n:
#     if i>0:
#         a.append(i)
# print(a)




# Q63.FC239
# sum1=0
# sum2=0
# sum3=0
# a=[[8,1,6],[3,5,7],[4,9,2]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[0]):
#         if i==j:
#             sum1+=a[i][j]
#         else:
#             sum2+=a[i][j]
#             sum3+=a[j][i]
#         j+=1
#     i+=1
# if sum1==sum2//2==sum3//2:
#     print('Magic square')
# else:
#     print('Not magic square')




# Q64.FC278
# a=list(input('Enter String >>'))
# b=list(input('Enter string >>'))
# count=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         if len(a)==len(b):
#             if a[i]==b[j]:
#                 count+=1
#         j+=1
#     i+=1
# if count==len(a):
#     print('Anagram')
# else:
#     print('Not Anagram')




# Q65.FC277
# a=list(input('Enter string >>'))
# b=list(input('Enter string >>'))
# c=''
# k=0
# while k<2:
#     i=0
#     while i<len(a):
#         count=0
#         j=0
#         while j<len(b):
#             if a[i]==b[j]:
#                 count+=1
#             j+=1
#         if count==0:
#             c+=a[i]
#         i+=1
#     k+=1
#     a,b=b,a       
#     i+=1
# print(c)



# Q66.FC272
# n=int(input('enter value >>'))
# x=[]
# i,a,b,c=0,0,1,0
# while i<=n:
#     # if i<=1:
#     #     c=i
#     # else:
#     x.append(c)
#     a=b
#     b=c
#     c=a+b
#     i+=1
# x.reverse()
# a=[]
# for i in x:
#     if i<=n:
#         n=n-i
#         a.append(i)
# print(a)




# Q67.FC273
# n=int(input('Enter value >>'))
# a=[]
# i=1
# while i<=n:
#     b=[]
#     j=1
#     p=0
#     while j<=i:
#         if i%j==0:
#             b.append(j)
#         j+=1
#     for k in b:
#         if n%k==0:
#             p+=1
#     if p==1:
#         a.append(b)
#     i+=1        
# c=[]
# for k in a:
#     if type(k)==list:
#         for n in k:
#             c.append(n)
#     else:
#         c.append(k)
# print(list(set(c)))



# Q68.FC227
# n=list(input('Enter Roman Number >>'))
# ro=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','III','II','I']
# de=[1000,900,500,400,100,90,50,40,10,9,5,4,3,2,1]
# row=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(ro):
#         if n[i]==ro[j]:
#             row+=de[j]
#         j+=1
#     i+=1
# print(row)


















        




























































