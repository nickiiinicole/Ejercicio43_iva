import pytest
from ..src.ejercicio43.main import calcular_cesta, iva_21, desc_10, no_desc, iva_4

def test_funcion_iva_21():
    assert round(iva_21(100.00), 2) == 121.00
    assert round(iva_21(50.00), 2) == 60.50

def test_funcion_iva_4():
    assert round(iva_4(100.00), 2) == 104.00
    assert round(iva_4(25.00), 2) == 26.00

def test_funcion_descuento_10():
    assert round(desc_10(100.00), 2) == 90.00
    assert round(desc_10(20.00), 2) == 18.00

def test_funcion_no_descuento():
    assert no_desc(55.00) == 55.00


def test_cesta_simple_sin_descuento():
    cesta_simple = [
        {"nombre": "Produto A", "precio": 100.00, "desc_fn": no_desc, "iva_fn": iva_21},
    ]
    resultado = calcular_cesta(cesta_simple)
    
    assert resultado['total_a_pagar'] == 121.00
    assert resultado['total_iva'] == 21.00
    assert resultado['total_descuento'] == 0.00

def test_cestas_completas():
    cesta_completa_1 = [
        {"nombre": "P1", "precio": 100.00, "desc_fn": desc_10, "iva_fn": iva_21},
        {"nombre": "P2", "precio": 50.00, "desc_fn": no_desc, "iva_fn": iva_4},
    ]
   
    cesta_completa_2 = [
        {"nombre": "P1", "precio": 30.00, "desc_fn": desc_10, "iva_fn": iva_21},  # 30 * 0.9 * 1.21 = 32.67 (Desc: 3.00, IVA: 5.67)
        {"nombre": "P2", "precio": 389.00, "desc_fn": no_desc, "iva_fn": iva_4}, # 389 * 1.04 = 404.56 (Desc: 0.00, IVA: 15.56)
        {"nombre": "P3", "precio": 43.00, "desc_fn": desc_10, "iva_fn": iva_21},  # 43 * 0.9 * 1.21 = 46.80 (Desc: 4.30, IVA: 4.78)
        {"nombre": "P4", "precio": 21.00, "desc_fn": no_desc, "iva_fn": iva_4},  # 21 * 1.04 = 21.84 (Desc: 0.00, IVA: 0.84)
    ]
    
    resultado1 = calcular_cesta(cesta_completa_1)
    assert resultado1['total_a_pagar'] == 160.90
    assert resultado1['total_iva'] == 20.90
    assert resultado1['total_descuento'] == 10.00
    
    resultado2 = calcular_cesta(cesta_completa_2)
    
    # Totales esperados:D
    # Pagar: 32.67 + 404.56 + 46.80 + 21.84 = 505.87
    # IVA: 5.67 + 15.56 + 4.78 + 0.84 = 26.85
    # Descuento: 3.00 + 0.00 + 4.30 + 0.00 = 7.30
    
    assert resultado2['total_a_pagar'] == 505.87
    assert resultado2['total_iva'] == 26.85
    assert resultado2['total_descuento'] == 7.30