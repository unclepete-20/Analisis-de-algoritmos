"""
    Grupo: Los 3otsitos
    Integrado por: 
    Pedro Pablo Arriola Jímenez
    Yongbum Park
    Oscar Fernando López Barrios
    José Rodrigo Barrera García
    Santiago Taracena Puga
"""

from Tape import Tape

class TuringFibonacci(object):
    def __init__(self, input_string, states, alphabet, initial_state, final_state):
        self.transitions = {
            ('q0', '1'): ('q1', 'B', 'R'),
            ('q1', '1'): ('q1', '1', 'R'),
            ('q1', 'B'): ('q2', 'B', 'L'),
            ('q2', '1'): ('q3', 'B', 'L'),
            ('q3', '1'): ('q3', '1', 'L'),
            ('q3', 'B'): ('q4', 'B', 'R'),
            ('q4', '1'): ('q5', 'B', 'R'),
            ('q4', 'B'): ('q9', 'B', 'R'),  # Cambio de 'q5' a 'q9'
            ('q5', '1'): ('q5', '1', 'R'),
            ('q5', 'B'): ('q6', 'B', 'L'),
            ('q6', '1'): ('q7', 'B', 'L'),
            ('q7', '1'): ('q8', '0', 'R'),  # Cambio de 'B' a '0'
            ('q7', 'B'): ('q9', 'B', 'R'),
            ('q8', '1'): ('q8', '1', 'R'),
            ('q8', 'B'): ('q9', 'B', 'R'),
            ('q9', 'B'): ('q10', 'B', 'L'),
            ('q10', '1'): ('q11', 'B', 'L'),
            ('q11', '1'): ('q11', '1', 'L'),
            ('q11', 'B'): ('q2', '1', 'L'),
            ('q0', 'B'): ('q0', 'B', 'R'), # Transición adicional para el estado q0 y el símbolo 1
        }
        self.states = lambda n: n if (n <= 1) else self.states(n - 1) + self.states(n - 2)
        self.tape = Tape(input_string)
        self.state = 'q0'
        automata_file = open("TuringFibonacci.txt", "w")
        automata_file.write(f"Estados: {states}\n")
        automata_file.write(f"Alfabeto: {alphabet}\n")
        automata_file.write(f"Estado inicial: {initial_state}\n")
        automata_file.write(f"Estado final: {final_state}\n")
        automata_file.write("Transiciones:\n")
        for transition in self.transitions:
            automata_file.write(f"\t{transition}\n")
        automata_file.close()

    def read_symbol(self):
        symbol = self.tape.read()
        if (self.state, symbol) not in self.transitions:
            print(f"Error: no hay transición definida para el estado {self.state} y el símbolo {symbol}.")
            return None
        return symbol

    def compute_fibonacci(self):
        tn = len(self.tape.get_output_string())
        file = open("res.txt", "w")
        while self.state != 'q10':
            symbol = self.read_symbol()
            if symbol is None:
                return None
            new_state, new_symbol, move = self.transitions[(self.state, symbol)]
            next_state = self.states(tn)
            print(f"Current state: {self.state}")
            print(f"Symbol read: {symbol}")
            s = f"New transition: ({self.state}, {symbol}) -> ({new_state}, {new_symbol}, {move})"
            print(s)
            file.write(s[16::])
            file.write('\n')
            self.state = new_state
            self.tape.write(new_symbol)
            result = ["1" for _ in range(next_state)]
            if move == 'L':
                self.tape.move_left()
            elif move == 'R':
                self.tape.move_right()
            elif self.state == 'q10':
                self.tape.save_output(new_symbol)
            print(f"New head position: {self.tape.head_position}")
        return result
