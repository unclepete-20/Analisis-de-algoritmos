"""
    Grupo: Los 3otsitos
    Integrado por: 
    Pedro Pablo Arriola Jímenez
    Yongbum Park
    Oscar Fernando López Barrios
    José Rodrigo Barrera García
    Santiago Taracena Puga
"""

class Conversion(object):
    def __init__(self, number):
        self.number = number
        self.tape = self.number_to_tape()
        
    def number_to_tape(self):
        ones = ["1" for _ in range(self.number)]
        one_string = "".join(ones)
        return one_string
        # binary = bin(self.number)[2:]
        # bin_string = list(binary)
        # return bin_string
