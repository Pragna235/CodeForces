s=input()
s=s.lower()
p=""
l=['a','e','i','o','u','y']
for i in range(len(s)):
    if(s[i] not in l):
        p+='.'
        p+=s[i]
print(p)
