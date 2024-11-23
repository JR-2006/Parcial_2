from producto import Producto

class Factura:
    def __init__(self, ventas, cliente):
        """
        Inicializa una factura con las ventas y los datos del cliente.
        """
        self.ventas = ventas
        self.cliente = cliente
        self.subtotal = 0
        self.iva = 0
        self.total = 0

    def calcular_totales(self):
        """
        Calcula el subtotal, IVA y total de la factura.
        """
        for producto, cantidad in self.ventas:
            self.subtotal += producto.precio * cantidad
        self.iva = self.subtotal * 0.19
        self.total = self.subtotal + self.iva

    def mostrar_factura(self):
        """
        Muestra la factura con los detalles del cliente y los productos comprados.
        """
        print("\nFactura:")
        print(f"Nombre: {self.cliente['nombre']}")
        print(f"Correo: {self.cliente['correo']}")
        print(f"Numero: {self.cliente['telefono']}")
        print("\nProductos:")
        for producto, cantidad in self.ventas:
            subtotal_producto = producto.precio * cantidad
            print(f"Producto: {producto.nombre}, Cantidad: {cantidad}, Precio Unitario: {producto.precio}, Subtotal: {subtotal_producto}")
        print(f"\nIVA: {self.iva}")
        print(f"Valor sin IVA: {self.subtotal}")
        print(f"Valor con IVA: {self.total}")
        print("\nEnviando factura a correo...")

    def guardar_factura(self, archivo):
        """
        Guarda la factura en un archivo de texto.
        """
        with open(archivo, 'w') as f:
            f.write("Factura:\n")
            f.write(f"Nombre: {self.cliente['nombre']}\n")
            f.write(f"Correo: {self.cliente['correo']}\n")
            f.write(f"Numero: {self.cliente['telefono']}\n")
            f.write("\nProductos:\n")
            for producto, cantidad in self.ventas:
                subtotal_producto = producto.precio * cantidad
                f.write(f"Producto: {producto.nombre}, Cantidad: {cantidad}, Precio Unitario: {producto.precio}, Subtotal: {subtotal_producto}\n")
            f.write(f"\nIVA: {self.iva}\n")
            f.write(f"Valor sin IVA: {self.subtotal}\n")
            f.write(f"Valor con IVA: {self.total}\n")
            f.write("\nEnviando factura a correo...\n")
