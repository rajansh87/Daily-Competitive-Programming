t = int(input())
for qwerty in range(t):
    n,k=input().split()
    n,k=int(n),int(k)
    #n=int(input())
    arr=list(map(int,input().split()))
    
    c=0
    m=0
    
    """for i in range(n-k+1):
        c=sum(arr[i:i+k])
        #print(arr[i:i+k])
        
        if(c>m):
            m=c
    print(m)
        
"""
    for i in range(n-k+1):
        s=0
        for j in range(i,i+k):
            s+=arr[j]
        if(m<s):
            m=s
    print(m)
