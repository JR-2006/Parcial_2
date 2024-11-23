from catalogo import crear_catalogo, mostrar_catalogo, agregar_producto, borrar_producto
from venta import registrar_venta
from factura import Factura
from errores import leer_opcion_valida
from datos_cliente import obtener_datos_cliente

def menu():
    """
    Muestra el menú principal del sistema de facturación electrónica.
    """
    catalogo = crear_catalogo()
    while True:
        print("\nSistema de Facturación Electrónica")
        print("1. Mostrar catálogo de productos")
        print("2. Registrar venta")
        print("3. Agregar nuevo producto")
        print("4. Borrar producto")
        print("5. Salir")
        opcion = leer_opcion_valida("Seleccione una opción: ", [1, 2, 3, 4, 5])
        if opcion == 1:
            mostrar_catalogo(catalogo)
        elif opcion == 2:
            cliente = obtener_datos_cliente()
            ventas = registrar_venta(catalogo)
            factura = Factura(ventas, cliente)
            factura.calcular_totales()
            factura.mostrar_factura()
            factura.guardar_factura("factura.txt")
        elif opcion == 3:
            agregar_producto(catalogo)
        elif opcion == 4:
            borrar_producto(catalogo)
        elif opcion == 5:
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    menu()