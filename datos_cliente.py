def obtener_datos_cliente():
    """
    Obtiene los datos del cliente.
    """
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    return {"nombre": nombre, "correo": correo, "telefono": telefono}
