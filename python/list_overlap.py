import random
a = []
b = []
counter = 0
while counter <= 13:
 a.append(random.randrange(100))
 b.append(random.randrange(100))
 counter += 1
c = []
print "list a: ", a
print "list b: ", b

for item in a:
 if item in b and item not in c:
     c.append(item)


print (c)
