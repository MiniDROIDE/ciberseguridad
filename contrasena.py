
def comprobar_longitud(contrasena):
    return len(contrasena) >= 8


contrasena = "Hola1234"

print("=== COMPROBADOR DE CONTRASEÑAS ===")
print("Contraseña:", contrasena)
print("Longitud:", len(contrasena))
print("¿Longitud correcta?:", comprobar_longitud(contrasena))
print("Prueba corta:", comprobar_longitud("Hola"))
print("Prueba larga:", comprobar_longitud("Hola1234"))
print("=== FIN ===")
