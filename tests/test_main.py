import pytest
from ..src.ejercicio43.main  import calcular_cesta, calcular_ive_21, aplicar_desconto_10, non_aplicar_desconto, calcular_ive_4
# NOTA: Cambia 'o_teu_ficheiro_principal' polo nome real do teu ficheiro (.main, por exemplo)

def test_funcion_ive_21():
    """Verifica que a función de IVE 21% calcula o valor correcto."""
    assert round(calcular_ive_21(100.00), 2) == 121.00
    assert round(calcular_ive_21(50.00), 2) == 60.50

def test_funcion_ive_4():
    """Verifica que a función de IVE 4% calcula o valor correcto."""
    assert round(calcular_ive_4(100.00), 2) == 104.00
    assert round(calcular_ive_4(25.00), 2) == 26.00

def test_funcion_desconto_10():
    """Verifica que a función de desconto do 10% calcula o valor correcto."""
    assert round(aplicar_desconto_10(100.00), 2) == 90.00
    assert round(aplicar_desconto_10(20.00), 2) == 18.00

def test_funcion_non_desconto():
    """Verifica que a función de non_desconto non altera o valor."""
    assert non_aplicar_desconto(55.00) == 55.00

def test_cesta_simple_sen_desconto():
    """Testa unha cesta sen descontos, só IVE."""
    cesta_simple = [
        {"nome": "Produto A", "prezo_base": 100.00, "desconto_fn": non_aplicar_desconto, "ive_fn": calcular_ive_21},
    ]
    resultado = calcular_cesta(cesta_simple)
    
    # 100.00 * 1.21 = 121.00
    # IVE = 21.00
    assert resultado['total_a_pagar'] == 121.00
    assert resultado['total_ive'] == 21.00
    assert resultado['total_desconto'] == 0.00

def test_cesta_complexa():
    """Testa a cesta de exemplo con descontos e diferentes IVES."""
    cesta_complexa = [
        # Produto 1: 100 - 10% (90) + 21% IVE = 108.90
        {"nome": "P1", "prezo_base": 100.00, "desconto_fn": aplicar_desconto_10, "ive_fn": calcular_ive_21},
        # Produto 2: 50 + 4% IVE = 52.00
        {"nome": "P2", "prezo_base": 50.00, "desconto_fn": non_aplicar_desconto, "ive_fn": calcular_ive_4},
    ]
    resultado = calcular_cesta(cesta_complexa)
    
    # Totais esperados:
    # Total a pagar: 108.90 + 52.00 = 160.90
    # Total IVE: 18.90 (do P1) + 2.00 (do P2) = 20.90
    # Total Desconto: 10.00 (do P1) + 0.00 (do P2) = 10.00

    assert resultado['total_a_pagar'] == 160.90
    assert resultado['total_ive'] == 20.90
    assert resultado['total_desconto'] == 10.00