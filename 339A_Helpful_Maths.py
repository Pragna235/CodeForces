s=input()
l=[s[i] for i in range(0,len(s),2)]
#print(l)
l1=[int(i) for i in l]
#print(l1)
l1.sort()
#print(l1)
for i in range(len(l1)):
    print(l1[i],end = "")
    if(i==len(l1)-1):
        break
    else:
        print('+',end = "")

