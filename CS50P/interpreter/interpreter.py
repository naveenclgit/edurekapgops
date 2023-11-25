import operator
intpr = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
}

x, y, z = input("Expression: ").strip().lower().split(" ")

a = int(x)
b = int(z)
print (float(intpr[y](a,b)))
