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
