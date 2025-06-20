"""
Módulo de utilitários para o agente de scan.
Inclui logger estruturado e parser de resultados.
"""

from .logger import get_logger
from .parser import interpret_results

__all__ = ["get_logger", "interpret_results"]
