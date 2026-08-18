import pandas as pd

ARCHIVO = "inventario.xlsx"

def cargar_inventario():
    try:
        return pd.read_excel(ARCHIVO)
    except FileNotFoundError:
        return pd.DataFrame(columns=['ID', 'Producto', 'Cantidad', 'Precio'])

def mostrar_inventario():
    df = cargar_inventario()
    print("\n--- Inventario Actual ---")
    if df.empty:
        print("El inventario está vacío.")
    else:
        print(df.to_string(index=False))

def pedir_numero(mensaje, es_entero=False):
    """Solicita un número por consola y repite hasta que el usuario ingrese un valor válido."""
    while True:
        try:
            entrada = input(mensaje)
            valor = int(entrada) if es_entero else float(entrada)
            if valor < 0:
                print("¡Error! El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("¡Error! Debes ingresar un número válido (ej. 10 o 150.50).")

def agregar_producto():
    df = cargar_inventario()
    
    print("\n--- Agregar Nuevo Producto ---")
    
    nombre = input("Nombre del producto: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Intenta de nuevo: ").strip()
        
    cantidad = pedir_numero("Cantidad: ", es_entero=True)
    precio = pedir_numero("Precio: $", es_entero=False)
    
    # ID temporal; se reordenará al guardar
    nuevo_registro = pd.DataFrame([{
        'ID': 0,
        'Producto': nombre,
        'Cantidad': cantidad,
        'Precio': precio
    }])
    
    df = pd.concat([df, nuevo_registro], ignore_index=True)
    
    # Reordena todos los IDs de 1 a N
    df['ID'] = range(1, len(df) + 1)
    
    df.to_excel(ARCHIVO, index=False)
    print(f"\n¡Producto '{nombre}' guardado exitosamente en Excel!")

def buscar_producto():
    df = cargar_inventario()
    if df.empty:
        print("\nEl inventario está vacío.")
        return

    print("\n--- Buscar Producto ---")
    busqueda = input("Ingresa el nombre o parte del nombre a buscar: ").strip().lower()
    
    resultado = df[df['Producto'].astype(str).str.lower().str.contains(busqueda)]
    
    if resultado.empty:
        print(f"No se encontraron productos que coincidan con '{busqueda}'.")
    else:
        print("\nResultados de la búsqueda:")
        print(resultado.to_string(index=False))

def borrar_producto():
    df = cargar_inventario()
    if df.empty:
        print("\nEl inventario está vacío, no hay nada que borrar.")
        return

    print("\n--- Borrar Producto ---")
    id_a_borrar = pedir_numero("Ingresa el ID del producto a eliminar: ", es_entero=True)
    
    if id_a_borrar in df['ID'].values:
        nombre = df[df['ID'] == id_a_borrar]['Producto'].values[0]
        
        # Elimina la fila seleccionada
        df = df[df['ID'] != id_a_borrar]
        
        # Reordena los IDs de las filas restantes de 1 a N
        df['ID'] = range(1, len(df) + 1)
        
        df.to_excel(ARCHIVO, index=False)
        print(f"\n¡Producto '{nombre}' eliminado. La lista se reordenó consecutivamente en Excel!")
    else:
        print(f"¡Error! No existe ningún producto con el ID {id_a_borrar}.")

# --- Menú Principal ---
while True:
    print("\n=== SISTEMA DE INVENTARIO (EXCEL) ===")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Borrar producto")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        borrar_producto()
    elif opcion == "5":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")