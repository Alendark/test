xо= float(input("Первая точка окружности: "))
yо= float(input("Вторая точка окружности: "))
r= float(input("Радиус круга: "))
y= float(input("Первая координата точки: "))
x= float(input("Вторая координата точки: "))

if (x - xо) * (x - xо) + (y - yо) * (y - yо) < r * r:
    print("Точка принадлежит окружности")
elif (x - xо) * (x - xо) + (y - yо) * (y - yо) > r * r:
    print("Точка не принадлежит окружности")
else:
    print("Точка на окружности")
    