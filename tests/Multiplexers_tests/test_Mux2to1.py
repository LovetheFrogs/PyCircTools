from CTools import NotTruthValue, NonExistingInput
from CTools.Multiplexers import Mux2to1


def test_Mux2to1():
    errors = []
    mux = Mux2to1()

    if mux.get_output():
        errors.append("Base get output test not passed!")

    if mux.set_set(True).get_output():
        errors.append("False, False with set to True test not passed!")

    if mux.set_input(1, True).set_set(False).get_output():
        errors.append("False, True with set to False test not passed!")

    if not mux.set_set(True).get_output():
        errors.append("False, True with set to True test not passed!")

    if not mux.set_input(0, True).set_input(1, False).set_set(False).get_output():
        errors.append("True, False with set to False test not passed!")

    if mux.set_set(True).get_output():
        errors.append("True, False with set to True test not passed!")

    if not mux.set_input(1, True).set_set(False).get_output():
        errors.append("True, True with set to False test not passed!")

    if not mux.set_set(True).get_output():
        errors.append("True, True with set to True test not passed!")

    try:
        mux.set_set(1)
        errors.append("Set to not truth test not passed!")
    except NotTruthValue:
        pass

    try:
        mux.set_input(-1, True)
        errors.append("Input to not existing input test not passed!")
    except NonExistingInput:
        pass

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
    