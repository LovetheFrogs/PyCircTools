from PyCircTools import DFlipflop, NotTruthValue, NotControlList, WrongSize
# Copy is used to generate a copy of input so that it is not deleted when calculating output.
import copy


class Shifter:
    def __init__(self, num=4, positions=1):
        self.num_of_inputs = num
        self.positions = positions
        self.D = False
        self.input = [False] * num
        self.clock = False
        self.output = self.__calculate_output()

    def get_numOfInputs(self):
        return self.num_of_inputs

    def get_positions(self):
        return self.positions

    def get_D(self):
        return self.D

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output

    def get_clock(self):
        return self.clock

    def set_D(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.D = value
        self.output = self.__calculate_output()
        return self

    def set_clock(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.clock = value
        self.output = self.__calculate_output()
        return self

    def set_input(self, values):
        if type(values) is not list:
            raise NotControlList

        for val in values:
            if type(val) is not bool:
                raise NotControlList

        if len(values) > self.num_of_inputs:
            raise WrongSize(len(values), self.num_of_inputs)

        self.input = values
        self.output = self.__calculate_output()
        return self

    def __calculate_output(self):
        output = [False] * self.num_of_inputs
        if self.clock:
            output = copy.copy(self.input)
            for _ in range(self.positions):
                inp = copy.copy(output)
                if not self.D:
                    for i in range(self.num_of_inputs):
                        if i == 0:
                            output[i] = DFlipflop().set_D(inp[self.num_of_inputs - 1]).set_enable(True).get_Q()
                        else:
                            output[i] = DFlipflop().set_D(inp[i - 1]).set_enable(True).get_Q()

                else:
                    for i in range(self.num_of_inputs):
                        if i == self.num_of_inputs - 1:
                            output[i] = DFlipflop().set_D(inp[0]).set_enable(True).get_Q()
                        else:
                            output[i] = DFlipflop().set_D(inp[i + 1]).set_enable(True).get_Q()

        return output
