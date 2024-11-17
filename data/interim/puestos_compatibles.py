import pandas as pd
import os

def listar_puestos(df):
    """
    Función que lista los puestos disponibles con sus IDs y devuelve la lista única de puestos.
    """
    puestos_unicos = df['Nombre puesto'].unique()
    print("Lista de puestos disponibles:")
    for idx, puesto in enumerate(puestos_unicos):
        print(f"{idx + 1}. {puesto}")
    return puestos_unicos

def obtener_puestos_compatibles(nombre_puesto, df):
    """
    Función para mostrar los puestos compatibles con el puesto seleccionado.
    """
    # Filtrar los datos por el puesto especificado
    puestos_compatibles = df[df['Nombre puesto'] == nombre_puesto]['Puesto compatible']
    
    # Verificar si se encontraron resultados
    if puestos_compatibles.empty:
        print(f"\nNo se encontraron puestos compatibles para el puesto '{nombre_puesto}'.")
    else:
        print(f"\nPuestos compatibles para '{nombre_puesto}' ({len(puestos_compatibles)} en total):")
        for puesto in puestos_compatibles:
            print(f"- {puesto}")

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
        
        # Mostrar la lista de puestos
        puestos_unicos = listar_puestos(df)
        
        # Solicitar la selección del puesto
        opcion = int(input("\nSelecciona un puesto para saber su combinacion: "))
        
        # Validar la opción seleccionada
        if 1 <= opcion <= len(puestos_unicos):
            puesto_seleccionado = puestos_unicos[opcion - 1]
            # Mostrar los puestos compatibles
            obtener_puestos_compatibles(puesto_seleccionado, df)
        else:
            print("Número ingresado fuera de rango. Por favor, intenta nuevamente.")
    except Exception as e:
        print(f"\nError general: {e}")
