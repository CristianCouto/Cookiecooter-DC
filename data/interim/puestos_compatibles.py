import pandas as pd
import os

def obtener_puestos_compatibles(nombre_puesto):
    try:
        # Ruta fija al archivo en la carpeta "Processed"
        archivo = os.path.join(os.path.dirname(__file__), "..", "Processed", "Ocra-Newsan 1.42.xlsm")
        
        # Verificar si el archivo existe
        if not os.path.exists(archivo):
            print(f"Error: El archivo '{archivo}' no se encontró. Verifica que esté en la carpeta 'Processed'.")
            return
        
        # Cargar el archivo Excel y leer la hoja "Combinaciones 2"
        df = pd.read_excel(archivo, sheet_name='Combinaciones 2')
        
        # Filtrar los datos por el puesto especificado
        puestos_compatibles = df[df['Nombre puesto'] == nombre_puesto]['Puesto compatible']
        
        # Verificar si se encontraron resultados
        if puestos_compatibles.empty:
            print(f"No se encontraron puestos compatibles para el puesto '{nombre_puesto}'.")
        else:
            print(f"Puestos compatibles para '{nombre_puesto}':")
            for puesto in puestos_compatibles:
                print(f"- {puesto}")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

def listar_puestos(df):
    puestos_unicos = df['Nombre puesto'].unique()
    print("Lista de puestos disponibles:")
    for idx, puesto in enumerate(puestos_unicos):
        print(f"{idx + 1}. {puesto}")
    return puestos_unicos

if __name__ == '__main__':
    try:
        # Ruta fija al archivo en la carpeta "Processed"
        archivo = os.path.join(os.path.dirname(__file__), "..", "Processed", "Ocra-Newsan 1.42.xlsm")
        
        # Verificar si el archivo existe
        if not os.path.exists(archivo):
            print(f"Error: El archivo '{archivo}' no se encontró. Verifica que esté en la carpeta 'Processed'.")
            exit()
        
        # Cargar el archivo Excel y leer la hoja "Combinaciones 2"
        df = pd.read_excel(archivo, sheet_name='Combinaciones 2')
        
        # Mostrar lista de puestos y permitir selección
        puestos_unicos = listar_puestos(df)
        opcion = int(input("Selecciona un puesto ingresando el número correspondiente: "))
        if 1 <= opcion <= len(puestos_unicos):
            puesto_seleccionado = puestos_unicos[opcion - 1]
            print(f"Has seleccionado: {puesto_seleccionado}")
            obtener_puestos_compatibles(puesto_seleccionado)
        else:
            print("Número ingresado fuera de rango. Por favor, intenta nuevamente.")
    except Exception as e:
        print(f"Error general: {e}")
