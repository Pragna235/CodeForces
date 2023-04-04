n,k=map(int,input().split())
l=list(map(int,input().split()))
count=0
for ele in l:
    if (ele>=l[k-1] and ele!=0):
        count+=1
print(count)
