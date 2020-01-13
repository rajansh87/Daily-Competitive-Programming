t = int(input())
for qwerty in range(t):
    #n,q=input().split()
    #n,q=int(n),int(q)
    n=int(input())
    #arr=list(map(int,input().split()))
    firstName=[]
    lastName=[]
    for i in range(n):
        x,y=input().split()
        firstName.append(x)
        lastName.append(y)
    for i in range(n):
        if(firstName.count(firstName[i])>1):
            print(firstName[i],lastName[i],sep=" ")
        else:
            print(firstName[i])






                            
