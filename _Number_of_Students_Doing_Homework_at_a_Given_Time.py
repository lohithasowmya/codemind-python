x=int(input())
a=list(map(int,input().split()))
y=int(input())
b=list(map(int,input().split()))
z=int(input())
c=0
for i in range(max(x,y)):
    if(a[i]<=z and b[i]>=z):
        c+=1
print(c)
