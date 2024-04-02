import os
import unittest
from main import extract_raw_text, process_pdfs

class TestMainFunctions(unittest.TestCase):
    def test_extract_raw_text(self):
        # define os caminhos de entrada e saída para um arquivo de teste
        input_path = "data/pdf/input_test.pdf"
        output_path = "data/raw/input_test.txt"
        
        # chama a função extract_raw_text com os caminhos de teste
        extract_raw_text(input_path, output_path)
        
        # verifica se o arquivo de saída foi criado
        self.assertTrue(os.path.exists(output_path))

    def test_process_pdfs(self):
        # chama a função process_pdfs com os diretórios de teste
        process_pdfs("data/pdf", "data/raw")

if __name__ == "__main__":
    unittest.main()
