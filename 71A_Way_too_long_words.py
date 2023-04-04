n=int(input())
for i in range(n):
    s=input()
    if(len(s)<=10):
        print(s)
    else:
        print(str(s[0])+str(len(s)-2)+str(s[len(s)-1]))

