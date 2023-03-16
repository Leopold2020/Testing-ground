
s=""
a="1112031584"
for i in range(len(a)):
    if int(a[i])%2 == int(a[i-1])%2:
        s += max(a[i], a[i-1])

print(f"www.multisoft.se/{s}")