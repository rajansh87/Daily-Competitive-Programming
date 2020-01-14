t = int(input())
for qwerty in range(t):
#n,m=input().split()
#n,m=int(n),int(m)
    n=int(input())
    #arr=list(map(int,input().split()))
    a=[0]*26
    s=""
    for i in range(n):
        s=input()
        for j in range(len(s)):
            p=ord(s[j])-97
            a[p]+=1
    arr=[0]*6
    arr[0]=a[2]//2
    arr[1]=a[3]
    arr[2]=a[4]//2
    arr[3]=a[5]
    arr[4]=a[7]
    arr[5]=a[14]

    print(min(arr))
    
                            
