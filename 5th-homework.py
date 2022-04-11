# Write your code here :-)
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
for i, value in enumerate(new):
    if value % 5 == 0:
        del new[i]
print(new)
