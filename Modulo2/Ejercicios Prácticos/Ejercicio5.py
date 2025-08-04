#Conversor de Monedas

from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

# Tasas de cambio 
exchange_rates = {
    ('USD', 'EUR'): Decimal('0.93'),
    ('USD', 'MXN'): Decimal('16.70'),
    ('EUR', 'USD'): Decimal('1.08'),
    ('EUR', 'MXN'): Decimal('18.00'),
    ('MXN', 'USD'): Decimal('0.060'),
    ('MXN', 'EUR'): Decimal('0.056'),
}

def convertir(moneda_origen, moneda_destino, cantidad):
    try:
        cantidad_decimal = Decimal(cantidad)
    except InvalidOperation:
        return "Cantidad inválida."

    monedas = [moneda_origen, moneda_destino]
    if any(m not in ['USD', 'EUR', 'MXN'] for m in monedas):
        return "Moneda no soportada."

    if moneda_origen == moneda_destino:
        return f"{cantidad_decimal.quantize(Decimal('0.01'))} {moneda_destino}"

    tasa = exchange_rates.get((moneda_origen, moneda_destino))
    if not tasa:
        return "Conversión no disponible."
    resultado = cantidad_decimal * tasa
    resultado = resultado.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return f"{cantidad_decimal} {moneda_origen} = {resultado} {moneda_destino}"

origen = input("Moneda origen (USD, EUR, MXN): ").upper()
destino = input("Moneda destino (USD, EUR, MXN): ").upper()
cantidad = input("Cantidad a convertir: ")

conversion = convertir(origen, destino, cantidad)
print(conversion)

