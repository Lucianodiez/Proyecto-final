import random

preguntas = [
    {
        "pregunta": "¿Cuál de los siguientes fenómenos es un efecto del cambio climático?",
        "opciones": [
            "A: Aumento en la frecuencia de inundaciones",
            "B: Incremento de eventos de tornados",
            "C: Prolongadas sequías",
            "D: Todas las anteriores"
        ],
        "respuesta": "D",
        "explicacion": "El cambio climático influye en todos estos fenómenos."
    },
    {
        "pregunta": "¿Qué gas de efecto invernadero es el más abundante en la atmósfera?",
        "opciones": [
            "A: Dióxido de carbono (CO2)",
            "B: Metano (CH4)",
            "C: Vapor de agua (H2O)",
            "D: Óxido nitroso (N2O)"
        ],
        "respuesta": "C",
        "explicacion": "El vapor de agua es el gas de efecto invernadero más abundante en la atmósfera."
    },
    {
        "pregunta": "¿Cuál es una de las principales causas del cambio climático?",
        "opciones": [
            "A: La rotación de la Tierra",
            "B: La quema de combustibles fósiles",
            "C: El ciclo lunar",
            "D: La fotosíntesis de las plantas"
        ],
        "respuesta": "B",
        "explicacion": "La quema de combustibles fósiles es una de las principales causas del cambio climático."
    }
]


def obtener_pregunta_aleatoria():
    return random.choice(preguntas)