n = int(input())
s = input()
min = 0

for i in range(n-1):
    if s[i] == s[i+1]:
        min += 1

print(min)
