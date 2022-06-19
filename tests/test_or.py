from BinaryTools.LogicGates import Or


def test_or_gate():
    errors = []
    orGate = Or.Or()

    if orGate.get_output():
        errors.append("False and False not passed!")

    orGate.set_input(0, True)
    if not orGate.get_output():
        errors.append("True and False not passed!")

    orGate.set_input(1, True)
    if not orGate.get_output():
        errors.append("True and True not passed!")

    orGate.add_input()
    if not orGate.get_numOfInputs() == 3:
        errors.append("Input adding not passed!")

    orGate2 = Or.Or(3)
    if not orGate2.get_numOfInputs() == 3:
        errors.append("Multiple inputs when building not passed!")

    if not orGate2.set_input(0, True).set_input(1, True).get_output():
        errors.append("True and True and False not passed!")

    orGate2.remove_input()
    if not orGate2.get_numOfInputs() == 2:
        errors.append("Removing item not passed!")

    if not orGate2.get_output():
        errors.append("Testing output after removing input not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
