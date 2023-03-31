"""Comparar 4 números solicitados al usuario, escribir condiciones que permita
mostrar que un número fue escrito 2 veces, que todos son iguales o por el contrario
todos son diferentes."""

numero1 = int(input("Ingresa un numero:   "))
numero2 = int(input("Ingresa un numero:   "))
numero3 = int(input("Ingresa un numero:   "))
numero4 = int(input("Ingresa un numero:   "))


if numero1 == numero2 and numero1 == numero3:
    print(numero1,"  Fue escrito dos veces")
elif numero1 == numero3:
    print(numero1,"  Fue escrito dos veces")
elif numero1 == numero4:
    print(numero1,"  Fue escrito dos veces")
elif numero2 == numero3:
    print(numero2,"  Fue escrito dos veces")
elif numero2 == numero4:
    print(numero2,"  Fue escrito dos veces")
elif numero3 == numero4:
    print(num3,"  Fue escrito dos veces")
elif numero1 == numero2 == numero3 == numero4:
    print(numero1,numero2,numero3,numero4,"  Son iguales")
else:
    print(f"{numero1},{numero2},{numero3} y {numero4} son diferentes")