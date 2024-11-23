from producto import Producto

def crear_catalogo():
    """
    Crea y devuelve un catálogo de productos clasificados por categorías.
    """
    catalogo = {
        "Línea Blanca": [
            Producto("LB001", "Refrigerador", 1600000, "Línea Blanca"),
            Producto("LB002", "Lavadora", 1200000, "Línea Blanca"),
            Producto("LB003", "Secadora", 1000000, "Línea Blanca")
        ],
        "Pequeños Electrodomésticos": [
            Producto("PE001", "Licuadora", 110000, "Pequeños Electrodomésticos"),
            Producto("PE002", "Cafetera", 90000, "Pequeños Electrodomésticos"),
            Producto("PE003", "Tostadora", 80000, "Pequeños Electrodomésticos")
        ],
        "Entretenimiento": [
            Producto("EN001", "Televisor", 550000, "Entretenimiento"),
            Producto("EN002", "Sistema de Sonido", 275000, "Entretenimiento")
        ],
        "Aires Acondicionados": [
            Producto("AA001", "Aire Acondicionado", 1600000, "Aires Acondicionados")
        ]
    }
    return catalogo

def mostrar_catalogo(catalogo):
    """
    Muestra el catálogo de productos.
    """
    for categoria, productos in catalogo.items():
        print(f"\nCategoría: {categoria}")
        for producto in productos:
            producto.mostrar_informacion()

def agregar_producto(catalogo):
    """
    Agrega un nuevo producto al catálogo.
    """
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    categoria = input("Ingrese la categoría del producto: ")
    nuevo_producto = Producto(codigo, nombre, precio, categoria)
    if categoria in catalogo:
        catalogo[categoria].append(nuevo_producto)
    else:
        catalogo[categoria] = [nuevo_producto]
    print(f"Producto {nombre} añadido al inventario.")

def borrar_producto(catalogo):
    """
    Borra un producto del catálogo por su código.
    """
    codigo = input("Ingrese el código del producto a borrar: ")
    for categoria, productos in catalogo.items():
        for i, producto in enumerate(productos):
            if producto.codigo == codigo:
                productos.pop(i)
                print(f"Producto con código {codigo} eliminado del inventario.")
                return
    print("Producto no encontrado.")
