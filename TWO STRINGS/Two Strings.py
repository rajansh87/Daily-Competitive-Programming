t = int(input())
for q in range(t):
    #n,k=input().split()
    #n,k=int(n),int(k)
    #n,m,k=input().split()
    #n,m,k=int(n),int(m),int(k)
    #n=int(input())
    #n=int(input())
    #arr=list(map(int,input().split()))
    
    s1=input()
    s2=input()
    if(len(s1)!=len(s2)):
        print("NO")  #unequal strings
    else:
        a1=[0]*26
        #a2=[0]*26
        for i in range(len(s1)):
            a1[ord(s1[i])-97]+=1
        for i in range(len(s2)):
            a1[ord(s2[i])-97]-=1
        if(a1.count(0)==26):
            print("YES") # equal strings
        else:
            print("NO")
