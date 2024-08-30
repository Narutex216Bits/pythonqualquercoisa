import unittest 
  
class TestStringMethods(unittest.TestCase): 
    
    def test_testemaiornumero(self): 
        primeiro = 15
        segundo = 27

        messagem = "primeiro valor não é maior que o segundo valor"
   
        self.assertGreater(primeiro, segundo, messagem) 
  
if __name__ == '__main__': 
    unittest.main()