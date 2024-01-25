#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese #número hasta cero separados por comas.

n = int(input("Introduce un numero positivo: ")) #10
u = 'hola'
j = 0

for j in range(n,-1,-1): #range(n,final,paso)
    print(j,end=", ")


#4,3,2,1,0