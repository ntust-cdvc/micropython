odd = []
even = []
for i in range(1, 100, 2):
    odd.append(i)
for i in range(2, 101, 2):
    even.append(i)
print(odd)
print(even)
new = odd + even
new.sort()
print(new)
index = 0
while index < len(new):
    if new[index] % 5 == 0:
        del new[index]
    else:
        index += 1
#new = [value for value in new if value % 5 != 0]
#new = list(filter(lambda x: x % 5 != 0, new))
print(new)
