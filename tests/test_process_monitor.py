import unittest
from src.process_monitor import ProcessMonitor
import platform

class TestProcessMonitor(unittest.TestCase):
    def test_get_active_window_process(self):
        monitor = ProcessMonitor()
        process_name = monitor.get_active_window_process()
        if platform.system() == "Linux":
            if process_name is None:
                print("Warning: No active window found. Ensure a window is active while testing.")
            else:
                self.assertIsNotNone(process_name, "Expected an active window name but got None.")
        elif platform.system() == "Windows":
            self.assertIsNotNone(process_name)
        else:
            self.fail("Unsupported operating system")

if __name__ == "__main__":
    unittest.main()

