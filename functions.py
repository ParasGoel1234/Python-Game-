import json

def paras_goel(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

a = [22, 44, 55]
b = [23, 40, 95]
x = paras_goel(a)
y = paras_goel(b)
print(x)
print(y)
m = json.dumps(x)
l = json.dumps(y)
print(l, m)