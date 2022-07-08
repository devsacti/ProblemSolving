import sys

if __name__=="__main__":
    n=int(sys.stdin.readline().strip())
    nums=sys.stdin.readline().split()

    nums.insert(0,nums.pop())
    

    print(' '.join(nums))