n=int(input())
count=0
for i in range(n):
    l=list(map(int,input().split()))
    if(l.count(1)>=2):
        count+=1
print(count)
