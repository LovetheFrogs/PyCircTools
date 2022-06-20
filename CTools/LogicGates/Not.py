from CTools.Exceptions.CircuitToolsExceptions import NotTruthValue


class Not:
    def __init__(self):
        self.input = True
        self.output = self.__calculate_output()

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output

    def set_input(self, value):
        if type(value) is not bool:
            raise NotTruthValue

        self.input = value
        self.__calculate_output()
        return self

    def __calculate_output(self):
        self.output = not self.input
        return self
