#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de #más abajo, de altura el número introducido.


n=int(input("Ingrese el número:"))
for t in range(-1,n,1):
    print('*'*(t+1))