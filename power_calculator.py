print("this is the power calculator!!")

b = int(input("Base: "))
p = int(input("Power: "))

r = 1
for _ in range(p):
    r *= b

print(r)
