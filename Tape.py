class Tape(object):
    def __init__(self, input_string):
        self.tape = ['B'] * 100  # Cinta con una longitud arbitraria
        self.head_position = 0
        self.result = ''
        for i in range(len(input_string)):
            self.tape[i] = input_string[i]

    def read(self):
        return self.tape[self.head_position]

    def write(self, symbol):
        self.tape[self.head_position] = symbol

    def move_left(self):
        self.head_position -= 1
    
    def move_right(self):
        self.head_position += 1

    def save_output(self, symbol):
        self.result += symbol

    def get_output_string(self):
        output = ""
        current_position = self.head_position
        while self.tape[current_position] != 'B':
            output += self.tape[current_position]
            current_position += 1
        return output