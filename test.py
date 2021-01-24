import unittest
import javaneseDate as jd

class TestJavaneseDate(unittest.TestCase):
    def test_awal_tahun(self):
        self.assertEqual(jd.JavaneseDate().format(), 'Selasa Pon, 1 Sura 1867')

if __name__ == '__main__':
    unittest.main()