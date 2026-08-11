"""Pruebas unitarias del algoritmo IVE (Índice de Vulnerabilidad Estudiantil)."""

import sys
import unittest
from pathlib import Path

# Agrega la carpeta backend al path para que encuentre analytics
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analytics.ive_calculator import calcular_ive

class TestCalcularIVE(unittest.TestCase):
    """Casos de prueba para la función calcular_ive."""

    def test_estudiante_bajo_riesgo(self):
        """Asistencia alta + buen rendimiento + bajo factor socioeconómico → IVE bajo."""
        ive = calcular_ive(
            asistencia=0.95,
            rendimiento=0.90,
            factor_socioeconomico=0.10
        )
        self.assertLess(ive, 0.30)
        self.assertGreaterEqual(ive, 0.0)

    def test_estudiante_alto_riesgo(self):
        """Baja asistencia + bajo rendimiento + alto factor socioeconómico → IVE alto."""
        ive = calcular_ive(
            asistencia=0.30,
            rendimiento=0.30,
            factor_socioeconomico=0.90
        )
        # FA=0.70, RA=0.70, ESA=0.90
        # IVE = 0.70*0.5 + 0.70*0.3 + 0.90*0.2 = 0.74
        self.assertGreater(ive, 0.70)   # Debe activar alerta roja
        self.assertAlmostEqual(ive, 0.74, places=4)

    def test_valores_limite_minimos(self):
        """Todos los valores en 0.0 → IVE máximo teórico (1.0)."""
        ive = calcular_ive(0.0, 0.0, 1.0)
        self.assertEqual(ive, 1.0)

    def test_valores_limite_maximos(self):
        """Asistencia y rendimiento perfectos + factor socioeconómico 0 → IVE mínimo (0.0)."""
        ive = calcular_ive(1.0, 1.0, 0.0)
        self.assertEqual(ive, 0.0)

    def test_umbral_alerta_roja(self):
        """Caso exacto en el umbral de alerta roja (> 0.7)."""
        ive = calcular_ive(
            asistencia=0.50,
            rendimiento=0.50,
            factor_socioeconomico=0.80
        )
        # FA = 0.50, RA = 0.50, ESA = 0.80
        # IVE = (0.50*0.5) + (0.50*0.3) + (0.80*0.2) = 0.25 + 0.15 + 0.16 = 0.56
        self.assertAlmostEqual(ive, 0.56, places=4)

    def test_validacion_asistencia_fuera_de_rango(self):
        """Debe lanzar ValueError si asistencia está fuera de 0.0-1.0."""
        with self.assertRaises(ValueError):
            calcular_ive(asistencia=1.5, rendimiento=0.8, factor_socioeconomico=0.3)

    def test_validacion_rendimiento_fuera_de_rango(self):
        """Debe lanzar ValueError si rendimiento está fuera de 0.0-1.0."""
        with self.assertRaises(ValueError):
            calcular_ive(asistencia=0.8, rendimiento=-0.1, factor_socioeconomico=0.3)

    def test_validacion_factor_socioeconomico_fuera_de_rango(self):
        """Debe lanzar ValueError si factor_socioeconomico está fuera de 0.0-1.0."""
        with self.assertRaises(ValueError):
            calcular_ive(asistencia=0.8, rendimiento=0.7, factor_socioeconomico=1.2)


if __name__ == "__main__":
    unittest.main()