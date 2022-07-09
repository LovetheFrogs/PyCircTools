from PyCircTools import Adder, NotCorrectAdder


def test_halfAdder():
    errors = []
    half = Adder()

    if half.get_output():
        errors.append("0 + 0 != 1!")

    if half.set_A(True).get_output() and not half.get_carryOut():
        pass
    else:
        errors.append("1 + 0 != 0! || carry != 1!")

    if not half.set_B(True).get_output() and half.get_carryOut():
        pass
    else:
        errors.append("1 + 1 != 1! || carry != 0!")

    if half.set_A(False).get_output() and not half.get_carryOut():
        pass
    else:
        errors.append("0 + 1 != 0! || carry != 1!")

    try:
        half.set_carryIn(False)
        errors.append("Shouldn't allow to set carryIn for a half-adder!")
    except NotCorrectAdder:
        pass

    assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_fullAdder():
    errors = []
    half = Adder(True)

    if half.get_output():
        errors.append("0 + 0 != 1!")

    if half.set_carryIn(True).get_output() and not half.get_carryOut():
        pass
    else:
        errors.append("0 + 0 + 1 error!")

    if half.set_carryIn(False).set_B(True).get_output() and not half.get_carryOut():
        pass
    else:
        errors.append("0 + 1 + 0 error!")

    if not half.set_carryIn(True).get_output() and half.get_carryOut():
        pass
    else:
        errors.append("0 + 1 + 1 error!")

    if half.set_carryIn(False).set_A(True).set_B(False).get_output() and not half.get_carryOut():
        pass
    else:
        errors.append("1 + 0 + 0 error!")

    if not half.set_carryIn(True).get_output() and half.get_carryOut():
        pass
    else:
        errors.append("1 + 0 + 1 error!")

    if not half.set_carryIn(False).set_B(True).get_output() and half.get_carryOut():
        pass
    else:
        errors.append("1 + 1 + 0 error!")

    if half.set_carryIn(True).get_output() and half.get_carryOut():
        pass
    else:
        errors.append("1 + 1 + 1 error!")

    try:
        pass
    except NotCorrectAdder:
        half.set_carryIn(False)
        errors.append("Should allow to set carryIn for a full-adder!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))


if __name__ == '__main__':
    test_halfAdder()
    test_fullAdder()
