t=int(input())
for qwerty in range(t):
        
        #n,a,b,c=input().split()
        #n,a,b,c=int(n),int(a),int(b),int(c)
        #n=int(input())
        arr1=list(map(int,input().split()))
        arr2=list(map(int,input().split()))
        n1,n2=len(arr1),len(arr2)
        arr3=[]
        i=0
        j=0
        k=0
        while(i<n1 and j <n2):
                if(arr1[i]<arr2[j]):
                        arr3.append(arr1[i])
                        i+=1
                else:
                        arr3.append(arr2[j])
                        j+=1
        if(j!=n1):
                for k in range(j,n2):
                        arr3.append(arr2[k])
        elif(i!=n2):
                for k in range(i,n1):
                        arr3.append(arr1[k])
        print(arr3)

