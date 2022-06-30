"""
PyCircTools LogicGates module Exceptions.
"""


class LogicGateException(Exception):
    """
    LogicGateException is the parent Exception class for all PyCircTools.LogicGates related Exceptions
    """
    def __init__(self, msg="Logic gate Exception."):
        self.msg = msg
        super().__init__(self.msg)


class NonPositiveInput(LogicGateException):
    """
    NonPositiveInput is raised when the number of inputs for a Logic Gate is lower than 1, as this is the minimum number
    of inputs of any logic gate.
    """
    def __init__(self, msg="Number of inputs must be a positive value greater than 0."):
        self.msg = msg
        super().__init__(self.msg)


class NotAnInput(LogicGateException):
    """
    NotAnInput is raised when the selected input does not exist.
    """
    def __init__(self, msg="Value higher than number of inputs."):
        self.msg = msg
        super().__init__(self.msg)
