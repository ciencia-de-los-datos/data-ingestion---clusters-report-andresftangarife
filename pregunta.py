"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    import re
    data = open("clusters_report.txt", 'r')
    lines = data.readlines()
    #Eliminar saltos
    no_jumps = []
    for line in lines:
        line = line.strip()
        no_jumps.append([line.strip("\n")])

        # Eliminar elementos vaciós
    no_empty = []
    for line in no_jumps:
        for elemento in line:
            if len(elemento) != 0:
                no_empty.append([elemento])

    lista_final = []
    linea_axu = ""
    for line in no_empty:
        if line[0][0].isdigit():
            linea_axu = ""
            linea_axu = line[0]
        else:
            linea_axu = linea_axu + " " +line[0]
        lista_final.append(linea_axu)

    filas_mas_largas = {}

    for fila in lista_final:
        valor = fila.split()[0]
        if valor in filas_mas_largas:
            if len(fila) > len(filas_mas_largas[valor]):
                filas_mas_largas[valor] = fila
        else:
            filas_mas_largas[valor] = fila

    lista_de_valores = list(filas_mas_largas.values())

    cluster = []
    cantidad_de_palabras_clave = []
    porcentaje_de_palabras_clave = []
    columna4 = []

    regex = r'^(\d+)\s+(\d+)\s+(\d+,\d+\s*%)\s+(.*)$'

    for linea in lista_de_valores:
        match = re.match(regex, linea)
        if match:
            cluster.append(int(match.group(1)))
            cantidad_de_palabras_clave.append(int(match.group(2)))
            porcentaje_de_palabras_clave.append(float(match.group(3).replace(' %', '').replace(",", ".")))
            columna4.append(match.group(4).replace("  ", " ").replace(".",""))
    
    col_1 = []
    col_2 = []
    principales_palabras_clave = []
    for parrafo in columna4:
        col_1 = parrafo.split(",")
        col_2 = []
        for palabra in col_1:
            palabra = palabra.strip()
            palabra = palabra.replace("  ", " ")
            col_2.append(palabra)
        col_2 = ", ".join(col_2)
        principales_palabras_clave.append(col_2)
    
    principales_palabras_clave[12] = principales_palabras_clave[12].replace("  ", " ")
    
    df = pd.DataFrame(data= {"cluster" : cluster, 
                         "cantidad_de_palabras_clave" : cantidad_de_palabras_clave, 
                         "porcentaje_de_palabras_clave" : porcentaje_de_palabras_clave, 
                         "principales_palabras_clave" : principales_palabras_clave
                        })

    return df