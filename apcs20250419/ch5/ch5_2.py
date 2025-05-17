cars = ['Honda','Toyota','Ford','BMW']
print(cars)
v1 = cars.pop()
print("pop:",cars)
print("v1:",v1)
v2 = cars.pop(1)
print("pop:",cars)
print("v2:",v2)
v3 = cars.pop()
print("v3:",v3)
v3 = cars.pop()
if len(cars) != 0 :
    print("v3:",v3)
    v3 = cars.pop()

