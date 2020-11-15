#importing
from interfaces import IArithmeticsMult 

#multiplication
class Multiply(IArithmeticsMult):
    def Multiplication(A, B):
        #returning value
        if(A>B):
            print("A is bigger than B")
            return A*B
        else:
            return A*B
        