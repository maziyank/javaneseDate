import unittest
import javaneseDate as jd

class TestJavaneseDate(unittest.TestCase):
    def test_nama_tahun(self):
        self.assertEqual(jd.JavaneseDate().tahun.name, 'Alip')

    def test_awal_tahun(self):
        self.assertEqual(jd.JavaneseDate().format(), 'Selasa Pon, 1 Sura 1867')

    def test_parluji(self):
        self.assertEqual(jd.JavaneseDate(1867,2,1).format(), 'Kemis Pon, 1 Sapar 1867')        

    def test_nguwalpatma(self):
        self.assertEqual(jd.JavaneseDate(1867,2,1).format(), 'Jemah Pahing, 1 Mulud 1867')        

if __name__ == '__main__':
    unittest.main()