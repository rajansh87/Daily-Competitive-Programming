t = int(input())
for q in range(t):
    #n,k=input().split()
    #n,k=int(n),int(k)
    #n,m,k=input().split()
    #n,m,k=int(n),int(m),int(k)
    #n=int(input())
    #n=int(input())
    #arr=list(map(int,input().split()))
    n=int(input())    
    s=input()
    arr=[]
    for i in range(n):
        arr.append(s[i])
    #step 1:
    if(n%2!=0):
        for i in range(0,n-2,2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    else:
        for i in range(0,n-1,2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
    #print(arr)

    #step 2:
    
    for i in range(n):
        x=ord(arr[i])
        x=x-97
        y=122-x
        arr[i]=chr(y)
    s=""
    for i in range(n):
        s=s+arr[i]
            
    print(s)
