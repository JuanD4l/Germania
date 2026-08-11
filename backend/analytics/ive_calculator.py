"""Módulo de cálculo del Índice de Vulnerabilidad Estudiantil (IVE)."""

# Pesos definidos en el Plan de Trabajo de Germania
PESO_ASISTENCIA = 0.50
PESO_RENDIMIENTO = 0.30
PESO_SOCIOECONOMICO = 0.20


def calcular_ive(
    asistencia: float,
    rendimiento: float,
    factor_socioeconomico: float
) -> float:
    """
    Calcula el Índice de Vulnerabilidad Estudiantil (IVE).

    Aplica una combinación lineal ponderada sobre tres variables
    normalizadas. El resultado es un valor entre 0.0 y 1.0, donde
    valores superiores a 0.7 activan la alerta roja de deserción.

    Args:
        asistencia (float): Porcentaje de asistencia del periodo (0.0 - 1.0).
        rendimiento (float): Promedio de calificaciones normalizado (0.0 - 1.0).
        factor_socioeconomico (float): Puntaje SISBEN normalizado (0.0 - 1.0).

    Returns:
        float: Valor del IVE para el estudiante en el periodo evaluado.
    """
    # Validación básica de rangos
    if not (0.0 <= asistencia <= 1.0):
        raise ValueError("asistencia debe estar entre 0.0 y 1.0")
    if not (0.0 <= rendimiento <= 1.0):
        raise ValueError("rendimiento debe estar entre 0.0 y 1.0")
    if not (0.0 <= factor_socioeconomico <= 1.0):
        raise ValueError("factor_socioeconomico debe estar entre 0.0 y 1.0")

    # Factores de riesgo (mayor valor = mayor vulnerabilidad)
    fa = 1.0 - asistencia          # baja asistencia → alto riesgo
    ra = 1.0 - rendimiento         # bajo rendimiento → alto riesgo
    esa = factor_socioeconomico    # ya viene como factor de riesgo

    ive = (fa * PESO_ASISTENCIA) + (ra * PESO_RENDIMIENTO) + (esa * PESO_SOCIOECONOMICO)

    # Redondeo a 4 decimales para estabilidad en pruebas
    return round(ive, 4)