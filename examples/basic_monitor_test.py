#!/usr/bin/env python3
"""
Ejemplo básico de uso de Atia (Activity Time Analysis)

Este script demuestra las diferentes formas de usar el monitor de actividad:
1. Monitoreo con duración fija
2. Monitoreo manual (hasta Ctrl+C)
3. Lectura básica de los resultados
"""

from atia.process_monitor import monitor_activity
import pandas as pd
from datetime import timedelta
import time

def ejemplo_duracion_fija():
    """Ejemplo de monitoreo con duración predeterminada"""
    print("\n=== Ejemplo 1: Monitoreo por 10 segundos ===")
    print("Cambia entre diferentes aplicaciones...")
    
    monitor_activity(duration=10)
    
    print("Monitoreo completado!")

def ejemplo_monitoreo_manual():
    """Ejemplo de monitoreo hasta que el usuario lo detenga"""
    print("\n=== Ejemplo 2: Monitoreo manual (Ctrl+C para detener) ===")
    print("Cambia entre diferentes aplicaciones...")
    
    try:
        monitor_activity(duration=None)
    except KeyboardInterrupt:
        print("\nMonitoreo detenido por el usuario")

def mostrar_resultados():
    """Ejemplo de cómo leer y mostrar los resultados"""
    print("\n=== Resultados del monitoreo ===")
    try:
        # Leemos el archivo de log
        df = pd.read_csv('activity_log.csv', parse_dates=['timestamp'])
        
        # Mostramos las últimas 5 entradas
        print("\nÚltimas 5 actividades registradas:")
        print(df.tail().to_string(index=False))
        
        # Calculamos tiempo total por aplicación
        df['duration'] = df.groupby('app')['timestamp'].diff().shift(-1)
        df.loc[df['event'] == 'end', 'duration'] = pd.NaT
        df['duration'] = df['duration'].dt.total_seconds()
        
        app_usage = df.groupby('app')['duration'].sum()
        app_usage = app_usage.apply(lambda x: str(timedelta(seconds=int(x))))
        
        print("\nTiempo total por aplicación:")
        print(app_usage.to_string())
        
    except FileNotFoundError:
        print("No se encontró el archivo activity_log.csv")
    except Exception as e:
        print(f"Error al leer los resultados: {e}")

def main():
    print("=== Demo de Atia (Activity Time Analysis) ===")
    print("Este ejemplo muestra diferentes formas de usar el monitor de actividad.")
    
    # Ejemplo 1: Monitoreo con duración fija
    ejemplo_duracion_fija()
    
    # Mostramos los resultados
    mostrar_resultados()
    
    # Ejemplo 2: Podríamos descomentar esto para probar el monitoreo manual
    # print("\n¿Quieres probar el monitoreo manual? (Ctrl+C para detener)")
    # input("Presiona Enter para continuar...")
    # ejemplo_monitoreo_manual()
    # mostrar_resultados()

if __name__ == "__main__":
    main()