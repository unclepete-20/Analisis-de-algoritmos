class Tape(object):
    def __init__(self, input_string):
        self.tape = ['B'] * 100  
        self.head_position = 0
        self.result = ''
        for i in range(len(input_string)):
            self.tape[i] = input_string[i]
        print(self.tape) # <-- Add this line to check the contents of the tape
        print(self.head_position) # <-- Add this line to check the current head position

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
        current_position = 0
        print("len del tape: ", len(self.tape))
        print("sel.tape: ",self.tape)
        while current_position < len(self.tape):
            if self.tape[current_position] != 'B':
                print("sel.tape no es B: ",self.tape[current_position])
                output += self.tape[current_position]
            current_position += 1
        self.result = output
        return output