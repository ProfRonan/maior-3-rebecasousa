"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_012(self):
        """Função que testa com 0 1 e 2."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['0', '1', '2']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 3
            mock_print.assert_called_with('2.0')

    def test_321(self):
        """Função que testa com 3 2 e 1."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['3', '2', '1']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 3
            mock_print.assert_called_with('3.0')

    def test_201(self):
        """Função que testa com 2 0 e 1."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['2', '0', '1']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 3
            mock_print.assert_called_with('2.0')

    def test_240312(self):
        """Função que testa com 2.4 0.3 e 1.2."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['2.4', '0.3', '1.2']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 3
            mock_print.assert_called_with('2.4')


if __name__ == '__main__':
    unittest.main()
