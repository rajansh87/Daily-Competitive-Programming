t=int(input())
for qwerty in range(t):
        
        #n,a,b,c=input().split()
        #n,a,b,c=int(n),int(a),int(b),int(c)
        #n=int(input())
        #arr=list(map(int,input().split()))
        if n == 0 or n == 1: 
                return n 
  
    # To store index of next 
    # unique element 
        j = 0
  
    # Doing same as done 
    # in Method 1 Just 
    # maintaining another  
    # updated index i.e. j 
        for i in range(0, n-1): 
                if arr[i] != arr[i+1]: 
                    arr[j] = arr[i] 
                    j += 1
  
        arr[j] = arr[n-1] 
        j += 1
        return j 
                        
                        

