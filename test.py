from random import randint as ri

sc = []

for i in range(500):
    a = []
    for j in range(3):
        a.append(ri(20,100))
    sc.append(a)
print(sc)
