from PyCircTools.LogicGates import And


def test_and_gate():
    errors = []
    andGate = And.And()

    if andGate.get_output():
        errors.append("False and False not passed!")

    andGate.set_input(0, True)
    if andGate.get_output():
        errors.append("True and False not passed!")

    andGate.set_input(1, True)
    if not andGate.get_output():
        errors.append("True and True not passed!")

    andGate.add_input()
    if not andGate.get_numOfInputs() == 3:
        errors.append("Input adding not passed!")

    andGate2 = And.And(3)
    if not andGate2.get_numOfInputs() == 3:
        errors.append("Multiple inputs when building not passed!")

    if andGate2.set_input(0, True).set_input(1, True).get_output():
        errors.append("True and True and False not passed!")

    andGate2.remove_input()
    if not andGate2.get_numOfInputs() == 2:
        errors.append("Removing item not passed!")

    if not andGate2.get_output():
        errors.append("Testing output after removing input not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
