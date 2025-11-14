'''
    cada produto na cesta da compra leve consigo as 
    instrucións (funcións) de como debe ser calculado.
    
    shopping_list : 
        precio
        desconto
        ive_fin
    
'''
def calcular_iva_21(cantidade):
    return cantidade * 1.21

def calcular_iva_4(cantidade):
    return cantidade * 1.04

def aplicar_descuento_10(cantidade):
    return cantidade * 0.90
    
def non_aplicar_descuento(cantidade):
    return cantidade

lista_compra = [
    {
        "nome": "Laptop",
        "prezo_base": 1200.00,
        "desconto_fn": aplicar_descuento_10, 
        "ive_fn": calcular_iva_21
    },
    {
        "nome": "Libro",
        "prezo_base": 20.00,
        "desconto_fn": non_aplicar_descuento, 
        "ive_fn": calcular_iva_4
    },
    {
        "nome": "Monitor",
        "prezo_base": 350.00,
        "desconto_fn": aplicar_descuento_10,
        "ive_fn": calcular_iva_21
    }
]

def calcular_cesta(cesta):
    total_a_pagar = 0
    total_ive_cobrado = 0 
    total_desconto_aplicado = 0
    
    for produto in cesta:
        prezo_inicial = produto['prezo_base']
        
        desconto_fn = produto['desconto_fn']
        prezo_cn_desconto = desconto_fn(prezo_inicial)
        
        cn_desconto = prezo_inicial - prezo_cn_desconto
        
        ive_fn = produto['ive_fn']
        prezo_final = ive_fn(prezo_cn_desconto)
        
        ive_cobrado = prezo_final - prezo_cn_desconto
        
        total_a_pagar += prezo_final
        total_ive_cobrado += ive_cobrado
        total_desconto_aplicado += cn_desconto
        
    return {
        "total_a_pagar": round(total_a_pagar, 2),
        "total_ive": round(total_ive_cobrado, 2),
        "total_desconto": round(total_desconto_aplicado, 2)
    }

