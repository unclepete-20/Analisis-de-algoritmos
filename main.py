"""
    Grupo: Los 3otsitos
    Integrado por: 
    Pedro Pablo Arriola Jímenez
    Yongbum Park
    Oscar Fernando López Barrios
    José Rodrigo Barrera García
    Santiago Taracena Puga
"""

from Conversion import Conversion
from TuringFibonacci import TuringFibonacci

number = 10

tape = Conversion(number).tape
turing = TuringFibonacci(tape)

salida = turing.compute_fibonacci()

print(salida)