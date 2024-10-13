import platform
import psutil
from datetime import datetime
import csv
import os
import time
from abc import ABC, abstractmethod


class SystemMonitor(ABC):
    @abstractmethod
    def get_active_window_process(self):
        pass

class LinuxMonitor(SystemMonitor):
    def __init__(self):
        from Xlib import display
        self.display = display.Display()

    def get_active_window_process(self):
        try:
            window = self.display.get_input_focus().focus
            window_class = window.get_wm_class()
            if window_class is not None:
                return window_class[1]
        except Exception as e:
            print(f"Error al obtener la ventana activa: {e}")
        return None

class WindowsMonitor(SystemMonitor):
    def __init__(self):
        import win32gui
        import win32process
        self.win32gui = win32gui
        self.win32process = win32process

    def get_active_window_process(self):
        try:
            window = self.win32gui.GetForegroundWindow()
            _, pid = self.win32process.GetWindowThreadProcessId(window)
            return self.win32process.GetProcessImageFileName(pid)
        except Exception as e:
            print(f"Error al obtener la ventana activa en Windows: {e}")
        return None

class ProcessMonitor:
    def __init__(self):
        if platform.system() == "Linux":
            self.system_monitor = LinuxMonitor()
        elif platform.system() == "Windows":
            self.system_monitor = WindowsMonitor()
        else:
            raise NotImplementedError("Sistema operativo no soportado")

    def get_active_window_process(self):
        return self.system_monitor.get_active_window_process()

    def get_process_info(self, process_name):
        for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
            if proc.info['name'] == process_name:
                return {
                      'name': proc.info['name'],
                      'cpu_percent': proc.info['cpu_percent'],
                      'memory_percent': proc.info['memory_percent']
                  }
        return None

class ActivityLogger:
    def __init__(self, filename="activity_log.csv"):
        self.filename = filename
        self.ensure_csv_exists()

    def ensure_csv_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['timestamp', 'app', 'event'])

    def log_activity(self, app, event):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, app, event])

def monitor_activity(duration=None):
    monitor = ProcessMonitor()
    logger = ActivityLogger()
    
    start_time = datetime.now()
    last_app = None

    try:
        while True:
            current_app = monitor.get_active_window_process()
            
            if current_app != last_app:
                if last_app:
                    logger.log_activity(last_app, 'end')
                if current_app:
                    logger.log_activity(current_app, 'start')
                last_app = current_app

            if duration and (datetime.now() - start_time).total_seconds() >= duration:
                break
            
            time.sleep(1)  # Pequeña pausa para reducir el uso de CPU
    except KeyboardInterrupt:
        if last_app:
            logger.log_activity(last_app, 'end')
        print("\nMonitoreo interrumpido por el usuario.")
    finally:
        if last_app:
            logger.log_activity(last_app, 'end')

if __name__ == "__main__":
    monitor_activity()
