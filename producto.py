class Producto:
    def __init__(self, codigo, nombre, precio, categoria):
        """
        Inicializa un producto con su código, nombre, precio y categoría.
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_informacion(self):
        """
        Muestra la información del producto.
        """
        print(f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Categoría: {self.categoria}")
