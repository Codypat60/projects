import math

v = int(input("What is v: "))

va = int(input("What is the angle of v: "))

m = int(input("What is m: "))

ma = int(input("What is the angle of m: "))

vc = round(v * (math.cos(math.radians(va))), 2)

mc = round(m * (math.cos(math.radians(ma))), 2)

t1 = vc + mc

vs = round(v * (math.sin(math.radians(va))), 2)

ms = round(m * (math.sin(math.radians(ma))), 2)

t2 = vs + ms

print(t1, t2)