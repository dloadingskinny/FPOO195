def calc_iva(cant_sniva, porcentaje_iva=None):
    if porcentaje_iva is None:
        porcentaje_iva = 21
    
    total = cant_sniva + (cant_sniva * porcentaje_iva / 100)
    
    return total

cant_sniva = 100
total_factura = calc_iva(cant_sniva)
print(f"El total de la factura con un 21% de IVA es: {total_factura}")

porcentaje_iva_personalizado = 10
total_factura_personalizado = calc_iva(cant_sniva, porcentaje_iva_personalizado)
print(f"El total de la factura con un {porcentaje_iva_personalizado}% de IVA es: {total_factura_personalizado}")
