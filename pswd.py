import random

def principal():
    # Solicitar entrada del usuario y generar la contraseña
    longitud = int(input("¿Cuántos caracteres deseas en la contraseña? ").strip())
    incluir_mayúsculas = input("¿Quieres incluir mayúsculas? ").strip().lower() == "si"
    incluir_números = input("¿Quieres incluir números? ").strip().lower() == "si"
    incluir_especiales = input("¿Quieres incluir caracteres especiales? ").strip().lower() == "si"

    # Generar y mostrar la contraseña
    conjunto_de_caracteres = "abcdefghijklmnopqrstuvwxyz" + \
                             ("ABCDEFGHIJKLMNOPQRSTUVWXYZ" if incluir_mayúsculas else "") + \
                             ("0123456789" if incluir_números else "") + \
                             ("!@#$%^&*()-_=+[]{}|;:,.<>?/" if incluir_especiales else "")
    
    contraseña = ''.join(random.choice(conjunto_de_caracteres) for _ in range(longitud))
    print("Tu contraseña segura es:", contraseña)

principal()
