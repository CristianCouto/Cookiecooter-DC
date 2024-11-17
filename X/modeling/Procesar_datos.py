import pandas as pd

# Ruta al archivo (asegúrate de que exista en data/raw)
archivo = "Cookiecooter-DC/data/processed/Ocra-Newsan 1.41.xlsx"

# Cargar el archivo Excel
datos = pd.read_excel(archivo)

# Mostrar las primeras filas
print("Primeras filas del dataset:")
print(datos.head())

# Eliminar filas con valores vacíos
datos_limpios = datos.dropna()

# Guardar los datos limpios en la carpeta de datos procesados
datos_limpios.to_excel("data/processed/datos_limpios.xlsx", index=False)
print("Datos limpios guardados en 'data/processed/datos_limpios.xlsx'")