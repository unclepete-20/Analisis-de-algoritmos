
from Tape import Tape

class TuringFibonacci(object):
    def __init__(self, input_string):
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
        self.tape = Tape(input_string)
        self.state = 'q0'

    def read_symbol(self):
        symbol = self.tape.read()
        if (self.state, symbol) not in self.transitions:
            print(f"Error: no hay transición definida para el estado {self.state} y el símbolo {symbol}.")
            return None
        return symbol

    def compute_fibonacci(self):
        while self.state != 'q10':
            symbol = self.read_symbol()
            if symbol is None:
                return None
            new_state, new_symbol, move = self.transitions[(self.state, symbol)]
            self.state = new_state
            self.tape.write(new_symbol)
            if move == 'L':
                self.tape.move_left()
            elif move == 'R':
                self.tape.move_right()
        return self.tape.get_output_string()
