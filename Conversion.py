class Conversion(object):
    def __init__(self, number):
        self.number = number
        self.tape = self.number_to_tape()
        
    def number_to_tape(self):
        ones_list = ['1' for _ in range(self.number)]
        ones_string = ''.join(ones_list)
        print(ones_string) # <-- Add this line to check if the string is being created correctly
        return ones_string
