from PyCircTools import DFlipflop, NotTruthValue


class Shifter:
    def __init__(self, num=2):
        self.num_of_inputs = num
        self.input = [False] * num
        self.clock = False
        self.output = self.__calculate_output()

    def get_numOfInputs(self):
        return self.num_of_inputs

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output

    def get_clock(self):
        return self.clock

    def set_clock(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.clock = value
        self.output = self.__calculate_output()
        return self

    def set_input(self, values):
        if type(values) is not bool:
            raise NotTruthValue

        self.input = values
        self.output = self.__calculate_output()
        return self

    def __calculate_output(self):
        output = [False] * self.num_of_inputs
        if self.clock:
            for i in range(self.num_of_inputs):
                output[i] = DFlipflop().set_D(self.input[i]).set_enable(True).get_Q()

        return output
