from PyCircTools.Latches import JKFlipflop


def test_JKFlipflop():
    errors = []
    flipflop = JKFlipflop()

    if flipflop.get_Q():
        errors.append("Q output when created flipflop is not False!")

    if flipflop.set_J(True).get_Q():
        errors.append("Operation done when clock is False!")

    if not flipflop.set_clock(True).set_J(False).set_K(True).get_Q() and flipflop.get_Qp():
        pass
    else:
        errors.append("Not J and K test not passed!")

    if flipflop.set_J(True).set_K(False).get_Q() and not flipflop.get_Qp():
        pass
    else:
        errors.append("J and not K test not passed!")

    previous = [flipflop.get_Q(), flipflop.get_Qp()]
    if flipflop.set_K(True).get_Q() == previous[1] and flipflop.get_Qp() == previous[0]:
        pass
    else:
        errors.append("J and K test not passed!")

    previous = [flipflop.get_Q(), flipflop.get_Qp()]
    if flipflop.set_J(False).set_K(False).get_Q() == previous[0] and flipflop.get_Qp() == previous[1]:
        pass
    else:
        errors.append("Not J and not K test not passed!")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
