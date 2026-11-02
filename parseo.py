def parsear_producto(linea: str):
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        dict: {"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    
    if type(linea) != str:
        raise ValueError("La línea debe ser un string")

    elementos = linea.split(",")    
    if len(elementos) != 4:
        raise ValueError("La línea debe tener 4 elementos")
    codigo = elementos[0].strip()
    nombre = elementos[1].strip()
    precio = elementos[2].strip()
    cantidad = elementos[3].strip()

    try:
        precio = float(precio)
        cantidad = int(cantidad)
    except:
        raise ValueError("El precio y la cantidad deben ser números válidos")

    if precio <= 0 or cantidad <= 0:
        raise ValueError("El precio y la cantidad deben ser valores positivos")

    return {"codigo" : codigo, "nombre" : nombre, "precio" : precio, "cantidad" : cantidad}



def resumen_de_producto(linea: str) -> str:
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        str: "CODIGO - NOMBRE: $VALOR" (VALOR = precio*cantidad redondeado a 1 decimal)
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    
    diccionario = parsear_producto(linea)
    valor = round(diccionario["cantidad"] * diccionario["precio"],1)

    return(f" {diccionario['codigo']} - {diccionario['nombre']}: ${valor}")

def _validar_lineas(lineas: list):
    if type(lineas) != list:
        raise ValueError("Líneas debe ser una lista")
    for linea in lineas:
        if type(linea) != str:
            raise ValueError("Cada elemento de la lista debe ser un string")
        
def resumen_de_lotes(lineas: list) -> list:
    """
    Entrada:
        lines: list de str, no vacía
    Salida:
        list de str con resúmenes por producto (usa resumen_de_producto)
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    _validar_lineas(lineas)
    lista_resumenes = []
    for linea in lineas:
        lista_resumenes.append(resumen_de_producto(linea))
    return lista_resumenes


def valor_de_lote(lineas: list) -> float:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        float: valor total (suma de precio*cantidad) redondeado a 1 decimal
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'
    _validar_lineas(lineas)
    total = 0.0
    for linea in lineas:
        diccionario = parsear_producto(linea)
        valor = diccionario["cantidad"] * diccionario["precio"]
        total += valor
    return round(total,1)


def producto_maximo_valor(lineas: list) -> str:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        str: resumen del producto de mayor (precio*cantidad). En empate, el primero.
    """
    # Tu código empieza aquí. Recuerda eliminar el 'pass'\
    _validar_lineas(lineas)
    mejor_linea = lineas[0]
    mejor_valor = valor_de_lote([mejor_linea])
    datos_mejor = parsear_producto(mejor_linea)

    for linea in lineas[1:]:
        datos = parsear_producto(linea)
        valor_actual = datos["cantidad"] * datos["precio"]

        if valor_actual > mejor_valor:
            mejor_linea = linea
            mejor_valor = valor_actual
            datos_mejor = parsear_producto(linea)

    return resumen_de_producto(mejor_linea)

if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10"
    ]
    # ejemplos rápidos para visualizar (descomenta cuando implementes)
    # print(resumen_de_producto(products[0]))       # "P001 - Lapiz: $50.0"
    # print(resumen_de_lotes(products))             # ["P001 - ...", "P002 - ...", "P003 - ..."]
    # print(valor_de_lote(products))                # 126.0
    # print(producto_maximo_valor(products))        # "P002 - Cuaderno: $62.5"
    print(resumen_de_producto(products[0]))       # "P001 - Lapiz: $50.0"
    print(resumen_de_lotes(products))             # ["P001 - ...", "P002 - ...", "P003 - ..."]
    print(valor_de_lote(products))                # 126.0
    print(producto_maximo_valor(products))        # "P002 - Cuaderno: $62.5"