t = int(input())
for q in range(t):
    #n,k=input().split()
    #n,k=int(n),int(k)
    #n,m,k=input().split()
    #n,m,k=int(n),int(m),int(k)
    #n=int(input())
    #n=int(input())
    #arr=list(map(int,input().split()))
    
    num=int(input())
    n=num%8
    if(n==0):
        print(num-1,"SL",sep="")
    elif(n==7):
        print(num+1,"SU",sep="")
    elif(n==1):
        print(num+3,"LB",sep="")
    elif(n==4):
        print(num-3,"LB",sep="")
    elif(n==2):
        print(num+3,"MB",sep="")
    elif(n==5):
        print(num-3,"MB",sep="")
    elif(n==3):
        print(num+3,"UB",sep="")
    elif(n==6):
        print(num-3,"UB",sep="")
