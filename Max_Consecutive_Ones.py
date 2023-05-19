n=int(input())
a=list(map(int,input().split()))
c=0
x=[]
maxx=0
for i in a:
    if i==1:#     1 1  
        c+=1#     1 2 1
        maxx=max(c,maxx)#1=(1,0) 2=(2,1)
    else:
        c=0
print(maxx)