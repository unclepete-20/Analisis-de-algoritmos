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


def readInput():
    # abrir y leer el archivo
    with open("test.txt", mode='r', encoding='utf-8') as file:
        for line in file.readlines():

            # definir el conjunto finito de estados
            if line[0] == 'Q':
                Q = line.split(' ')[-2].split(',')

            # definir el alfabeto de entrada
            elif line[0] == 'S':
                S = line.split(' ')[-2].split(',')

            # definir estado inicial
            elif line[0] == 's':
                s = line.split(' ')[-2]

            # conjunto de estados de aceptacion
            elif line[0] == 'F':
                F = line.split(' ')[-2].split(',')

            else:
                pass
    
        file.close()

        
        if s not in Q:
            return 'el estado inicial no forma parte del conjunto de estados'
        
        
        return ( Q, S, s, F )

Q, S, s, F = readInput()
print('Estados:'+str(Q))
print('Alfabeto de entrada:'+str(S))
print('estado inicial:'+str(s))
print('estado final:'+str(F))



tape = Conversion(number).tape
turing = TuringFibonacci(
    input_string=tape,
    states=Q,
    alphabet=S,
    initial_state=s,
    final_state=F[0],
)

start = time.time()
salida = turing.compute_fibonacci()
end = time.time() - start

print(len(salida))
print("Tiempo: ", end)
