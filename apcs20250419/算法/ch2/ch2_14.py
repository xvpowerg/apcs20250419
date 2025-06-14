poly1 = [1,-3,2]
poly2 = [3, 2, 2, -3, 1, 1, 0]

x = 2
fx = 0
for i in range(len(poly1)):
    fx += poly1[i] * ｘ ** i
print(fx)    

y = 2
fy = 0

for j in range(poly2[0]):
    fy += poly2[2*j+1] * y ** poly2[2*(j+1)]
print(fy)
