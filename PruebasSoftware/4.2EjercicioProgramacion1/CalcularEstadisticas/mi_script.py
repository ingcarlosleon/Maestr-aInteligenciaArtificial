
# Aquí va todo tu código de Python
# Importaciones necesarias
import time
import sys
import math
import os

base_path = '/content/CalidadSoftware'

def calculate_mean(data):
  
    #Calcula la media de una lista de números.
    return sum(data) / len(data) if len(data) > 0 else 0

def calculate_median(data):
     #Calcula la mediana de una lista de números.
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2
    return sorted_data[n // 2]

def calculate_variance(data, mean):
 #Calcula la varianza de una lista de números.
 return sum((x - mean) ** 2 for x in data) / len(data) if len(data) > 0 else 0

def calculate_mode(data):
 #Calcula la moda de una lista de números.
 frequency = {}
 for num in data:
     frequency[num] = frequency.get(num, 0) + 1
 max_freq = max(frequency.values())
 modes = [k for k, v in frequency.items() if v == max_freq]
 return modes[0] if modes else None  # Devuelve la primera moda si existe


def calculate_standard_deviation(data, mean):
 variance = sum((x - mean) ** 2 for x in data) / len(data) if len(data) > 0 else 0
 return math.sqrt(variance)

def handle_invalid_data(data_str):
    """
    Maneja datos inválidos intentando convertirlos a float.
    Si la conversión falla, elimina los caracteres no numéricos y cuenta los datos.
    """
    try:
        return float(data_str)
    except ValueError:
        numeric_value = ''.join(char for char in data_str if char.isdigit() or char == '.')
        if numeric_value:
            print(f"Converted non-numeric data: {data_str} to {numeric_value}")
            return float(numeric_value)
        print(f"Ignoring invalid data: {data_str}")
        return None



def handle_invalid_data(data_str):
    
    #Maneja datos inválidos intentando convertirlos a float.
    #Si la conversión falla, elimina los caracteres no numéricos y cuenta los datos.
    
    try:
        return float(data_str)
    except ValueError:
        numeric_value = ''.join(char for char in data_str if char.isdigit() or char == '.')
        if numeric_value:
            print(f"Converted non-numeric data: {data_str} to {numeric_value}")
            return float(numeric_value)
        print(f"Ignoring invalid data: {data_str}")
        return None

def read_data_from_file(filename):
    
    #Lee datos de un archivo y maneja datos inválidos.
    #Devuelve una lista de valores numéricos.
    
    data = []
    with open(filename, 'r') as file:
        for line in file:
            for data_str in line.split():
                numeric_value = handle_invalid_data(data_str)
                if numeric_value is not None:
                    data.append(numeric_value)
    return data

    file_names = ['TC1.txt', 'TC2.txt', 'TC3.txt', 'TC4.txt', 'TC5.txt', 'TC6.txt', 'TC7.txt']

for file_name in file_names:
    file_path = f"{base_path}/{file_name}"
    print(file_path)
    print(f"Procesando {file_name}...")
    data = read_data_from_file(file_path)
    # Aquí puedes llamar a tus funciones de estadísticas como calculate_mean, calculate_median, etc.
    # Por ejemplo:
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    std_dev = calculate_standard_deviation(data, mean)

    # Mostrar resultados
    print(f"Media: {mean}, Mediana: {median}, Moda: {mode}, Desviación Estándar: {std_dev}")

    import time
import os
from datetime import datetime

def main():
    start_time = time.time()

    # Define la ruta base a tus archivos
    base_path = '/content/CalidadSoftware'
    file_names = ['TC1.txt', 'TC2.txt', 'TC3.txt', 'TC4.txt', 'TC5.txt', 'TC6.txt', 'TC7.txt']

    # Preparar los encabezados para los resultados
    headers = ["TC", "COUNT", "MEAN", "MEDIAN", "MODE", "SD", "VAR", "Elapsed Time", "Timestamp"]
    file_results = []

    # Procesar cada archivo
    for file_name in file_names:
        file_path = os.path.join(base_path, file_name)
        print(f"Procesando {file_name}...")

        # Llama aquí a tus funciones de procesamiento de datos
        # Por ejemplo: data = read_data_from_file(file_path)
        # mean, median, mode, std_dev = tus funciones de cálculo de estadísticas

        # Simula resultados (reemplaza con tus cálculos reales)
        result = [file_name, len(data), mean, median, mode, std_dev, "variance", time.time() - start_time, datetime.now()]
        file_results.append(result)

    # Mostrar y guardar los resultados
    for row in file_results:
        print('	'.join(map(str, row)))

    # Al final de tu función main, donde guardas los resultados
    result_file_path = os.path.join(base_path, 'StatisticsResults.txt')

    with open(result_file_path, 'w', encoding='utf-8') as f:
        # Escribir los encabezados
        f.write('	'.join(headers) + '')
        # Escribir los datos
        for row in file_results:
            f.write('	'.join(map(str, row)) + '')
    print(f"Results saved to {result_file_path}")

    # Medir y mostrar el tiempo transcurrido
    elapsed_time = time.time() - start_time
    print(f"Tiempo total transcurrido: {elapsed_time} segundos.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()