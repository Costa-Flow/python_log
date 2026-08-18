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

def pedir_numero(mensaje, es_entero=False, permitir_vacio=False):
    """Solicita un número por consola y repite hasta que el usuario ingrese un valor válido."""
    while True:
        entrada = input(mensaje).strip()
        if permitir_vacio and entrada == "":
            return None
        try:
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
    
    nuevo_registro = pd.DataFrame([{
        'ID': 0,
        'Producto': nombre,
        'Cantidad': cantidad,
        'Precio': precio
    }])
    
    df = pd.concat([df, nuevo_registro], ignore_index=True)
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

def editar_producto():
    df = cargar_inventario()
    if df.empty:
        print("\nEl inventario está vacío, no hay nada que editar.")
        return

    print("\n--- Editar Producto ---")
    id_a_editar = pedir_numero("Ingresa el ID del producto a modificar: ", es_entero=True)
    
    if id_a_editar in df['ID'].values:
        idx = df[df['ID'] == id_a_editar].index[0]
        prod_actual = df.loc[idx, 'Producto']
        cant_actual = df.loc[idx, 'Cantidad']
        prec_actual = df.loc[idx, 'Precio']

        print(f"\nEditando ID {id_a_editar}: {prod_actual}")
        print("(Deja el campo en blanco y presiona Enter para mantener el valor actual)\n")

        # Nuevo nombre
        nuevo_nombre = input(f"Nuevo nombre [{prod_actual}]: ").strip()
        if nuevo_nombre:
            df.loc[idx, 'Producto'] = nuevo_nombre

        # Nueva cantidad
        nueva_cant = pedir_numero(f"Nueva cantidad [{cant_actual}]: ", es_entero=True, permitir_vacio=True)
        if nueva_cant is not None:
            df.loc[idx, 'Cantidad'] = nueva_cant

        # Nuevo precio
        nuevo_prec = pedir_numero(f"Nuevo precio [${prec_actual:.2f}]: ", es_entero=False, permitir_vacio=True)
        if nuevo_prec is not None:
            df.loc[idx, 'Precio'] = nuevo_prec

        df.to_excel(ARCHIVO, index=False)
        print(f"\n¡Producto ID {id_a_editar} actualizado exitosamente!")
    else:
        print(f"¡Error! No existe ningún producto con el ID {id_a_editar}.")

def borrar_producto():
    df = cargar_inventario()
    if df.empty:
        print("\nEl inventario está vacío, no hay nada que borrar.")
        return

    print("\n--- Borrar Producto ---")
    id_a_borrar = pedir_numero("Ingresa el ID del producto a eliminar: ", es_entero=True)
    
    if id_a_borrar in df['ID'].values:
        nombre = df[df['ID'] == id_a_borrar]['Producto'].values[0]
        df = df[df['ID'] != id_a_borrar]
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
    print("4. Editar producto")
    print("5. Borrar producto")
    print("6. Salir")
    
    opcion = input("Selecciona una opción (1-6): ")
    
    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        editar_producto()
    elif opcion == "5":
        borrar_producto()
    elif opcion == "6":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")