t = int(input())
for qwerty in range(t):
    #n,q=input().split()
    #n,q=int(n),int(q)
    n=int(input())
    #arr=list(map(int,input().split()))
    alice=list(map(int,input().split()))
    bob=list(map(int,input().split()))
    
    alice.remove(max(alice))
    bob.remove(max(bob))
    if(sum(alice)<sum(bob)):
        print("Alice")
    elif(sum(alice)>sum(bob)):
        print("Bob")
    else:
        print("Draw")
        
   

















                            
