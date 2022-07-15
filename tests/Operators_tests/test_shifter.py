from PyCircTools import Shifter


def test_shifter():
    shift = Shifter()

    assert shift.set_input([True, False, False, False]).set_clock(True).get_output() == [False, True, False, False]
    assert shift.set_D(True).get_output() == [False, False, False, True]
    assert shift.set_input([True, True, False, False]).get_input() == [True, True, False, False]
    assert shift.get_numOfInputs() == 4
    assert shift.get_D() is True
    assert shift.get_positions() == 1

    _shift = Shifter(num=16).set_input([False, False, False, False, False, False, False, False, False, False, False,
                                        False, False, False, False, True]).set_clock(True)

    assert _shift.get_output() == [True, False, False, False, False, False, False, False, False, False, False, False,
                                   False, False, False, False]
    assert _shift.set_D(True).get_output() == [False, False, False, False, False, False, False, False, False, False,
                                               False, False, False, False, True, False]

    _shift3 = Shifter(pos=3).set_input([False, True, False, False]).set_clock(True)

    assert _shift3.get_output() == [True, False, False, False]
    assert _shift3.set_D(True).get_output() == [False, False, True, False]

    _shift8_4 = Shifter(8, 4, True).set_input([False, False, False, False, False, False, False, True]).set_clock(True)

    assert _shift8_4.get_output() == [False, False, False, True, False, False, False, False]
    assert _shift8_4.set_D(False).get_output() == [False, False, False, True, False, False, False, False]
