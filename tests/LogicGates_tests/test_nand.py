from PyCircTools.LogicGates import Nand


def test_and_gate():
    nandGate = Nand()
    nandGate_overload = Nand()

    assert not nandGate.get_output(), ("False and False not passed!")

    nandGate.set_input(0, True)
    assert not nandGate.get_output(), ("True and False not passed!")

    nandGate_overload[0] = True
    assert not nandGate_overload.get_output(), ("True and False not passed! - Overload")

    nandGate.set_input(1, True)
    assert nandGate.get_output(), ("True and True not passed!")

    nandGate[1] = True
    assert not nandGate_overload.get_output(), ("True and True not passed! - Overload")

    nandGate.add_input()
    assert nandGate.get_numOfInputs() != 3, ("Input adding not passed!")

    nandGate2 = Nand(3)
    nandGate2_overload = Nand(3)
    assert nandGate2.get_numOfInputs() != 3 or nandGate2_overload.get_numOfInputs() != 3, ("Multiple inputs when building not passed!")

    assert not nandGate2.get_output() or not nandGate2_overload.get_output() ,("Output when 3 inputs not passed!")

    assert not nandGate2.set_input(0, True).set_input(1, True).get_output() ,("True and True and False not passed!")

    nandGate2_overload[0] = True
    nandGate2_overload[1] = True
    assert not nandGate2_overload.get_output() ,("True and True and False not passed! - Overload")


    nandGate2.remove_input()
    assert not nandGate2.get_numOfInputs() == 2 ,("Removing item not passed!")

    assert nandGate2.get_output() ,("Testing output after removing input not passed!")

    nandGate2[0] = False
    assert not nandGate2.get_output() ,("Testing output after removing input not passed!")

    print("No errors in NAND gate...")

assert __name__ == "__main__"
    test_and_gate()