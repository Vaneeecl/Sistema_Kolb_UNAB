from pathlib import Path

import joblib
import pandas as pd

# =====================================================
# RUTA DE LA CARPETA DEL MODELO
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODELO_DIR = BASE_DIR / "model"

# =====================================================
# CARGA DE ARCHIVOS
# =====================================================

modelo = joblib.load(MODELO_DIR / "modelo_final.pkl")
label_encoder = joblib.load(MODELO_DIR / "label_encoder.pkl")
variables_modelo = joblib.load(MODELO_DIR / "variables_modelo.pkl")


# =====================================================
# PREPARAR DATOS PERSONALES
# =====================================================

def preparar_datos(datos):

    datos = datos.copy()

    # Codificar género
    if datos["GENERO"] == "Masculino":
        datos["GENERO"] = 1
    else:
        datos["GENERO"] = 0

    # Codificar colegio
    if datos["COLEGIO"] == "Público":
        datos["COLEGIO"] = 1
    else:
        datos["COLEGIO"] = 0

    return datos


# =====================================================
# CREAR DATAFRAME
# =====================================================

def crear_dataframe(datos):

    df = pd.DataFrame([datos])

    return df


# =====================================================
# CONVERTIR RESPUESTAS DEL CUESTIONARIO
# =====================================================

def convertir_respuestas(respuestas):

    equivalencias = {
        "Me identifica totalmente": 4,
        "Me identifica con frecuencia": 3,
        "Me identifica poco": 2,
        "No me identifica": 1
    }

    respuestas_numericas = {}

    for pregunta, respuesta in respuestas.items():
        respuestas_numericas[pregunta] = equivalencias[respuesta]

    return respuestas_numericas


# =====================================================
# UNIR DATOS PERSONALES Y RESPUESTAS
# =====================================================

def unir_datos(datos_personales, respuestas):

    datos = datos_personales.copy()

    datos.update(respuestas)

    return datos


# =====================================================
# PREPARAR DATAFRAME PARA EL MODELO
# =====================================================

def preparar_dataframe_modelo(datos_completos):

    # Crear DataFrame con una sola fila
    df = pd.DataFrame([datos_completos])

    # Agregar las variables que falten
    for variable in variables_modelo:
        if variable not in df.columns:
            df[variable] = 0

    # Ordenar exactamente como espera el modelo
    df = df[variables_modelo]

    return df


# =====================================================
# REALIZAR PREDICCIÓN
# =====================================================

def realizar_prediccion(df):

    prediccion = modelo.predict(df)

    probabilidades = modelo.predict_proba(df)

    estilo = label_encoder.inverse_transform(prediccion)[0]

    return estilo, probabilidades[0]


# =====================================================
# FUNCIÓN PRINCIPAL DE PREDICCIÓN
# =====================================================
def predecir_estilo(datos_personales, respuestas):

    # Preparar datos personales
    datos = preparar_datos(datos_personales)

    # Convertir respuestas del cuestionario
    respuestas_numericas = convertir_respuestas(respuestas)

    # Unir toda la información
    datos_completos = unir_datos(datos, respuestas_numericas)

    # Crear DataFrame
    df = preparar_dataframe_modelo(datos_completos)

    # Realizar predicción
    estilo, probabilidades = realizar_prediccion(df)

    return estilo, probabilidades


# =====================================================
# PRUEBA DEL MÓDULO
# =====================================================

if __name__ == "__main__":

    print("===================================")
    print("PRUEBA DEL MÓDULO DE PREDICCIÓN")
    print("===================================")

    # ---------------------------------
    # Datos personales
    # ---------------------------------

    estudiante = {
        "EDAD": 20,
        "GENERO": "Masculino",
        "COLEGIO": "Público",
        "PROMEDIO ACADEMICO ACTUAL": 4.5
    }

    datos = preparar_datos(estudiante)

    print("\nDatos personales preparados:")
    print(datos)

    # ---------------------------------
    # DataFrame
    # ---------------------------------

    df = crear_dataframe(datos)

    print("\nDataFrame generado:")
    print(df)

    # ---------------------------------
    # Respuestas del cuestionario
    # ---------------------------------

    respuestas = {
        "EC2": "Me identifica totalmente",
        "EC3": "Me identifica poco",
        "EA9": "No me identifica"
    }

    print("\nRespuestas originales:")
    print(respuestas)

    respuestas_numericas = convertir_respuestas(respuestas)

    print("\nRespuestas convertidas:")
    print(respuestas_numericas)

    # ---------------------------------
    # Unir datos
    # ---------------------------------

    datos_completos = unir_datos(datos, respuestas_numericas)

    print("\nDatos completos:")
    print(datos_completos)

    # ---------------------------------
    # DataFrame final adaptado para el modelo
    # ---------------------------------

    df_final = preparar_dataframe_modelo(datos_completos)
    print("\nVariables del modelo:")
    print(variables_modelo)
    print("\nDataFrame listo para el modelo:")
    print(df_final)
    print("\nColumnas del DataFrame:")
    print(df_final.columns.tolist())

    print("\nRealizando predicción...")
    resultado = realizar_prediccion(df_final)
    print("\nResultado del modelo:")
    print(resultado)
    print("Orden real de las clases:")
print(label_encoder.classes_)