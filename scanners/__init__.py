"""
Módulo de wrappers de ferramentas de varredura.
Inclui integração com Zgrab e Nmap.
"""

from .zgrab_scan import run_zgrab
from .nmap_scan import run_nmap

__all__ = ["run_zgrab", "run_nmap"]
