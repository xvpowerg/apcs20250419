cars = ['honda','BMW','Toyota','audi']
cars.sort()
print(cars)
#小寫 > 大寫 > 數字
cars.sort(key=lambda z :z.upper(),reverse=True)
print(cars)
cars.sort(key=len)
print(cars)
