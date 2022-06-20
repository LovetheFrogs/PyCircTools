class LogicGateException(Exception):
    def __init__(self, msg="Logic gate Exception."):
        self.msg = msg
        super().__init__(self.msg)


class NonPositiveInput(LogicGateException):
    def __init__(self, msg="Number of inputs must be a positive value greater than 0."):
        self.msg = msg
        super().__init__(self.msg)


class NotAnInput(LogicGateException):
    def __init__(self, msg="Value higher than number of inputs."):
        self.msg = msg
        super().__init__(self.msg)
