"""Escribir un programa donde se ingrese la nota de las materias: desarrollo de
software, matemáticas, lógica programación, si el promedio es mayor o igual
que 3,0 muestre en pantalla aprobado, de lo contrario muestre en pantalla
reprobado."""

nota1=int(input("Ingrese nota de desarrollo de software:"))
nota2=int(input("Ingrese nota de matematicas:"))
nota3=int(input("Ingrese nota de desarrollo de logica programacion:"))

PromedioNotas=(nota1+nota2+nota3)/3

if PromedioNotas >=3.0:
    print("¡¡¡Felicitaciones...!!! APROBO, su promedio es: ",PromedioNotas)
else:
    print("¡¡¡Sigue intentando!!! REPROBO, su promedio es",PromedioNotas)