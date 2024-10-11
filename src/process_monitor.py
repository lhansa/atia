import psutil
from Xlib import display

class ProcessMonitor:
    def __init__(self):
        self.display = display.Display()

    def get_active_window_process(self):
        try:
            window = self.display.get_input_focus().focus
            window_class = window.get_wm_class()
            if window_class is not None:
                process_name = window_class[1]
                return process_name
        except Exception as e:
            print(f"Error al obtener la ventana activa: {e}")
        return None

    def get_process_info(self, process_name):
        for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
            if proc.info['name'] == process_name:
                return {
                    'name': proc.info['name'],
                    'cpu_percent': proc.info['cpu_percent'],
                    'memory_percent': proc.info['memory_percent']
                }
        return None