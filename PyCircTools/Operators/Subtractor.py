from PyCircTools import Adder, Not


class Subtractor(Adder):
    def __init__(self, full=False):
        super().__init__(full)
        self.B = Not().set_input(self.B).get_output()
