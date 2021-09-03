# TUPLE UNPACKING

e = 1, 2, 3, 4, 5
q, w, *t = e
print(q, w, t)
x = [5, 6, 7, 8]
s = [1, 2, *x]
print(s)
a, *b, c = x
print(a, b, c)
