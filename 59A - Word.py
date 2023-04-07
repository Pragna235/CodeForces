s=input()
l,u=0,0
for i in s:
    if(i.isupper()):
        u+=1
    else:
        l+=1
if(u>l):
    s=s.upper()
else:
    s=s.lower()
print(s)
