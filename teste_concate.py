import unittest 
  
  def  string1 = "Olá"
      string2 = "mundo"
      concatenada = string1 + " " + string2

class Teste(unittest.TestCase):
    def test_concatenar(self):
        self.assertEqual("Olá mundo")

if __name__ == '__main__':
     unittest.main()
