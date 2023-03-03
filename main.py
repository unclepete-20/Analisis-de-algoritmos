from Conversion import Conversion
from TuringFibonacci import TuringFibonacci

number = 10

tape = Conversion(number).tape
turing = TuringFibonacci(tape)

salida = turing.compute_fibonacci()

print(salida)