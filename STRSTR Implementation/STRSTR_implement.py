t = int(input())
for qwerty in range(t):
        #n,m=input().split()
            #n,m=int(n),int(m)
            #n=int(input())
            #arr=list(map(int,input().split()))
        s1=input()
        s2=input()
        
        for i in range(len(s1)-len(s2)):
                if(s1[i]==s2[0]):
                        c=0
                        for j in range(len(s2)):
                                if(s1[i+j]==s2[j]):
                                        c+=1
                                else:
                                        break
                        if(c==len(s2)):
                                return(i)
                
        if(s1!=s2):
            return(-1)
        else:
            return(0)
