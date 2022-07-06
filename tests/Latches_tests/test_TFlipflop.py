from PyCircTools.Latches import TFlipflop


def test_TFlipflop():
    errors = []
    flipflop = TFlipflop()

    if flipflop.get_Q():
        errors.append("Q output when created flipflop is not False!")

    if flipflop.set_T(True).get_Q():
        errors.append("Operation done when clock is False!")

    if not flipflop.set_T(False).set_clock(True).get_Q() and flipflop.get_Qp():
        pass
    else:
        errors.append("Clock tests not passed!")

    if flipflop.set_T(True).get_Q() and not flipflop.get_Qp():
        pass
    else:
        errors.append("False then T test not passed!")

    if not flipflop.set_T(True).get_Q() and flipflop.get_Qp():
        pass
    else:
        errors.append("True then not T test not passed!")

    if not flipflop.set_T(False).get_Q() and flipflop.get_Qp():
        pass
    else:
        errors.append("False then not T test not passed!")

    if flipflop.set_T(True).get_Q() and not flipflop.get_Qp():
        pass
    else:
        errors.append("False then not T test not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
