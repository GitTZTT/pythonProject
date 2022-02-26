import unittest
import myProgram as prog

class Test(unittest.TestCase):
    def test_code(self):
        self.assertEqual(prog.r.status_code, 200)
    def test_url(self):
        self.assertEqual(prog.url, 'https://www.tp.edu.sg/')
    def test_header(self):
        self.assertEqual(prog.headers, {'User-Agent': 'Mobile'})
if __name__ == '_TestCase_':
    unittest.TestCase()