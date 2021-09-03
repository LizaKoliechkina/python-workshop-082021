from collections import Counter

# Counter counts number of elements in collection
# Counter inherits from Dict

c1 = Counter('sequence')
c2 = Counter({'a': 3, 'c': 1})
c3 = Counter(b=3, f=65)
c4 = Counter()

print(c1)
print(c2)
print(c3)
print(c4)

c4.update('abc')
print(c4)
c4.update('abc')
print(c4)
c4.subtract('a')
print(c4)

print(c4.most_common(2))

l = ['l', 3, 8, 'l', 'dr', '3', 3, 'dr', 3]
c4.update(l)
print(c4)
print(c4.most_common(1))  # element that is most common
