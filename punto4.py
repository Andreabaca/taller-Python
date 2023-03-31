print("**MENU DE OPCIONES**")
print ("1. Amarillo")
print ("2. Azul")
print ("3. Rojo")
print ("4. Blanco")
print ("5. Negro")
print ("6. Salir")
     
opcion1 = int(input("selecciona una Opción :  "))
opcion2 = int(input("Selecciona otra opción  :  "))
 
if opcion1 == 1 and opcion2 == 2:
    print("💚 Verde 💚")
elif opcion1 == 1 and opcion2 == 3:
    print("🧡 Naranja 🧡")
elif opcion1 == 1 and opcion2 == 4:
    print("💡 Crema 💡")
elif opcion1 == 1 and opcion2 == 5:
    print("Gris verdoso ")
elif opcion1 == 1 and opcion2 == 1:
    print("😕 Opción no válida 😕")
elif opcion1 == 2 and opcion2 == 1:
    print("💚 Verde 💚")
elif opcion1 == 2 and opcion2 == 2:
    print("😕 Opción no válida 😕")
elif opcion1 == 2 and opcion2 == 3:
    print("💜 Morado 💜")
elif opcion1 == 2 and opcion2 == 4:
    print("💦 Azul Claro 💦")
elif opcion1 == 2 and opcion2 == 5:
    print("💙 Azul Oscuro 💙")
elif opcion1 == 3 and opcion2 == 1:
    print("🧡 Naranja 🧡")
elif opcion1 == 3 and opcion2 == 2:
    print("💜 Morado 💜")
elif opcion1 == 3 and opcion2 == 3:
    print("😕 Opción no válida 😕")
elif opcion1 == 3 and opcion2 == 4:
    print("💗 Rosado 💗")
elif opcion1 == 3 and opcion2 == 5:
    print("🤎 Café 🤎")
elif opcion1 == 4 and opcion2 == 1:
    print("💡 Crema 💡")
elif opcion1 == 4 and opcion2 == 2:
    print("💦 Azul Claro 💦")
elif opcion1 == 4 and opcion2 == 3:
    print("💗 Rosado 💗")
elif opcion1 == 4 and opcion2 == 4:
    print("😕 Opción no válida 😕")
elif opcion1 == 4 and opcion2 == 5:
    print("🖤 Gris 🖤")
elif opcion1 == 5 and opcion2 == 1:
    print("Verde Oliva")
elif opcion1 == 5 and opcion2 == 2:
    print("💙 Azul Oscuro 💙" )
elif opcion1 == 5 and opcion2 == 3:
    print("🤎 Café 🤎")
elif opcion1 == 5 and opcion2 == 4:
    print("🖤 Gris 🖤")
elif opcion1 == 5 and opcion2 == 5:
    print("😕 Opción no válida 😕")
elif opcion1 == 6:
    salir = True
else:
    print("Introduce un numero entre 1 y 5")
 
print("Fin")