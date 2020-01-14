t = int(input())
for qwerty in range(t):
    #n,m=input().split()
    #n,m=int(n),int(m)
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    song=arr[k-1]
    arr.sort()
    print(arr.index(song)+1)
