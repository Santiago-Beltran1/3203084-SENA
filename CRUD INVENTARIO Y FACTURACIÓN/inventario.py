INVENTARIO_FILE = "inventario.txt"
FACTURAS_FILE = "facturas.txt"
IVA = 0.19

# FUNCIONES DE INVENTARIO

def cargar_inventario():
    inventario = []
    try:
        with open(INVENTARIO_FILE, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    inventario.append({
                        "id": datos[0],
                        "nombre": datos[1],
                        "precio": float(datos[2]),
                        "stock": int(datos[3])
                    })
    except FileNotFoundError:
        pass  # si no existe el archivo devuelve lista vacía
    return inventario

def guardar_inventario(inventario):
    with open(INVENTARIO_FILE, "w") as f:
        for prod in inventario:
            f.write(f"{prod['id']},{prod['nombre']},{prod['precio']},{prod['stock']}\n")

def agregar_producto():
    inventario = cargar_inventario()
    id_prod = input("ID del producto: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Cantidad: "))
    inventario.append({"id": id_prod, "nombre": nombre, "precio": precio, "stock": stock})
    guardar_inventario(inventario)
    print("Producto agregado correctamente.")

def listar_productos():
    inventario = cargar_inventario()
    if not inventario:
        print("Inventario vacío.")
    else:
        for prod in inventario:
            print(f"ID:{prod['id']} | Nombre:{prod['nombre']} | Precio:{prod['precio']} | Stock:{prod['stock']}")

def buscar_producto():
    inventario = cargar_inventario()
    criterio = input("Buscar por ID o Nombre: ")
    encontrados = [p for p in inventario if p["id"] == criterio or p["nombre"].lower() == criterio.lower()]
    if encontrados:
        for p in encontrados:
            print(f"ID:{p['id']} | {p['nombre']} | Precio:{p['precio']} | Stock:{p['stock']}")
    else:
        print("Producto no encontrado.")

def actualizar_producto():
    inventario = cargar_inventario()
    id_prod = input("ID del producto a actualizar: ")
    for p in inventario:
        if p["id"] == id_prod:
            p["precio"] = float(input("Nuevo precio: "))
            p["stock"] = int(input("Nuevo stock: "))
            guardar_inventario(inventario)
            print("Producto actualizado.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    inventario = cargar_inventario()
    id_prod = input("ID del producto a eliminar: ")
    nuevo_inv = [p for p in inventario if p["id"] != id_prod]
    if len(nuevo_inv) < len(inventario):
        guardar_inventario(nuevo_inv)
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

# FUNCIONES DE FACTURAS

def crear_factura():
    inventario = cargar_inventario()
    if not inventario:
        print("No hay productos en inventario.")
        return

    factura = []
    while True:
        listar_productos()
        id_prod = input("Ingrese ID del producto (o 'fin' para terminar): ")
        if id_prod.lower() == "fin":
            break
        for p in inventario:
            if p["id"] == id_prod:
                cantidad = int(input("Cantidad: "))
                if cantidad <= p["stock"]:
                    subtotal = cantidad * p["precio"]
                    factura.append({
                        "id": p["id"],
                        "nombre": p["nombre"],
                        "precio": p["precio"],
                        "cantidad": cantidad,
                        "subtotal": subtotal
                    })
                    p["stock"] -= cantidad
                else:
                    print("Stock insuficiente.")
        guardar_inventario(inventario)

    if factura:
        total = sum(item["subtotal"] for item in factura)
        iva_val = total * IVA
        total_final = total + iva_val

        with open(FACTURAS_FILE, "a") as f:
            f.write("FACTURA:\n")
            for item in factura:
                f.write(f"{item['id']},{item['nombre']},{item['precio']},{item['cantidad']},{item['subtotal']}\n")
            f.write(f"SUBTOTAL: {total}\nIVA: {iva_val}\nTOTAL: {total_final}\n---\n")

        print("Factura creada y guardada.")

def listar_facturas():
    try:
        with open(FACTURAS_FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No hay facturas registradas.")

def eliminar_facturas():
    try:
        with open(FACTURAS_FILE, "r"):  # comprobar si existe
            pass
        with open(FACTURAS_FILE, "w") as f:  # sobrescribir vacío
            pass
        print("Todas las facturas eliminadas.")
    except FileNotFoundError:
        print("No hay facturas registradas.")

# MENÚ PRINCIPAL

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Añadir producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Crear factura")
        print("7. Listar facturas")
        print("8. Eliminar facturas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            crear_factura()
        elif opcion == "7":
            listar_facturas()
        elif opcion == "8":
            eliminar_facturas()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
