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
    print(df.to_string(index=False))

def agregar_producto():
    df = cargar_inventario()
    
    print("\n--- Agregar Nuevo Producto ---")
    nuevo_id = len(df) + 1
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: $"))
    
    nuevo_registro = pd.DataFrame([{
        'ID': nuevo_id,
        'Producto': nombre,
        'Cantidad': cantidad,
        'Precio': precio
    }])
    
    # Unir el nuevo registro y guardar en el Excel
    df = pd.concat([df, nuevo_registro], ignore_index=True)
    df.to_excel(ARCHIVO, index=False)
    print(f"\n¡Producto '{nombre}' guardado exitosamente en Excel!")

# --- Menú Principal ---
while True:
    print("\n=== SISTEMA DE INVENTARIO (EXCEL) ===")
    print("1. Ver inventario")
    print("2. Agregar producto")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1-3): ")
    
    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        print("¡Saliendo del programa!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")