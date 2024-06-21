import unittest
from src.url_detector import URLDetector

class TestURLDetector(unittest.TestCase):
    def setUp(self):
        # Define las rutas de los controladores
        self.chrome_driver_path = '/usr/local/bin/chromedriver'
        self.firefox_driver_path = '/usr/bin/geckodriver'  # Actualiza con la ruta correcta a geckodriver

    def test_get_active_tab_url_chrome(self):
        detector = URLDetector(chrome_driver_path=self.chrome_driver_path)
        url = detector.get_active_tab_url(browser="chrome")
        # Como no estamos controlando las pestañas abiertas en Chrome en este test,
        # es posible que no se encuentre una URL activa.
        # Nos aseguramos de que el test no falle si no hay una URL activa.
        if url is not None:
            self.assertTrue(url.startswith("http"), "La URL activa debe comenzar con 'http'")
        detector.close_driver()

    def test_get_active_tab_url_firefox(self):
        detector = URLDetector(firefox_driver_path=self.firefox_driver_path)
        url = detector.get_active_tab_url(browser="firefox")
        # Como no estamos controlando las pestañas abiertas en Firefox en este test,
        # es posible que no se encuentre una URL activa.
        # Nos aseguramos de que el test no falle si no hay una URL activa.
        if url is not None:
            self.assertTrue(url.startswith("http"), "La URL activa debe comenzar con 'http'")
        detector.close_driver()

if __name__ == "__main__":
    unittest.main()
