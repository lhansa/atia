import argparse
import time
from src.process_monitor import monitor_activity, ActivityLogger
import pandas as pd
from datetime import datetime, timedelta

def start_monitoring(duration=None):
    print("Iniciando monitoreo de actividad...")
    if duration:
        print(f"El monitoreo se detendrá automáticamente después de {duration} segundos.")
    else:
        print("Presiona Ctrl+C para detener el monitoreo.")
    
    try:
        monitor_activity(duration)
    except KeyboardInterrupt:
        print("\nMonitoreo detenido por el usuario.")
    
    print("Monitoreo completado. Los datos se han guardado en 'activity_log.csv'.")

def generate_report():
    df = pd.read_csv('activity_log.csv', parse_dates=['timestamp'])
    
    # Calculamos la duración de cada sesión
    df['duration'] = df.groupby('app')['timestamp'].diff().shift(-1)
    df.loc[df['event'] == 'end', 'duration'] = pd.NaT
    
    # Convertimos la duración a segundos
    df['duration'] = df['duration'].dt.total_seconds()
    
    # Agrupamos por aplicación y sumamos las duraciones
    app_usage = df.groupby('app')['duration'].sum()
    
    # Convertimos los segundos a un formato más legible
    app_usage = app_usage.apply(lambda x: str(timedelta(seconds=int(x))))
    
    print("\nInforme de uso de aplicaciones:")
    print(app_usage)

def main():
    parser = argparse.ArgumentParser(description="Monitor de actividad de aplicaciones")
    parser.add_argument('action', choices=['start', 'report'], help="Acción a realizar")
    parser.add_argument('-d', '--duration', type=int, help="Duración del monitoreo en segundos")
    
    args = parser.parse_args()
    
    if args.action == 'start':
        start_monitoring(args.duration)
    elif args.action == 'report':
        generate_report()

if __name__ == "__main__":
    main()