class obj:
    def __init__ (self, num1a, num1b, num2a, num2b, num3a, num3b):
        self.complexo1 = complex(num1a, num1b)
        self.complexo2 = complex(num2a, num2b)
        self.complexo3 = complex(num3a, num3b)
        
    def printing (self):
        print(f"SOMA = {self.complexo1+self.complexo2+self.complexo3}")
        print(f"SUBTRAÇÃO = {self.complexo1-self.complexo2-self.complexo3}")
        print(f"MULTIPLICAÇÃO = {self.complexo1*self.complexo2*self.complexo3}")
        print(f"DIVISÃO = {self.complexo1/self.complexo2/self.complexo3}\n")
        print(f"1° NÚMERO:\nparte real: {self.complexo1.real}\nparte imaginária: {self.complexo1.imag}")
        print(f"2° NÚMERO:\nparte real: {self.complexo2.real}\nparte imaginária: {self.complexo2.imag}")
        print(f"3° NÚMERO:\nparte real: {self.complexo3.real}\nparte imaginária: {self.complexo3.imag}")
        
numComplexos = obj(0, 1, 2, 3, 4, 5)
numComplexos.printing()