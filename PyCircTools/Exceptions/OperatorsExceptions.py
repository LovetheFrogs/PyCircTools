"""
PyCircTools Operators module Exceptions.
"""


class OperatorException(Exception):
    """
    OperatorException is the parent Exception class for all PyCircTools.Operators related Exceptions.
    """
    def __init__(self, msg="Operator Exception"):
        self.msg = msg
        super().__init__(self.msg)


class NotCorrectAdder(OperatorException):
    """
    NotCorrectAdder is raised when a function is called and is not allowed for the instance of an adder used in.
    """
    def __init__(self, method=None, addr_class=False):
        if method is None:
            self.msg = "Method not allowed for an instance of a " + get_adder_type(addr_class)
        else:
            self.msg = "Method " + method + " not allowed for an instance of " + get_adder_type(addr_class)


class NotControlList(OperatorException):
    """
    NotControlList is raised when a list of operation codes is not of type bool or is not a list at all.
    """
    def __init__(self, msg="Operation code is not a list or its contents are not of type bool."):
        self.msg = msg
        super().__init__(self.msg)


class WrongSize(OperatorException):
    """
    WrongSize is raised when the list of operation codes does not have the required size.
    """
    def __init__(self, curr_size, req_size):
        self.msg = "List of size " + str(curr_size) + ". Needs to be of size " + str(req_size) + "!"
        super().__init__(self.msg)


class WrongRange(OperatorException):
    """
    WrongRange is raised when the number of inputs is lower or equal than the number of inputs in certain modules.
    """
    def __init(self, obj):
        self.msg = "Number of inputs of " + obj + " must be lower than the number of outputs."
        super().__init__(self.msg)


def get_adder_type(addr_class):
    """
    Method used to get the type of adder used.

    :param addr_class: Type of adder, either False for half-adder or True for full-adder.
    :type addr_class: bool
    :return: String containing the name of the adder.
    :rtype: str
    """
    if not addr_class:
        return "Half-adder."
    else:
        return "Full-adder."
