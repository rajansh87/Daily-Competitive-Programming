# cook your dish here
t = int(input())

while t> 0:
    n = int(input())
    
    n //= 2
    
    ans = (n*(n - 1))/2
    
    print(int(ans))
    
    t -= 1
