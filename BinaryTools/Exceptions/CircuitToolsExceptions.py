class CircuitToolsException(Exception):
    def __init__(self, msg="CircuitTools Exception."):
        self.msg = msg
        super().__init__(self.msg)


class NotTruthValue(CircuitToolsException):
    def __init__(self, msg="Not a supported value 'True' or 'False'."):
        self.msg = msg
        super().__init__(self.msg)
        