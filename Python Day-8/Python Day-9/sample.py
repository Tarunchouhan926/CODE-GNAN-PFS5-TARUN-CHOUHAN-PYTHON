#chef team
'''
t=int(input())
for i in range(t):
    n=int(input())
    ev=[]
    ov=[]
    for j in range(1,n+ 1):
       if n%j==0 and i%2==0:
           ev.append(j)
       elif n%j==0 and i%2!=0:
           ov.append(j)
    if len(ev)==len(ov):
         print(1)
    else:
       print(0)
      
#deblicate
t=int(input())
for i in range(t):
   n=int(input())
   arr=list(map(int,input().split()))[:n]
   res=[]
   for i in arr:
       if i not in res:
           res.append(i)
   print(*res,sep=" ")
'''
t=int(input())
for i in range(t):
   n,x=map(int,input().split())
   a=list(map(int,input().split()))[::n]
   b=list(map(int,input().split()))[::n]
   fc=0
   for i in range(n):
     if a[i]>=x:
         fc=fc+b[i]
   print(fc)
            
     
     

    
