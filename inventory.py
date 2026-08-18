import pandas as pd

# 1. Cargar el archivo Excel
df = pd.read_excel("inventario.xlsx")

# 2. Mostrar la tabla completa
print("--- Inventario Completo ---")
print(df)

# 3. Filtrar productos con menos de 10 unidades
print("\n--- Alerta de Reabastecimiento (Stock < 10) ---")
stock_bajo = df[df['Cantidad'] < 10]
print(stock_bajo)
