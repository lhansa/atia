import psutil
import time
import datetime
import platform
import os

class ProcessMonitor:
    def __init__(self, interval=1):
        self.interval = interval
        self.active_process = None
        self.start_time = None
        self.system = platform.system()

    def get_active_window_process(self):
        if self.system == "Windows":
            return self._get_active_window_process_windows()
        elif self.system == "Linux":
            return self._get_active_window_process_linux()
        else:
            raise NotImplementedError(f"Unsupported operating system: {self.system}")

    def _get_active_window_process_windows(self):
        try:
            import win32gui
            window = win32gui.GetForegroundWindow()
            pid = win32gui.GetWindowThreadProcessId(window)[1]
            active_window = psutil.Process(pid)
            return active_window.name()
        except Exception as e:
            print(f"Error getting active window on Windows: {e}")
            return None

    def _get_active_window_process_linux(self):
        try:
            with os.popen('xdotool getactivewindow') as p:
                active_window_id = p.read().strip()
            if not active_window_id:
                return None
            with os.popen(f'xdotool getwindowname {active_window_id}') as p:
                active_window_name = p.read().strip()
            return active_window_name if active_window_name else None
        except Exception as e:
            print(f"Error getting active window on Linux: {e}")
            return None

    def monitor(self):
        while True:
            current_process = self.get_active_window_process()
            if current_process != self.active_process:
                if self.active_process:
                    duration = datetime.datetime.now() - self.start_time
                    print(f"{self.active_process} was active for {duration}")
                self.active_process = current_process
                self.start_time = datetime.datetime.now()
                print(f"Switched to {self.active_process}")
            time.sleep(self.interval)

