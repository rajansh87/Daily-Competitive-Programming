t = int(input())
for qwerty in range(t):
    #n,q=input().split()
    #n,q=int(n),int(q)
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(n):
        if(arr1[i]<=arr2[i]):
            c1+=1
        else:
            c1=-1
            break
    arr1.reverse()
    for i in range(n):
        if(arr1[i]<=arr2[i]):
            c2+=1
        else:
            c2=-5
            break
    if(c1==c2):
        if(c1==n):
            print("both")
    elif(c1==n):
        print("front")
    elif(c2==n):
        print("back")
    else:
        print("none")
    
