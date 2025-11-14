def iva_21(cant):
    
    return cant * 1.21

def iva_4(cant):
    
    return cant * 1.04

def desc_10(cant):
   
    return cant * 0.90
    
def no_desc(cant):
    return cant

lista_compra = [
    {
        "nombre": "Laptop",
        "precio": 1200.00,
        "desc_fn": desc_10,  
        "iva_fn": iva_21
    },
    {
        "nombre": "Libro",
        "precio": 20.00,
        "desc_fn": no_desc, 
        "iva_fn": iva_4
    },
    {
        "nombre": "Monitor",
        "precio": 350.00,
        "desc_fn": desc_10,
        "iva_fn": iva_21
    }
]




def calcular_cesta(cesta):
    total_pagar = 0
    total_iva = 0 
    total_desc = 0
    
    for prod in cesta:
        precio_inicial = prod['precio']
        
       
        desc_fn = prod['desc_fn']
        precio_desc = desc_fn(precio_inicial)
        
        desc_aplicado = precio_inicial - precio_desc
        
      
        iva_fn = prod['iva_fn']
        precio_final = iva_fn(precio_desc)
        
        iva_cobrado = precio_final - precio_desc
        
       
        total_pagar += precio_final
        total_iva += iva_cobrado
        total_desc += desc_aplicado
        
    return {
        "total_a_pagar": round(total_pagar, 2),
        "total_iva": round(total_iva, 2),
        "total_descuento": round(total_desc, 2)
    }