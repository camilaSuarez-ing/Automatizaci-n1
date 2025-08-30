from collections import Counter
import json
import os

archivo = "frecuencias.json"

def procesar_resenas():
    n = int(input("¿Cuántas reseñas desea ingresar? (mínimo 3): "))
    if n < 3:
        print("Debe ingresar al menos 3 reseñas.")
        return []
    return [input(f"Ingrese la reseña {i+1}: ") for i in range(n)]

def cargar_diccionario():
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            return json.load(f)
    return {}

def guardar_diccionario(diccionario):
    with open(archivo, "w") as f:
        json.dump(diccionario, f)

def limpiar_texto(texto):
    texto = texto.lower()
    for signo in ".,!?":
        texto = texto.replace(signo, "")
        texto = texto.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    return texto

def main():

    frecuencia = cargar_diccionario()
    
    resenas = procesar_resenas()
    if not resenas:  # si la lista está vacía, terminar
        return

    # limpiar cada reseña
    resenas_limpias = [limpiar_texto(r) for r in resenas]

    # combinar y separar en palabras
    texto_combinado = " ".join(resenas_limpias)
    palabras = texto_combinado.split()

    # Crear diccionario de frecuencias
    # frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    guardar_diccionario(frecuencia) # guardar historial actualizado

    # Ordenar por frecuencia
    palabras_ordenadas = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)
    
    # contar y mostrar top 3
    conteo = Counter(palabras)
    print("\nLas 3 palabras más frecuentes en esta solicitud son:")
    for palabra, freq in conteo.most_common(3):
        print(f"{palabra}: {freq} veces")

    #contar top en historia
    print(f"las palabras más comunes en toda la historia son:")
    ordenado = dict(sorted(frecuencia.items(),
                    key=lambda x: x[1], reverse = True))
    contador = 0
    for palabra, freq in ordenado.items():
        print(f"{palabra}: {freq} veces")
        contador += 1
        if contador == 3:
            break

if __name__ == "__main__":
    main()