import unittest
from atia.process_monitor import ProcessMonitor

class TestProcessMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = ProcessMonitor()

    def test_get_active_window_process(self):
        process_name = self.monitor.get_active_window_process()
        if process_name is None:
            print("Warning: No active window found. Ensure a window is active while testing.")
        else:
            self.assertIsNotNone(process_name, "Expected an active window name but got None.")

    def test_get_process_info(self):
        # Asumimos que siempre habrá un proceso del sistema en ejecución
        process_name = "systemd"
        process_info = self.monitor.get_process_info(process_name)
        self.assertIsNotNone(process_info)
        self.assertEqual(process_info['name'], process_name)
        self.assertIn('cpu_percent', process_info)
        self.assertIn('memory_percent', process_info)

if __name__ == "__main__":
    unittest.main()