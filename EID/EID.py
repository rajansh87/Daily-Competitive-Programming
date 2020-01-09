t = int(input())
for q in range(t):
    #n,m=input().split()
    #n,m=int(n),int(m)
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    m=1000000000000000000
    for i in range(n-1):
        x=arr[i+1]-arr[i]
        m=min(x,m)
    print(m)










    
