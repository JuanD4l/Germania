"""Clasificación del semáforo IVE y generación de alertas."""

from analytics.ive_calculator import calcular_ive


# Umbrales definidos para Germania
UMBRAL_ROJO = 0.70
UMBRAL_AMARILLO = 0.40


def clasificar_semaforo(ive: float) -> dict:
    """
    Clasifica el valor del IVE en uno de los tres estados del semáforo.

    Args:
        ive (float): Valor del Índice de Vulnerabilidad Estudiantil (0.0 - 1.0).

    Returns:
        dict: Diccionario con el nivel, color y mensaje de alerta.
    """
    if ive > UMBRAL_ROJO:
        return {
            "nivel": "alto",
            "color": "rojo",
            "mensaje": "Alerta roja: riesgo alto de deserción. Intervención prioritaria."
        }
    elif ive > UMBRAL_AMARILLO:
        return {
            "nivel": "medio",
            "color": "amarillo",
            "mensaje": "Alerta amarilla: riesgo moderado. Requiere seguimiento."
        }
    else:
        return {
            "nivel": "bajo",
            "color": "verde",
            "mensaje": "Sin alerta: estudiante en rango de bajo riesgo."
        }


def generar_alerta(
    asistencia: float,
    rendimiento: float,
    factor_socioeconomico: float
) -> dict:
    """
    Calcula el IVE y genera la alerta completa del semáforo.

    Args:
        asistencia (float): Porcentaje de asistencia (0.0 - 1.0).
        rendimiento (float): Promedio de calificaciones normalizado (0.0 - 1.0).
        factor_socioeconomico (float): Puntaje SISBEN normalizado (0.0 - 1.0).

    Returns:
        dict: Contiene el valor del IVE y la clasificación del semáforo.
    """
    ive = calcular_ive(asistencia, rendimiento, factor_socioeconomico)
    semaforo = clasificar_semaforo(ive)

    return {
        "ive": ive,
        "semaforo": semaforo
    }