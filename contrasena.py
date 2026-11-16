
from utilidades import comprobar_numero


def comprobar_longitud(contrasena):
    return len(contrasena) >= 8


def comprobar_mayuscula(contrasena):
    return any(caracter.isupper() for caracter in contrasena)


contrasena = "Hola1234"

print("=== COMPROBADOR DE CONTRASEÑAS ===")
print("Contraseña:", contrasena)
print("¿Longitud correcta?:", comprobar_longitud(contrasena))
print("¿Contiene números?:", comprobar_numero(contrasena))
print("¿Contiene mayúsculas?:", comprobar_mayuscula(contrasena))


