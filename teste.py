from unittest import TestCase, main
from codigo import caixa_eletronico

class TestCaixaEletronico(TestCase):
    def test_quero_5_reais(self):
        self.assertEquals(caixa_eletronico(5), "1 nota 5 reais")
    
    def test_quero_10_reais(self):
        self.assertEquals(caixa_eletronico(10), "1 nota 10 reais")
        
    def test_quero_15_reais(self):
        self.assertEquals(caixa_eletronico(15), "1 nota 5 reais, 1 nota 10 reais")
    
    def test_quero_25_reais(self):
        self.assertEquals(caixa_eletronico(25), "1 nota 5 reais, 1 nota 20 reais")    

    def test_quero_30_reais(self):
        self.assertEquals(caixa_eletronico(30), "1 nota 10 reais, 1 nota 20 reais")
main()