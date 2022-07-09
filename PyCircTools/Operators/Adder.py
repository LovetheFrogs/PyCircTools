from PyCircTools.Exceptions.OperatorsExceptions import NotCorrectAdder


class Adder:
    def __init__(self, full=False):
        self.A = False
        self.B = False
        self.carryOut = False
        self.output = False
        self.full = full
        if full:
            self.carryIn = False

    def get_A(self):
        return self.A

    def get_B(self):
        return self.B

    def get_carryOut(self):
        return self.carryOut

    def get_output(self):
        return self.output

    def get_carryIn(self):
        if not self.full:
            raise(NotCorrectAdder('get_carryIn', False))

        return self.carryOut

    # Add method to convert to full adder from half adder.