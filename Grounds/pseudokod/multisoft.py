
a = ""
s = "527918932189"

for i in range(len(s)-1):
    if (abs(int(s[i-1]) - int(s[i+1])) == int(s[i])):
        a += s[i]

print(f"www.multisoft.se/{a}")