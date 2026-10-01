def plus(a,b):
    print(a + b)
def minus(a,b):
    print(a-b)
def umn(a,b):
    print(a*b)

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
z = input("Введите операцию(+): ")
if z == "+":
    plus(a,b)
elif z == "-":
    minus(a,b)
elif z == "*":
    umn(a,b)
