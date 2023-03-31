"""Para tributar un determinado impuesto se debe ser mayor de 18 años y tener
unos ingresos iguales o superiores a 2.500.000 mensuales. Escribir un
programa que pregunte al usuario su edad y sus ingresos mensuales y muestre
por pantalla si el usuario tiene que tributar o no."""


Edad=int(input("Ingrese su edad:"))
Ingresos=int(input("Ingrese  su Salario:"))

if Edad >=18 and Ingresos >= 2500000:
    print("Usted SI debe  tributar")
else:
    print("Usted NO debe tributar")