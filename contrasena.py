
from utilidades import comprobar_numero


def comprobar_longitud(contrasena):
    return len(contrasena) >= 8


def comprobar_mayuscula(contrasena):
    return any(caracter.isupper() for caracter in contrasena)


contrasena = "Hola1234"

print("=== COMPROBADOR DE CONTRASEÑAS ===")
print("Contraseña:", contrasena)
print("¿Contiene números?:", comprobar_numero(contrasena))
print("Longitud:", len(contrasena))
print("¿Longitud correcta?:", comprobar_longitud(contrasena))
print("Prueba corta:", comprobar_longitud("Hola"))
print("Prueba larga:", comprobar_longitud("Hola1234"))
print("=== FIN ===")
print("¿Contiene mayúscula?:", comprobar_mayuscula(contrasena))
print("Prueba sin mayúscula:", comprobar_mayuscula("hola1234"))

