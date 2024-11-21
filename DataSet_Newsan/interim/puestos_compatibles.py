import pandas as pd
import os

def obtener_puestos_compatibles(nombre_puesto, df):
    try:
        # Filtrar los datos por el puesto especificado
        puestos_compatibles = df[df['Nombre puesto'] == nombre_puesto]['Puesto compatible']

        # Verificar si se encontraron resultados
        if puestos_compatibles.empty:
            print(f"No se encontraron puestos compatibles para el puesto '{nombre_puesto}'.")
        else:
            print(f"Puestos compatibles para '{nombre_puesto}':")
            for puesto in puestos_compatibles:
                print(f"- {puesto}")
            # Mostrar el total de puestos compatibles
            print(f"\nTotal de puestos compatibles : {len(puestos_compatibles)}")  
            
            
    except Exception as e:
        print(f"Error al procesar los datos: {e}")

def listar_puestos(df):
    # Obtener valores únicos de la columna "Nombre puesto"
    puestos_unicos = df['Nombre puesto'].dropna().unique()
    print("Lista de puestos disponibles:")
    for idx, puesto in enumerate(puestos_unicos, start=1):
        print(f"{idx}. {puesto}")
    return puestos_unicos

if __name__ == "__main__":
    try:
        # Ruta fija al archivo en la carpeta "Processed"
        archivo = os.path.join(os.path.dirname(__file__), "..", "Processed", "Ocra-Newsan 1.42.xlsm")

        # Verificar si el archivo existe
        if not os.path.exists(archivo):
            print(f"Error: El archivo {archivo} no se encontró. Verifica que esté en la carpeta 'Processed'.")
            exit()

        # Cargar el archivo Excel y leer la hoja "Combinaciones 2"
        df = pd.read_excel(archivo, sheet_name="Combinaciones 2")

        # Listar los puestos disponibles
        puestos_disponibles = listar_puestos(df)

        # Solicitar al usuario que seleccione un puesto
        seleccion = int(input("\nSelecciona un puesto ingresando el número correspondiente: "))
        if 1 <= seleccion <= len(puestos_disponibles):
            puesto_seleccionado = puestos_disponibles[seleccion - 1]
            print(f"\nHas seleccionado: {puesto_seleccionado}")
            obtener_puestos_compatibles(puesto_seleccionado, df)
        else:
            print("Selección inválida. Intenta nuevamente.")

    except Exception as e:
        print(f"Error inesperado: {e}")
