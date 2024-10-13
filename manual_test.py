from src.process_monitor import monitor_activity
import time

def main():
    print("Iniciando monitoreo de actividad...")
    print("Cambia entre diferentes aplicaciones durante los próximos 60 segundos.")
    print("El registro se guardará en 'activity_log.csv'.")
    
    monitor_activity(duration=60)
    
    print("\nMonitoreo completado. Revisa 'activity_log.csv' para ver los resultados.")

if __name__ == "__main__":
    main()
