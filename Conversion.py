

class Conversion(object):
    def __init__(self, number):
        self.number = number
        self.tape = self.number_to_tape()
        
    
    def number_to_tape(self):
        
        # Crea una lista de caracteres '1' de longitud num
        ones_list = ['1' for _ in range(self.number)]

        # Une los caracteres de la lista en una cadena
        ones_string = ''.join(ones_list)

        return ones_string