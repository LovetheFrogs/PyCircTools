from PyCircTools import NotTruthValue, NotControlList, WrongSize


class Extender:
    def __init__(self, into=2, out=4, pure=True):
        self.numInto = into
        self.numOut = out
        self.pure = pure
        self.input = [False] * into
        self.output = self.__calculate_output()

    def get_numIn(self):
        return self.numInto

    def get_numOut(self):
        return self.numOut

    def get_input(self):
        return self.input

    def get_output(self):
        return self.output

    def get_pure(self):
        return self.pure

    def set_input(self, values, pure=True):
        if type(pure) is not bool:
            raise NotTruthValue

        if type(values) is not list:
            raise NotControlList

        for item in values:
            if type(item) is not bool:
                raise NotControlList

        if len(values) != self.numInto:
            raise WrongSize(len(values), self.numInto)

        self.input = values
        self.set_pure(pure)
        self.output == self.__calculate_output()

        return self

    def set_pure(self, value):
        if type(value) is not bool:
            raise NotTruthValue

    def __calculate_output(self):
        output = []
        if self.pure:
            for i in range(self.numOut):
                if i < self.numInto:
                    output.append(self.input[i])
                else:
                    output.append(False)

        else:
            for i in range(self.numOut):
                if i < self.numInto:
                    output.append(self.input[i])
                else:
                    output.append(self.input[self.numInto - 1])

        return output
