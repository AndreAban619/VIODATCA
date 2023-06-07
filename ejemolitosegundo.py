cadena_original = "Hola mundo"
cadena_comparar = "Hola mundo y algo más"
palabras_no_corresponden = []

for palabra in cadena_comparar.split():
    if palabra not in cadena_original:
        palabras_no_corresponden.append(palabra)

print(palabras_no_corresponden)