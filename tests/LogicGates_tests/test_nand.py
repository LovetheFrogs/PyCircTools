from PyCircTools.LogicGates import Nand


def test_and_gate():
    errors = []
    nandGate = Nand()
    nandGate_overload = Nand()

    if not nandGate.get_output():
        errors.append("False and False not passed!")

    nandGate.set_input(0, True)
    if not nandGate.get_output():
        errors.append("True and False not passed!")

    nandGate_overload[0] = True
    if not nandGate_overload.get_output():
        errors.append("True and False not passed! - Overload")

    nandGate.set_input(1, True)
    if nandGate.get_output():
        errors.append("True and True not passed!")

    nandGate[1] = True
    if not nandGate_overload.get_output():
        errors.append("True and False not passed! - Overload")

    nandGate.add_input()
    if nandGate.get_numOfInputs() != 3:
        errors.append("Input adding not passed!")

    nandGate_overload.add_input()
    if nandGate_overload.get_numOfInputs() != 3:
        errors.append("Input adding not passed! - Overload")

    nandGate2 = Nand(3)
    nandGate2_overload = Nand(3)
    if nandGate2.get_numOfInputs() != 3 or nandGate2_overload.get_numOfInputs() != 3:
        errors.append("Multiple inputs when building not passed!")

    if not nandGate2.get_output() or not nandGate2_overload.get_output():
        errors.append("Output when 3 inputs not passed!")

    if not nandGate2.set_input(0, True).set_input(1, True).get_output():
        errors.append("True and True and False not passed!")

    nandGate2_overload[0] = True
    nandGate2_overload[1] = True
    if not nandGate2_overload.get_output():
        errors.append("True and True and False not passed! - Overload")


    nandGate2.remove_input()
    if not nandGate2.get_numOfInputs() == 2:
        errors.append("Removing item not passed!")

    if nandGate2.get_output():
        errors.append("Testing output after removing input not passed!")


    nandGate2[0] = False
    if not nandGate2.get_output():
        errors.append("Testing output after removing input not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
    print("No errors in NAND gate...")

if __name__ == "__main__":
    test_and_gate()