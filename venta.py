from producto import Producto

def seleccionar_producto(catalogo, codigo):
    """
    Selecciona un producto del catálogo por su código.
    """
    for categoria, productos in catalogo.items():
        for producto in productos:
            if producto.codigo == codigo:
                return producto
    return None

def registrar_venta(catalogo):
    """
    Registra la venta de productos seleccionados por el cliente.
    """
    ventas = []
    while True:
        codigo = input("Ingrese el código del producto (o 'fin' para terminar): ")
        if codigo.lower() == 'fin':
            break
        producto = seleccionar_producto(catalogo, codigo)
        if producto:
            cantidad = int(input(f"Ingrese la cantidad de {producto.nombre}: "))
            ventas.append((producto, cantidad))
        else:
            print("Producto no encontrado.")
    return ventas
