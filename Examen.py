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
    },
    {
        "pregunta": "¿Cual puede ser una manera para ayudar a mejorar el cambio climatico?",
        "opciones": [
            "A: Reciclar y uso menor de combustibles fosiles",
            "B: Votar toda nuestra basura al mar",
            "C: Dejar de comer",
            "D: No se puede hacer nada para ayudar"
        ],
        "respuesta": "A",
        "explicacion": "Lo mejor para solucionar y mejorar el cambio climatico es ir reciclando lo que usamos para no contaminar tanto y reducir lo que usamos los combustibles fosiles"
    },
    {
        "pregunta": "¿Cómo afecta el cambio climático a la biodiversidad en los ecosistemas terrestres y marinos?",
        "opciones": [
            "A: Ayuda en la ",
            "B: Provoca pérdida de especies y hábitats",
            "C: No afecta a la biodiversidad, solo al clima",
            "D: Hace que todos los animales se adapten fácilmente "
        ],
        "respuesta": "B",
        "explicacion": "El cambio climatica afecta mucho la biodiversidad por destruir y cambiar el los ecosistemas del planeta"
    },
]


def obtener_pregunta_aleatoria():
    if preguntas:
        indice = random.randrange(len(preguntas)) 
        return preguntas.pop(indice)  
    else:
        return None  
