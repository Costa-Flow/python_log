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
    
    # Garantizar ID único buscando el valor máximo actual
    nuevo_id = 1 if df.empty else int(df['ID'].max()) + 1
    
    # Validar que el nombre no quede vacío
    nombre = input("Nombre del producto: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Intenta de nuevo: ").strip()
        
    # Pedir números con validaciones
    cantidad = pedir_numero("Cantidad: ", es_entero=True)
    precio = pedir_numero("Precio: $", es_entero=False)
    
    nuevo_registro = pd.DataFrame([{
        'ID': nuevo_id,
        'Producto': nombre,
        'Cantidad': cantidad,
        'Precio': precio
    }])
    
    df = pd.concat([df, nuevo_registro], ignore_index=True)
    df.to_excel(ARCHIVO, index=False)
    print(f"\n¡Producto '{nombre}' (ID: {nuevo_id}) guardado exitosamente en Excel!")

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