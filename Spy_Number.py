n=int(input())
temp=n
sum=0
mul=1
while(temp>0):
    r=temp%10
    sum=sum+r
    mul=mul*r
    temp=temp//10
if(sum==mul):
    print('Spy Number')
else:
    print('Not Spy Number')

