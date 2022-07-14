from PyCircTools.LogicGates import Nand


def test_and_gate():
    nandGate = Nand()
    nandGate_overload = Nand()

    assert (bool)(nandGate.get_output()), ("False and False not passed!")

    nandGate.set_input(0, True)
    assert (bool)(nandGate.get_output()), ("True and False not passed!")

    nandGate_overload[0] = True
    assert (bool)(nandGate_overload.get_output()), ("True and False not passed! - Overload")

    nandGate.set_input(1, True)
    assert not (bool)(nandGate.get_output()), ("True and True not passed!")

    nandGate[1] = True
    assert (bool)(nandGate_overload.get_output()), ("True and True not passed! - Overload")

    nandGate.add_input()
    assert (nandGate.get_numOfInputs() == 3), ("Input adding not passed!")

    nandGate2 = Nand(3)
    nandGate2_overload = Nand(3)
    assert nandGate2.get_numOfInputs() == 3 or nandGate2_overload.get_numOfInputs() == 3, ("Multiple inputs when building not passed!")

    assert (bool)(nandGate2.get_output()) or (bool)(nandGate2_overload.get_output()) ,("Output when 3 inputs not passed!")

    nandGate2.set_input(0, True)
    nandGate2.set_input(1, True)
    assert (bool)(nandGate2.get_output()) ,("True and True and False not passed!")

    nandGate2_overload[0] = True
    nandGate2_overload[1] = True
    assert (bool)(nandGate2_overload.get_output()) ,("True and True and False not passed! - Overload")


    nandGate2.remove_input()
    assert (nandGate2.get_numOfInputs() == 2) ,("Removing item not passed!")

    assert not (bool)(nandGate2.get_output()) ,("Testing output after removing input not passed!")

    nandGate2[0] = False
    assert (bool)(nandGate2.get_output()) ,("Testing output after removing input not passed!")

    print("No errors in NAND gate...")

if __name__ == "__main__":
    test_and_gate()