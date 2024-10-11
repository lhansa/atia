from src.process_monitor import ProcessMonitor
import time

def main():
    monitor = ProcessMonitor()
    
    print("Monitoreo de procesos activos:")
    for _ in range(10):  # Monitorear durante 10 iteraciones
        active_process = monitor.get_active_window_process()
        if active_process:
            print(f"Proceso activo: {active_process}")
            process_info = monitor.get_process_info(active_process)
            if process_info:
                print(f"  CPU: {process_info['cpu_percent']}%")
                print(f"  Memoria: {process_info['memory_percent']}%")
        else:
            print("No se pudo detectar el proceso activo")
        
        time.sleep(2)  # Esperar 2 segundos antes de la siguiente comprobación

if __name__ == "__main__":
    main()
