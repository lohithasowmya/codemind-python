n=int(input())
x=n*n
temp=x
sum=0
while(temp>0):
    r=temp%10
    sum=sum+r
    temp=temp//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')
