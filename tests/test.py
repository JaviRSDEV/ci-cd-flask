import unittest
from src.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Hello, World!")

    def test_welcome(self):
        result = self.app.get('/welcome')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Bienvenido Señor")

    def test_404_page(self):
        response = self.app.get('/ruta-que-no-existe')
        self.assertEqual(response.status_code, 404)

    def test_greet_user(self):
        nombre = "Javi"
        res = self.app.get(f'/user/{nombre}')
        self.assertEqual(res.status_code, 200)
        self.assertIn(f"Hola {nombre}", res.get_data(as_text=True))

    def test_get_status_json(self):
        res = self.app.get('/status')
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['status'], 'online')
        self.assertEqual(data['port'], 8000)

if __name__ == "__main__":
    unittest.main()