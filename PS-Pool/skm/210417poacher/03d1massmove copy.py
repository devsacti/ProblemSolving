import sys

if __name__=="__main__":
    n,x, d,t = map(int, sys.stdin.readline().split())
    t %= (2*n-2)
    dx=[-1,1]

    while( x + t*dx[d] < 1 or x + t*dx[d]>n):
        if(x + t*dx[d] < 1):
            t-= (x-1)
            x=1
            d=1
        elif(x + t*dx[d] < n):
            t-= (n-x)
            x=n
            d=0

    x += t*dx[d]

    print(x,d)
