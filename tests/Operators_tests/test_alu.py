from PyCircTools import Alu

def test_alu_and():
    alu = Alu()
    errors = []

    # Checking AND operation and results.
    alu.set_op([False, False])
    if alu.set_A(False).set_B(False).get_output():
        errors.append("0 and 0 error!")

    if alu.set_A(True).get_output():
        errors.append("1 and 0 error!")

    if alu.set_A(False).set_B(True).get_output():
        errors.append("0 and 1 error!")

    if not alu.set_A(True).get_output():
        errors.append("1 and 1 error!")

    assert not errors, "Errors occurred!\n{}".format("\n".join(errors))


def test_alu_or():
    alu = Alu()
    errors = []

    # Checking OR operation and results
    alu.set_op([True, False])
    if alu.set_A(False).set_B(False).get_output():
        errors.append("0 or 0 error!")

    if not alu.set_A(True).get_output():
        errors.append("1 or 0 error!")

    if not alu.set_A(False).set_B(True).get_output():
        errors.append("0 or 1 error!")

    if not alu.set_A(True).get_output():
        errors.append("1 or 1 error!")

    assert not errors, "Errors occurred!\n{}".format("\n".join(errors))


def test_alu_add():
    half = Alu()
    errors = []

    # Checking + operation and results
    half.set_op([False, True])
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

    assert not errors, "Errors occurred!\n{}".format("\n".join(errors))


def test_alu_sub():
    half = Alu()
    errors = []

    # Checking - operation and results
    half.set_op([True, True])
    if half.set_A(True).get_output() and not half.get_carryOut():
        pass
    else:
        errors.append("1 - 0 != 0! || carry != 1!")

    if not half.set_B(True).get_output() and not half.get_carryOut():
        pass
    else:
        errors.append("1 - 1 != 1! || carry != 1!")

    if half.set_A(False).get_output() and half.get_carryOut():
        pass
    else:
        errors.append("0 - 1 != 0! || carry != 0!")

    assert not errors, "Errors occurred!\n{}".format("\n".join(errors))


if __name__ == '__main__':
    test_alu_and()
    test_alu_or()
    test_alu_add()
    test_alu_sub()
