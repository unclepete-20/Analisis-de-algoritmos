"""
    Grupo: Los 3otsitos
    Integrado por: 
    Pedro Pablo Arriola Jímenez
    Yongbum Park
    Oscar Fernando López Barrios
    José Rodrigo Barrera García
    Santiago Taracena Puga
    Roberto Rios 
"""

from Conversion import Conversion
from TuringFibonacci import TuringFibonacci
import time
import sys

number = 0

try:
    number = int(input("Ingrese un número: "))
except ValueError:
    print("Error: el valor ingresado no es un número entero.")
    sys.exit(1)

tape = Conversion(number).tape
turing = TuringFibonacci(
    input_string=tape,
    states=['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11'],
    alphabet=['1', 'B'],
    initial_state='q0',
    final_state='q11',
)

start = time.time()
salida = turing.compute_fibonacci()
end = time.time() - start

print(len(salida))
print("Tiempo", end)
