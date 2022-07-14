from PyCircTools.LogicGates import Xor


def test_or_gate():
    xorGate = Xor()
    xorGate_overload = Xor()

    assert (bool)(xorGate.get_output()), ("False and False not passed!")

    xorGate.set_input(0, True)
    assert (bool)(xorGate.get_output()),("True and False not passed!")

    xorGate_overload[0] = True
    assert (bool)(xorGate_overload.get_output()),("True and False not passed!")

    xorGate.set_input(1, True)
    assert not (bool)(xorGate.get_output()), ("True and True not passed!")

    xorGate_overload[1] = True
    assert not (bool)(xorGate_overload.get_output()), ("True and True not passed!")

    xorGate.add_input()
    assert xorGate.get_numOfInputs() == 3, ("Input adding not passed!")

    xorGate2 = Xor(3)
    assert xorGate2.get_numOfInputs() == 3, ("Multiple inputs when building not passed!")

    assert not (bool)(xorGate2.set_input(0, True).set_input(1, True).get_output()), ("True and True and False not passed!")

    xorGate2.remove_input()
    assert xorGate2.get_numOfInputs() == 2, ("Removing item not passed!")

    assert not (bool)(xorGate2.get_output()), ("Testing output after removing input not passed!")

    print("No errors in XOR gate...")

if __name__ == "__main__":
    test_or_gate()
