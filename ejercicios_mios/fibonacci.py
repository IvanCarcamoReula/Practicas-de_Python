a,b = 0,1
fibonacci = [0]

num = int(input("ingrese un valor: "))

while b < num:
    fibonacci.append(b)
    a,b = b,a+b
    
print(fibonacci)