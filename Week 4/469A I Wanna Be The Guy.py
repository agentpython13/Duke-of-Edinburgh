a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=b[1:]+c[1:]

if(len(set(d))==a):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")