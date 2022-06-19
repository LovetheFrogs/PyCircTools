class Nand:
    def __init__(self, inputNumber=2):
        self.input = self.__create_input(inputNumber)
        self.output = True
        self.numOfInputs = inputNumber

    def get_input(self, num):
        return self.input[num]

    def get_output(self):
        return self.output

    def get_numOfInputs(self):
        return self.numOfInputs

    def set_input(self, num, value):
        self.input[num] = value
        self.__calculate_output()
        return self

    def __calculate_output(self):
        output = False
        for value in self.input:
            output = not(output and value)
        self.output = output
        return self

    def add_input(self):
        self.input.append(False)
        self.numOfInputs += 1
        self.output = self.__calculate_output()
        return self

    def remove_input(self):
        self.input.pop()
        self.output = self.__calculate_output()
        self.numOfInputs -= 1
        return self

    @staticmethod
    def __create_input(num):
        return [False] * num
