from PyCircTools import Adder, Not, NotTruthValue


class Subtractor(Adder):
    def __init__(self, full=False):
        super().__init__(full)
        self.B = Not().set_input(self.B).get_output()

    def set_B(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.B = Not().set_input(value).get_output()
        super()._calculate_output()
        return self
