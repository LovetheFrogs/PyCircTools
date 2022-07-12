from PyCircTools import And, Or, Adder, Subtractor, Mux2to1, Mux4to1, NotTruthValue
from PyCircTools.Exceptions.OperatorsExceptions import NotControlList, WrongSize


class Alu:
    def __init__(self):
        self.A = False
        self.B = False
        self.Operation = [False, False]
        self.CarrySel = False
        self.conj = And()
        self.disj = Or()
        self.adder = Adder()
        self.sub = Subtractor()
        self.mux = Mux4to1()
        self.carrSel = Mux2to1()
        self.output = self.mux.get_output()
        self.carryOut = self.carrSel.get_output()
        self.__cal_modules()

    def get_A(self):
        return self.A

    def get_B(self):
        return self.B

    def get_op(self):
        return self.Operation

    def get_output(self):
        return self.output

    def get_carryOut(self):
        return self.carryOut

    def set_A(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.A = value
        self.__cal_modules()
        return self

    def set_B(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.B = value
        self.__cal_modules()
        return self

    def set_op(self, op_code):
        if type(op_code) is not list(bool):
            raise NotControlList

        if len(op_code) != 2:
            raise WrongSize(len(op_code), 2)

        # CarrySel control signal's value is the same as the most significant input from op_code.
        self.Operation = op_code
        self.CarrySel = op_code[1]
        self.__cal_modules()
        return self
    
    def __cal_modules(self):
        self.conj.set_input(0, self.A).set_input(1, self.B)
        self.disj.set_input(0, self.A).set_input(1, self.B)
        self.adder.set_A(self.A).set_B(self.B)
        self.sub.set_A(self.A).set_B(self.B)

        for count, value in enumerate(self.Operation):
            self.mux.set_set(count, value)

        self.mux.set_input(0, self.conj.get_output()).set_input(1, self.disj.get_output())\
            .set_input(2, self.adder.get_output()).set_input(3, self.sub.get_output())
        self.output = self.mux.get_output()

        self.carrSel.set_set(self.CarrySel)
        self.carrSel.set_input(0, self.adder.get_carryOut()).set_input(1, self.sub.get_carryOut())
        self.carryOut = self.carrSel.get_output()
