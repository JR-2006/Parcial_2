def leer_opcion_valida(mensaje, opciones_validas):
    """
    Lee una opción válida del usuario.
    """
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones_validas:
                return opcion
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
