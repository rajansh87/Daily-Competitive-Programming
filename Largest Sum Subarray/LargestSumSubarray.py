t=int(input())
for qwerty in range(t):
        #n,a,b,c=input().split()
        #n,a,b,c=int(n),int(a),int(b),int(c)
        n=int(input())
        arr=list(map(int,input().split()))
        me=0
        mf=-100000000000000000000000     #min
        for i in range(n):
                me+=arr[i]
                if(mf<me):
                        mf=me
                if(me<0):
                        me=0
        print(mf)
        
